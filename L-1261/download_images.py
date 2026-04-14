#!/usr/bin/env python3
"""Download carry-over images for L-1261."""
import os
import urllib.request

IMAGES_DIR = "/Users/Shared/projects/hp-demo/L-1261/images"
os.makedirs(IMAGES_DIR, exist_ok=True)

images = [
    ("https://img01.ecgo.jp/usr/is-tax/css/img/集合写真2.png", "group_photo.png"),
    ("https://img01.ecgo.jp/usr/is-tax/img/170927134639.jpg", "shiiki_hideyuki.jpg"),
]

for url, filename in images:
    dest = os.path.join(IMAGES_DIR, filename)
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

print("Done. Files:")
for f in os.listdir(IMAGES_DIR):
    path = os.path.join(IMAGES_DIR, f)
    print(f"  {f} ({os.path.getsize(path)} bytes)")
