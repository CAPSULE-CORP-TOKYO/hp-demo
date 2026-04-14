#!/usr/bin/env python3
"""Download images for L-1260 demo. Run manually if needed."""
import urllib.request, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

images = [
    ('https://kd-tax.com/wp-content/uploads/2019/12/962cf03585f3eeab73167feb0df5453f.png', 'logo.png'),
    ('https://kd-tax.com/wp-content/uploads/2021/08/1ada9b80f53cd279cb9957b3824332d8.jpg', 'hero-exterior.jpg'),
    ('https://kd-tax.com/wp-content/uploads/2021/03/a5b8b65768a2100850652711d99b40df-875x1024.jpg', 'representative.jpg'),
    ('https://kd-tax.com/wp-content/uploads/2021/04/image.png', 'badge-nintei.png'),
    ('https://kd-tax.com/wp-content/uploads/2020/11/c9a3498f1399945f478d605dab15348b.jpg', 'badge-yayoi.jpg'),
    ('https://kd-tax.com/wp-content/uploads/2020/04/3752c1c3c5c2edb0357e6264870547ed.png', 'badge-mf.png'),
]

outdir = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(outdir, exist_ok=True)

for url, fname in images:
    path = os.path.join(outdir, fname)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as r, open(path, 'wb') as f:
            f.write(r.read())
        print(f'OK: {fname} ({os.path.getsize(path)} bytes)')
    except Exception as e:
        print(f'FAIL: {fname} - {e}')
