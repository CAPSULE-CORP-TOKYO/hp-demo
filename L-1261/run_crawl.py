#!/usr/bin/env python3
"""One-off crawl script for L-1261 using 'load' wait instead of 'networkidle'."""
import os, json, re, sys
from urllib.parse import urldefrag, urljoin, urlparse
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
OUTDIR = "/Users/Shared/projects/hp-demo/L-1261"
BASE_URL = "https://www.is-tax.or.jp/"
MAX_PAGES = 30

EXCLUDED_EXTENSIONS = (
    ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico",
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".zip", ".rar", ".tar", ".gz", ".7z",
    ".mp3", ".mp4", ".avi", ".mov", ".webm",
    ".csv", ".txt", ".xml", ".rss", ".json",
)

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)

def slugify(url):
    parsed = urlparse(url)
    path = parsed.path
    if not path or path == "/":
        return "index"
    path = path.strip("/")
    path = re.sub(r"\.html?$", "", path, flags=re.IGNORECASE)
    slug = path.replace("/", "-")
    slug = re.sub(r"[^A-Za-z0-9._-]", "_", slug)
    return slug or "index"

def is_crawlable(url, base_netloc):
    if not url:
        return False
    if url.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return False
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc != base_netloc:
        return False
    if parsed.path.lower().endswith(EXCLUDED_EXTENSIONS):
        return False
    return True

def canonicalize(url):
    parsed = urlparse(url)
    path = parsed.path
    path = re.sub(r"/(index|default)\.(html?|php|aspx?)$", "/", path, flags=re.IGNORECASE)
    if not path:
        path = "/"
    canonical = f"{parsed.scheme}://{parsed.netloc}{path}"
    if parsed.query:
        canonical += f"?{parsed.query}"
    return canonical.rstrip("/")

def capture_page(page, url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    page.goto(url, wait_until="load", timeout=60000)
    page.wait_for_timeout(3000)
    height = page.evaluate("document.body.scrollHeight")
    for pos in range(0, int(height), 300):
        page.evaluate(f"window.scrollTo(0, {pos})")
        page.wait_for_timeout(150)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(output_dir, "screenshot.png"), full_page=True)
    html = page.content()
    with open(os.path.join(output_dir, "source.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return html

def main():
    os.makedirs(OUTDIR, exist_ok=True)
    base_parsed = urlparse(BASE_URL)
    base_netloc = base_parsed.netloc
    visited = set()
    manifest = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, user_agent=UA)
        page = ctx.new_page()

        print(f"[1/?] homepage: {BASE_URL}", file=sys.stderr)
        html = capture_page(page, BASE_URL, OUTDIR)
        visited.add(canonicalize(BASE_URL))
        manifest.append({"url": BASE_URL, "slug": "index", "path": ".", "depth": 0})

        lp = LinkExtractor()
        lp.feed(html)
        targets = []
        seen = set()
        for raw in lp.links:
            absolute = urljoin(BASE_URL, raw)
            absolute = urldefrag(absolute)[0]
            if not is_crawlable(absolute, base_netloc):
                continue
            canon = canonicalize(absolute)
            if canon in visited or canon in seen:
                continue
            seen.add(canon)
            targets.append(absolute)
        targets = targets[:MAX_PAGES - 1]
        print(f"Found {len(targets)} unique linked pages to crawl", file=sys.stderr)

        pages_dir = os.path.join(OUTDIR, "pages")
        for i, target_url in enumerate(targets, start=2):
            slug = slugify(target_url)
            base_slug = slug
            n = 2
            while os.path.exists(os.path.join(pages_dir, slug)):
                slug = f"{base_slug}-{n}"
                n += 1
            page_dir = os.path.join(pages_dir, slug)
            print(f"[{i}/{len(targets)+1}] {slug}: {target_url}", file=sys.stderr)
            try:
                capture_page(page, target_url, page_dir)
                visited.add(canonicalize(target_url))
                manifest.append({"url": target_url, "slug": slug, "path": f"pages/{slug}", "depth": 1})
            except Exception as e:
                print(f"  SKIP ({e.__class__.__name__}): {e}", file=sys.stderr)
                continue

        browser.close()

    manifest_path = os.path.join(OUTDIR, "pages-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"Captured {len(manifest)} pages -> {OUTDIR}", file=sys.stderr)

if __name__ == "__main__":
    main()
