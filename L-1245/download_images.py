#!/usr/bin/env python3
import os
import urllib.request

outdir = '/Users/Shared/projects/hp-demo/L-1245/images'
os.makedirs(outdir, exist_ok=True)

urls = [
    ('https://040tax.jp/img/logoS.png', 'logoS.png'),
    ('https://040tax.jp/img/mainLogo.svg', 'mainLogo.svg'),
    ('https://040tax.jp/img/mainLogo-w.svg', 'mainLogo-w.svg'),
]
for url, fname in urls:
    try:
        urllib.request.urlretrieve(url, os.path.join(outdir, fname))
        print(f'OK: {fname}')
    except Exception as e:
        print(f'FAIL: {fname} - {e}')
