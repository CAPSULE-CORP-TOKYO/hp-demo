#!/usr/bin/env python3
"""Download the group photo with proper URL encoding."""
import os
import urllib.request
import urllib.parse

IMAGES_DIR = "/Users/Shared/projects/hp-demo/L-1261/images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# URL-encode the Japanese filename part
base = "https://img01.ecgo.jp/usr/is-tax/css/img/"
filename_jp = "集合写真2.png"
url = base + urllib.parse.quote(filename_jp)

dest = os.path.join(IMAGES_DIR, "group_photo.png")
print(f"Downloading {url} -> {dest}")
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
})
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  OK ({len(data)} bytes)")
except Exception as e:
    print(f"  FAIL: {e}")

print("Files in images/:")
for f in os.listdir(IMAGES_DIR):
    path = os.path.join(IMAGES_DIR, f)
    print(f"  {f} ({os.path.getsize(path)} bytes)")
