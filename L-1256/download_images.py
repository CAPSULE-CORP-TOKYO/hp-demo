#!/usr/bin/env python3
"""Download carry-over images for L-1256 demo HTML."""
import urllib.request
import os

outdir = '/Users/Shared/projects/hp-demo/L-1256/images'
os.makedirs(outdir, exist_ok=True)

images = [
    ('http://www.tsubasa-p.co.jp/images/header/logo.png', 'logo.png'),
    ('http://www.tsubasa-p.co.jp/images/top/img_mainimg_takeda.jpg', 'img_mainimg_takeda.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_suizokukan.jpg', 'pic_voice_suizokukan.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_glaft.jpg', 'pic_voice_glaft.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_laugh_associates.jpg', 'pic_voice_laugh_associates.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_miyamachidori_clinic.jpg', 'pic_voice_miyamachidori_clinic.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_konnoinsatsu.jpg', 'pic_voice_konnoinsatsu.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/pic_voice_challenge.jpg', 'pic_voice_challenge.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/img_staff_v4.png', 'img_staff_v4.png'),
    ('http://www.tsubasa-p.co.jp/images/staff/pic_takeda.jpg', 'pic_takeda.jpg'),
    ('http://www.tsubasa-p.co.jp/images/staff/pic_takahashi.jpg', 'pic_takahashi.jpg'),
    ('http://www.tsubasa-p.co.jp/images/staff/pic_sato.jpg', 'pic_sato.jpg'),
    ('http://www.tsubasa-p.co.jp/images/about/pic_takeda.jpg', 'pic_takeda_about.jpg'),
    ('http://www.tsubasa-p.co.jp/images/top/img_teikoku_news.png', 'img_teikoku_news.png'),
    ('http://www.tsubasa-p.co.jp/images/footer/logo.png', 'footer_logo.png'),
]

ok = 0
fail = 0
for url, fname in images:
    dest = os.path.join(outdir, fname)
    try:
        urllib.request.urlretrieve(url, dest)
        sz = os.path.getsize(dest)
        print(f'OK: {fname} ({sz} bytes)')
        ok += 1
    except Exception as e:
        print(f'FAIL: {fname} - {e}')
        fail += 1

print(f'\nDone: {ok} OK, {fail} FAIL')
