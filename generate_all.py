#!/usr/bin/env python3
"""Generate high-quality demo sites for 20 tax accountant leads."""
import json
import os
import re

# Lead data extracted from leads.json
LEADS = [
    {"id": "L-194", "name": "矢口俊幸税理士事務所", "address": "神奈川県横浜市磯子区森１丁目５−２１ ヴェルドミール磯子 218号室", "zip": "235-0023", "phone": "045-840-3225", "area": "横浜市磯子区", "station": "磯子駅", "lat": "35.4050", "lng": "139.6170", "accent": "#1a5276", "accent2": "#2980b9", "gradient": "linear-gradient(135deg, #1a5276 0%, #2980b9 100%)"},
    {"id": "L-197", "name": "山野井千恵税理士事務所", "address": "神奈川県横浜市港南区港南中央通９−１４ ライオンズマンション港南中央 ３１４", "zip": "233-0004", "phone": "045-840-4500", "area": "横浜市港南区", "station": "港南中央駅", "lat": "35.3960", "lng": "139.5960", "accent": "#1b4332", "accent2": "#2d6a4f", "gradient": "linear-gradient(135deg, #1b4332 0%, #2d6a4f 100%)"},
    {"id": "L-198", "name": "西田公一 税理士事務所", "address": "神奈川県横浜市港南区港南中央通９−１４ ライオンズマンション港南中央", "zip": "233-0004", "phone": "045-353-7860", "area": "横浜市港南区", "station": "港南中央駅", "lat": "35.3960", "lng": "139.5960", "accent": "#4a1942", "accent2": "#6b2fa0", "gradient": "linear-gradient(135deg, #4a1942 0%, #6b2fa0 100%)"},
    {"id": "L-199", "name": "税理士法人 鈴木会計事務所", "address": "神奈川県横浜市港南区上大岡西２丁目９−２０−４０２", "zip": "233-0002", "phone": "045-844-2371", "area": "横浜市港南区", "station": "上大岡駅", "lat": "35.3990", "lng": "139.5960", "accent": "#0d3b66", "accent2": "#1d6fa5", "gradient": "linear-gradient(135deg, #0d3b66 0%, #1d6fa5 100%)"},
    {"id": "L-200", "name": "税理士大嶋理惠事務所", "address": "神奈川県横浜市金沢区能見台通２２ 22-7-302（MHビル", "zip": "236-0053", "phone": "045-791-7525", "area": "横浜市金沢区", "station": "能見台駅", "lat": "35.3530", "lng": "139.6200", "accent": "#7b2d26", "accent2": "#c0392b", "gradient": "linear-gradient(135deg, #7b2d26 0%, #c0392b 100%)"},
    {"id": "L-203", "name": "田沢徳和税理士事務所", "address": "神奈川県横浜市港南区丸山台２丁目１−５ 第２丸照ビル", "zip": "233-0013", "phone": "045-841-4055", "area": "横浜市港南区", "station": "上永谷駅", "lat": "35.3870", "lng": "139.5760", "accent": "#1a3c34", "accent2": "#27ae60", "gradient": "linear-gradient(135deg, #1a3c34 0%, #27ae60 100%)"},
    {"id": "L-204", "name": "田村哲朗税理士事務所", "address": "神奈川県鎌倉市大船３丁目２−１１ 大船メディカルビル 3F", "zip": "247-0056", "phone": "0467-45-5680", "area": "鎌倉市大船", "station": "大船駅", "lat": "35.3530", "lng": "139.5340", "accent": "#2c3e50", "accent2": "#34495e", "gradient": "linear-gradient(135deg, #2c3e50 0%, #34495e 100%)"},
    {"id": "L-207", "name": "川崎清税理士事務所", "address": "神奈川県横浜市港南区上大岡西１丁目１５−１", "zip": "233-0002", "phone": "045-843-2775", "area": "横浜市港南区", "station": "上大岡駅", "lat": "35.4010", "lng": "139.5960", "accent": "#1a237e", "accent2": "#3949ab", "gradient": "linear-gradient(135deg, #1a237e 0%, #3949ab 100%)"},
    {"id": "L-210", "name": "巻幡直美税理士事務所", "address": "神奈川県横浜市南区中里１丁目１９−１２", "zip": "232-0063", "phone": "045-744-1793", "area": "横浜市南区", "station": "弘明寺駅", "lat": "35.4180", "lng": "139.6010", "accent": "#5b2c6f", "accent2": "#8e44ad", "gradient": "linear-gradient(135deg, #5b2c6f 0%, #8e44ad 100%)"},
    {"id": "L-211", "name": "吉田大税理士事務所", "address": "神奈川県横浜市磯子区杉田１丁目１３−１ 野村ビル ４Ｆ", "zip": "235-0033", "phone": "045-775-3914", "area": "横浜市磯子区", "station": "杉田駅", "lat": "35.3820", "lng": "139.6230", "accent": "#0e4d44", "accent2": "#16a085", "gradient": "linear-gradient(135deg, #0e4d44 0%, #16a085 100%)"},
    {"id": "L-212", "name": "山重会計事務所（税理士法人）", "address": "神奈川県横浜市戸塚区上倉田町１０００ ハイツ山重", "zip": "244-0816", "phone": "045-864-1666", "area": "横浜市戸塚区", "station": "戸塚駅", "lat": "35.3950", "lng": "139.5350", "accent": "#1b3a4b", "accent2": "#2e86c1", "gradient": "linear-gradient(135deg, #1b3a4b 0%, #2e86c1 100%)"},
    {"id": "L-213", "name": "宅井龍文税理士事務所", "address": "神奈川県横浜市金沢区能見台通１１−８ 松島荘", "zip": "236-0053", "phone": "045-788-9565", "area": "横浜市金沢区", "station": "能見台駅", "lat": "35.3540", "lng": "139.6190", "accent": "#4a235a", "accent2": "#7d3c98", "gradient": "linear-gradient(135deg, #4a235a 0%, #7d3c98 100%)"},
    {"id": "L-216", "name": "あおい税理士事務所", "address": "神奈川県横浜市金沢区谷津町３５５ 3F", "zip": "236-0016", "phone": "045-352-8768", "area": "横浜市金沢区", "station": "金沢文庫駅", "lat": "35.3400", "lng": "139.6180", "accent": "#0b5394", "accent2": "#3d85c6", "gradient": "linear-gradient(135deg, #0b5394 0%, #3d85c6 100%)"},
    {"id": "L-217", "name": "後藤税理士法人", "address": "神奈川県鎌倉市大船１丁目１２−１０ ３Ｆ", "zip": "247-0056", "phone": "0467-84-7607", "area": "鎌倉市大船", "station": "大船駅", "lat": "35.3510", "lng": "139.5340", "accent": "#1e3a2f", "accent2": "#1e8449", "gradient": "linear-gradient(135deg, #1e3a2f 0%, #1e8449 100%)"},
    {"id": "L-218", "name": "北堀税理士事務所", "address": "神奈川県横浜市港南区野庭町２４２−５８", "zip": "234-0056", "phone": "045-840-0800", "area": "横浜市港南区", "station": "上永谷駅", "lat": "35.3830", "lng": "139.5780", "accent": "#6c3461", "accent2": "#a93f8e", "gradient": "linear-gradient(135deg, #6c3461 0%, #a93f8e 100%)"},
    {"id": "L-219", "name": "税理士・社労士近藤洋志事務所", "address": "神奈川県横浜市金沢区富岡東５丁目１８−１ 長谷川メディカルプラザ富岡 207", "zip": "236-0051", "phone": "045-873-5469", "area": "横浜市金沢区", "station": "京急富岡駅", "lat": "35.3620", "lng": "139.6310", "accent": "#1a4731", "accent2": "#239b56", "gradient": "linear-gradient(135deg, #1a4731 0%, #239b56 100%)"},
    {"id": "L-222", "name": "市村税理士事務所", "address": "神奈川県横浜市港南区丸山台２丁目３９−３ 飯島ビル", "zip": "233-0013", "phone": "045-843-5589", "area": "横浜市港南区", "station": "上永谷駅", "lat": "35.3870", "lng": "139.5760", "accent": "#1c2833", "accent2": "#2c3e50", "gradient": "linear-gradient(135deg, #1c2833 0%, #566573 100%)"},
    {"id": "L-223", "name": "新春枝税理士事務所", "address": "神奈川県横浜市港南区大久保１丁目７", "zip": "233-0007", "phone": None, "area": "横浜市港南区", "station": "上大岡駅", "lat": "35.4020", "lng": "139.5940", "accent": "#7e2954", "accent2": "#c2185b", "gradient": "linear-gradient(135deg, #7e2954 0%, #c2185b 100%)"},
    {"id": "L-228", "name": "安田諭司税理士事務所", "address": "神奈川県横浜市港南区港南台３丁目３−１", "zip": "234-0054", "phone": "045-355-0005", "area": "横浜市港南区", "station": "港南台駅", "lat": "35.3750", "lng": "139.5800", "accent": "#1b4f72", "accent2": "#2e86c1", "gradient": "linear-gradient(135deg, #1b4f72 0%, #2e86c1 100%)"},
    {"id": "L-229", "name": "近藤会計事務所", "address": "神奈川県横浜市磯子区杉田４丁目５−１４ メゾン新杉田", "zip": "235-0033", "phone": "045-353-5753", "area": "横浜市磯子区", "station": "新杉田駅", "lat": "35.3810", "lng": "139.6200", "accent": "#2c3e50", "accent2": "#2980b9", "gradient": "linear-gradient(135deg, #2c3e50 0%, #2980b9 100%)"},
]

# Service items for tax accountant offices
SERVICES = [
    {"icon": "fa-file-invoice-dollar", "title": "税務申告", "desc": "法人税・所得税・消費税の申告書作成から提出まで、正確かつ迅速に対応いたします。"},
    {"icon": "fa-calculator", "title": "記帳代行", "desc": "日々の経理業務を代行し、正確な帳簿を作成。経営判断に役立つ財務データをご提供します。"},
    {"icon": "fa-building", "title": "会社設立支援", "desc": "法人設立の手続きから届出書の作成まで、スムーズな起業をトータルサポートいたします。"},
    {"icon": "fa-hand-holding-usd", "title": "資金調達支援", "desc": "融資申請・補助金申請のサポートから、事業計画書の作成まで資金面をバックアップします。"},
    {"icon": "fa-chart-line", "title": "経営コンサルティング", "desc": "月次決算を基にした経営分析で、利益改善と成長戦略を一緒に考えます。"},
    {"icon": "fa-users", "title": "相続・事業承継", "desc": "相続税対策から事業承継プランの策定まで、次世代への円滑な引き継ぎをサポートします。"},
]

def generate_html(lead):
    phone_display = lead["phone"] if lead["phone"] else "お問い合わせください"
    phone_href = f'tel:{lead["phone"]}' if lead["phone"] else "#contact"
    short_name = lead["name"].replace("税理士事務所", "").replace("税理士法人", "").replace("会計事務所", "").strip()
    if short_name.endswith("（）"):
        short_name = short_name.replace("（）", "")

    # Pick different hero images per lead using Unsplash
    hero_images = [
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1920&q=80",
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1920&q=80",
        "https://images.unsplash.com/photo-1497215842964-222b430dc094?w=1920&q=80",
        "https://images.unsplash.com/photo-1554469384-e58fac16e23a?w=1920&q=80",
        "https://images.unsplash.com/photo-1541746972996-4e0b0f43e02a?w=1920&q=80",
        "https://images.unsplash.com/photo-1560179707-f14e90ef3623?w=1920&q=80",
        "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=1920&q=80",
        "https://images.unsplash.com/photo-1568992687947-868a62a9f521?w=1920&q=80",
        "https://images.unsplash.com/photo-1604328698692-f76ea9498e76?w=1920&q=80",
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=1920&q=80",
    ]
    hero_idx = hash(lead["id"]) % len(hero_images)
    hero_img = hero_images[hero_idx]

    about_images = [
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=800&q=80",
        "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=800&q=80",
        "https://images.unsplash.com/photo-1553028826-f4804a6dba3b?w=800&q=80",
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&q=80",
        "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&q=80",
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&q=80",
        "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800&q=80",
    ]
    about_idx = hash(lead["id"] + "about") % len(about_images)
    about_img = about_images[about_idx]

    services_html = ""
    for i, svc in enumerate(SERVICES):
        delay = i * 100
        services_html += f'''
            <div class="service-card" data-aos="fade-up" data-aos-delay="{delay}">
              <div class="service-icon"><i class="fas {svc['icon']}"></i></div>
              <h3>{svc['title']}</h3>
              <p>{svc['desc']}</p>
            </div>'''

    # Strengths section
    strengths = [
        {"num": "01", "title": "地域密着の安心感", "desc": f"{lead['area']}を中心に、地域の皆様に寄り添ったサービスを提供。お気軽にご相談いただける身近な存在を目指しています。"},
        {"num": "02", "title": "丁寧なヒアリング", "desc": "お客様一人ひとりの状況を丁寧にお聞きし、最適なソリューションをご提案。初回相談は無料です。"},
        {"num": "03", "title": "迅速・正確な対応", "desc": "期限厳守はもちろん、日々変わる税制にも迅速に対応。お客様の大切な経営判断をサポートします。"},
    ]
    strengths_html = ""
    for i, s in enumerate(strengths):
        delay = i * 150
        strengths_html += f'''
            <div class="strength-item" data-aos="fade-right" data-aos-delay="{delay}">
              <div class="strength-num">{s['num']}</div>
              <div class="strength-content">
                <h3>{s['title']}</h3>
                <p>{s['desc']}</p>
              </div>
            </div>'''

    # FAQ
    faqs = [
        {"q": "初回相談は無料ですか？", "a": "はい、初回のご相談は無料で承っております。お気軽にお問い合わせください。"},
        {"q": "対応エリアはどこですか？", "a": f"{lead['area']}を中心に、横浜市全域および周辺地域のお客様に対応しております。オンラインでのご相談も可能です。"},
        {"q": "個人の確定申告も対応していますか？", "a": "はい、個人の確定申告から法人の決算申告まで幅広く対応しております。副業や不動産所得のご相談もお任せください。"},
        {"q": "料金体系を教えてください。", "a": "お客様の事業規模やご依頼内容に応じて、明確な料金をご提示いたします。まずはお気軽にお見積もりをご依頼ください。"},
    ]
    faq_html = ""
    for i, f in enumerate(faqs):
        faq_html += f'''
            <div class="faq-item" data-aos="fade-up" data-aos-delay="{i * 100}">
              <div class="faq-question" onclick="toggleFaq(this)">
                <span>{f['q']}</span>
                <i class="fas fa-chevron-down"></i>
              </div>
              <div class="faq-answer">
                <p>{f['a']}</p>
              </div>
            </div>'''

    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{lead['name']} | {lead['area']}の税理士</title>
  <meta name="description" content="{lead['area']}の{lead['name']}。税務申告・記帳代行・会社設立・相続対策など、経験豊富な税理士が丁寧にサポートいたします。">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <style>
    :root {{
      --primary: {lead['accent']};
      --primary-light: {lead['accent2']};
      --gradient: {lead['gradient']};
      --text: #1a1a2e;
      --text-light: #555;
      --text-muted: #888;
      --bg: #ffffff;
      --bg-alt: #f8f9fa;
      --bg-dark: #0f1923;
      --border: #e8e8e8;
      --shadow: 0 4px 20px rgba(0,0,0,0.08);
      --shadow-lg: 0 10px 40px rgba(0,0,0,0.12);
      --radius: 12px;
      --radius-lg: 20px;
      --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      --font-sans: 'Noto Sans JP', sans-serif;
      --font-serif: 'Noto Serif JP', serif;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{
      font-family: var(--font-sans);
      color: var(--text);
      line-height: 1.8;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    /* ===== Utility ===== */
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
    .section {{ padding: 100px 0; }}
    .section-header {{ text-align: center; margin-bottom: 60px; }}
    .section-header .label {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--primary-light);
      margin-bottom: 12px;
    }}
    .section-header h2 {{
      font-family: var(--font-serif);
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 700;
      color: var(--text);
      margin-bottom: 16px;
    }}
    .section-header p {{
      color: var(--text-light);
      font-size: 1rem;
      max-width: 600px;
      margin: 0 auto;
    }}
    .section-header .divider {{
      width: 60px;
      height: 3px;
      background: var(--gradient);
      margin: 20px auto 0;
      border-radius: 2px;
    }}

    /* ===== Loading Screen ===== */
    .loader {{
      position: fixed;
      inset: 0;
      background: var(--bg);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
      transition: opacity 0.6s ease, visibility 0.6s ease;
    }}
    .loader.hidden {{ opacity: 0; visibility: hidden; pointer-events: none; }}
    .loader-spinner {{
      width: 48px; height: 48px;
      border: 3px solid var(--border);
      border-top-color: var(--primary);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}

    /* ===== Navigation ===== */
    .navbar {{
      position: fixed; top: 0; left: 0; right: 0;
      z-index: 1000;
      padding: 20px 0;
      transition: var(--transition);
    }}
    .navbar.scrolled {{
      background: rgba(255,255,255,0.97);
      backdrop-filter: blur(20px);
      padding: 12px 0;
      box-shadow: 0 2px 20px rgba(0,0,0,0.08);
    }}
    .navbar .container {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .nav-logo {{
      font-family: var(--font-serif);
      font-size: 1.1rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      transition: var(--transition);
    }}
    .navbar.scrolled .nav-logo {{ color: var(--primary); }}
    .nav-links {{
      display: flex;
      list-style: none;
      gap: 32px;
      align-items: center;
    }}
    .nav-links a {{
      color: rgba(255,255,255,0.9);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 500;
      transition: var(--transition);
      position: relative;
    }}
    .nav-links a::after {{
      content: '';
      position: absolute;
      bottom: -4px; left: 0;
      width: 0; height: 2px;
      background: var(--primary-light);
      transition: width 0.3s ease;
    }}
    .nav-links a:hover::after {{ width: 100%; }}
    .navbar.scrolled .nav-links a {{ color: var(--text); }}
    .navbar.scrolled .nav-links a:hover {{ color: var(--primary); }}
    .nav-cta {{
      background: var(--gradient) !important;
      color: #fff !important;
      padding: 10px 24px !important;
      border-radius: 50px !important;
      font-weight: 600 !important;
      transition: var(--transition) !important;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    .nav-cta:hover {{ transform: translateY(-2px); box-shadow: 0 6px 25px rgba(0,0,0,0.3); }}
    .nav-cta::after {{ display: none !important; }}
    .hamburger {{
      display: none;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
      z-index: 1001;
    }}
    .hamburger span {{
      width: 28px; height: 2px;
      background: #fff;
      transition: var(--transition);
    }}
    .navbar.scrolled .hamburger span {{ background: var(--text); }}

    /* ===== Hero ===== */
    .hero {{
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}
    .hero-bg {{
      position: absolute;
      inset: 0;
      background: url('{hero_img}') center/cover no-repeat;
    }}
    .hero-bg::after {{
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(135deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 50%, rgba(0,0,0,0.6) 100%);
    }}
    .hero-content {{
      position: relative;
      z-index: 2;
      text-align: center;
      padding: 0 32px;
      max-width: 900px;
    }}
    .hero-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255,255,255,0.2);
      padding: 8px 20px;
      border-radius: 50px;
      color: #fff;
      font-size: 0.85rem;
      font-weight: 500;
      margin-bottom: 24px;
      animation: fadeInDown 0.8s ease 0.2s both;
    }}
    .hero h1 {{
      font-family: var(--font-serif);
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 900;
      color: #fff;
      line-height: 1.3;
      margin-bottom: 20px;
      animation: fadeInUp 0.8s ease 0.4s both;
    }}
    .hero h1 .highlight {{
      background: var(--gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}
    .hero-subtitle {{
      font-size: clamp(0.95rem, 2vw, 1.15rem);
      color: rgba(255,255,255,0.85);
      margin-bottom: 40px;
      line-height: 1.8;
      animation: fadeInUp 0.8s ease 0.6s both;
    }}
    .hero-buttons {{
      display: flex;
      gap: 16px;
      justify-content: center;
      flex-wrap: wrap;
      animation: fadeInUp 0.8s ease 0.8s both;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 16px 36px;
      border-radius: 50px;
      font-size: 1rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      cursor: pointer;
      border: none;
    }}
    .btn-primary {{
      background: var(--gradient);
      color: #fff;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}
    .btn-primary:hover {{ transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.4); }}
    .btn-outline {{
      background: transparent;
      color: #fff;
      border: 2px solid rgba(255,255,255,0.5);
    }}
    .btn-outline:hover {{ background: rgba(255,255,255,0.15); border-color: #fff; transform: translateY(-3px); }}
    .hero-scroll {{
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 2;
      animation: bounce 2s infinite;
    }}
    .hero-scroll a {{
      color: rgba(255,255,255,0.7);
      font-size: 1.5rem;
      transition: var(--transition);
    }}
    .hero-scroll a:hover {{ color: #fff; }}

    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(30px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes fadeInDown {{
      from {{ opacity: 0; transform: translateY(-20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes bounce {{
      0%, 20%, 50%, 80%, 100% {{ transform: translateX(-50%) translateY(0); }}
      40% {{ transform: translateX(-50%) translateY(-12px); }}
      60% {{ transform: translateX(-50%) translateY(-6px); }}
    }}

    /* ===== Features Bar ===== */
    .features-bar {{
      background: var(--bg);
      padding: 0;
      margin-top: -60px;
      position: relative;
      z-index: 10;
    }}
    .features-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      background: var(--bg);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      overflow: hidden;
    }}
    .feature-item {{
      padding: 40px 30px;
      text-align: center;
      border-right: 1px solid var(--border);
      transition: var(--transition);
    }}
    .feature-item:last-child {{ border-right: none; }}
    .feature-item:hover {{ background: var(--bg-alt); }}
    .feature-item .icon {{
      width: 56px; height: 56px;
      background: var(--gradient);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 16px;
      color: #fff;
      font-size: 1.3rem;
    }}
    .feature-item h4 {{ font-size: 1rem; font-weight: 700; margin-bottom: 8px; }}
    .feature-item p {{ font-size: 0.85rem; color: var(--text-light); }}

    /* ===== About ===== */
    .about {{ background: var(--bg-alt); }}
    .about-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }}
    .about-image {{
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }}
    .about-image img {{
      width: 100%;
      height: 400px;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }}
    .about-image:hover img {{ transform: scale(1.05); }}
    .about-image .overlay {{
      position: absolute;
      bottom: 0; left: 0; right: 0;
      padding: 24px;
      background: linear-gradient(transparent, rgba(0,0,0,0.7));
      color: #fff;
    }}
    .about-image .overlay span {{
      font-size: 0.8rem;
      opacity: 0.8;
    }}
    .about-text h3 {{
      font-family: var(--font-serif);
      font-size: 1.6rem;
      margin-bottom: 20px;
      color: var(--text);
    }}
    .about-text p {{
      color: var(--text-light);
      margin-bottom: 16px;
      font-size: 0.95rem;
    }}
    .about-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 30px;
    }}
    .stat {{
      text-align: center;
      padding: 20px;
      background: var(--bg);
      border-radius: var(--radius);
      box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }}
    .stat-num {{
      font-size: 2rem;
      font-weight: 900;
      color: var(--primary);
      font-family: var(--font-serif);
    }}
    .stat-label {{ font-size: 0.8rem; color: var(--text-muted); margin-top: 4px; }}

    /* ===== Services ===== */
    .services-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
    }}
    .service-card {{
      background: var(--bg);
      padding: 40px 30px;
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow);
      transition: var(--transition);
      position: relative;
      overflow: hidden;
    }}
    .service-card::before {{
      content: '';
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 4px;
      background: var(--gradient);
      transform: scaleX(0);
      transform-origin: left;
      transition: transform 0.4s ease;
    }}
    .service-card:hover {{ transform: translateY(-8px); box-shadow: var(--shadow-lg); }}
    .service-card:hover::before {{ transform: scaleX(1); }}
    .service-icon {{
      width: 64px; height: 64px;
      background: var(--gradient);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      color: #fff;
      font-size: 1.5rem;
      transition: var(--transition);
    }}
    .service-card:hover .service-icon {{ transform: scale(1.1) rotate(-5deg); }}
    .service-card h3 {{ font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; }}
    .service-card p {{ font-size: 0.9rem; color: var(--text-light); line-height: 1.7; }}

    /* ===== Strengths ===== */
    .strengths {{ background: var(--bg-alt); }}
    .strength-item {{
      display: flex;
      gap: 30px;
      align-items: flex-start;
      padding: 36px;
      background: var(--bg);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow);
      margin-bottom: 20px;
      transition: var(--transition);
    }}
    .strength-item:hover {{ transform: translateX(8px); box-shadow: var(--shadow-lg); }}
    .strength-num {{
      font-size: 2.5rem;
      font-weight: 900;
      color: var(--primary-light);
      opacity: 0.3;
      font-family: var(--font-serif);
      line-height: 1;
      min-width: 60px;
    }}
    .strength-content h3 {{ font-size: 1.15rem; font-weight: 700; margin-bottom: 8px; }}
    .strength-content p {{ font-size: 0.9rem; color: var(--text-light); }}

    /* ===== CTA Banner ===== */
    .cta-banner {{
      background: var(--gradient);
      padding: 80px 0;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
    .cta-banner::before {{
      content: '';
      position: absolute;
      top: -50%; right: -20%;
      width: 500px; height: 500px;
      background: rgba(255,255,255,0.05);
      border-radius: 50%;
    }}
    .cta-banner::after {{
      content: '';
      position: absolute;
      bottom: -40%; left: -10%;
      width: 400px; height: 400px;
      background: rgba(255,255,255,0.05);
      border-radius: 50%;
    }}
    .cta-banner h2 {{
      font-family: var(--font-serif);
      font-size: clamp(1.6rem, 3vw, 2.2rem);
      color: #fff;
      margin-bottom: 16px;
      position: relative;
      z-index: 1;
    }}
    .cta-banner p {{
      color: rgba(255,255,255,0.85);
      margin-bottom: 30px;
      font-size: 1rem;
      position: relative;
      z-index: 1;
    }}
    .cta-banner .btn {{
      background: #fff;
      color: var(--primary);
      font-weight: 700;
      position: relative;
      z-index: 1;
    }}
    .cta-banner .btn:hover {{ transform: translateY(-3px); box-shadow: 0 8px 30px rgba(0,0,0,0.2); }}

    /* ===== FAQ ===== */
    .faq-item {{
      background: var(--bg);
      border-radius: var(--radius);
      margin-bottom: 12px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.05);
      overflow: hidden;
      transition: var(--transition);
    }}
    .faq-item:hover {{ box-shadow: var(--shadow); }}
    .faq-question {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 24px;
      cursor: pointer;
      font-weight: 600;
      transition: var(--transition);
    }}
    .faq-question:hover {{ color: var(--primary); }}
    .faq-question i {{ transition: transform 0.3s ease; color: var(--primary-light); }}
    .faq-question.active i {{ transform: rotate(180deg); }}
    .faq-answer {{
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease, padding 0.4s ease;
    }}
    .faq-answer.open {{ max-height: 200px; }}
    .faq-answer p {{ padding: 0 24px 20px; color: var(--text-light); font-size: 0.95rem; }}

    /* ===== Contact ===== */
    .contact {{ background: var(--bg-alt); }}
    .contact-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
    }}
    .contact-info-card {{
      background: var(--bg);
      padding: 40px;
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow);
    }}
    .contact-info-card h3 {{
      font-family: var(--font-serif);
      font-size: 1.4rem;
      margin-bottom: 24px;
    }}
    .info-item {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 24px;
    }}
    .info-item .icon-box {{
      width: 48px; height: 48px;
      background: var(--gradient);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      flex-shrink: 0;
    }}
    .info-item h4 {{ font-size: 0.85rem; color: var(--text-muted); margin-bottom: 4px; }}
    .info-item p {{ font-size: 0.95rem; font-weight: 500; }}
    .info-item a {{ color: var(--primary); text-decoration: none; }}
    .info-item a:hover {{ text-decoration: underline; }}
    .map-wrapper {{
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow);
      height: 100%;
      min-height: 400px;
    }}
    .map-wrapper iframe {{ width: 100%; height: 100%; border: none; min-height: 400px; }}

    /* ===== Footer ===== */
    .footer {{
      background: var(--bg-dark);
      color: rgba(255,255,255,0.7);
      padding: 60px 0 0;
    }}
    .footer-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 40px;
      padding-bottom: 40px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .footer-brand h3 {{
      font-family: var(--font-serif);
      color: #fff;
      font-size: 1.2rem;
      margin-bottom: 16px;
    }}
    .footer-brand p {{ font-size: 0.85rem; line-height: 1.8; }}
    .footer h4 {{
      color: #fff;
      font-size: 0.95rem;
      margin-bottom: 20px;
    }}
    .footer-links {{ list-style: none; }}
    .footer-links li {{ margin-bottom: 12px; }}
    .footer-links a {{
      color: rgba(255,255,255,0.6);
      text-decoration: none;
      font-size: 0.9rem;
      transition: var(--transition);
    }}
    .footer-links a:hover {{ color: #fff; padding-left: 4px; }}
    .footer-bottom {{
      padding: 24px 0;
      text-align: center;
      font-size: 0.8rem;
      color: rgba(255,255,255,0.4);
    }}

    /* ===== Back to Top ===== */
    .back-to-top {{
      position: fixed;
      bottom: 30px; right: 30px;
      width: 50px; height: 50px;
      background: var(--gradient);
      color: #fff;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.2rem;
      box-shadow: var(--shadow);
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
      z-index: 999;
    }}
    .back-to-top.visible {{ opacity: 1; visibility: visible; }}
    .back-to-top:hover {{ transform: translateY(-4px); box-shadow: var(--shadow-lg); }}

    /* ===== Animations (AOS-like) ===== */
    [data-aos] {{
      opacity: 0;
      transition: opacity 0.6s ease, transform 0.6s ease;
    }}
    [data-aos="fade-up"] {{ transform: translateY(40px); }}
    [data-aos="fade-right"] {{ transform: translateX(-40px); }}
    [data-aos="fade-left"] {{ transform: translateX(40px); }}
    [data-aos="zoom-in"] {{ transform: scale(0.9); }}
    [data-aos].aos-animate {{
      opacity: 1;
      transform: translateY(0) translateX(0) scale(1);
    }}

    /* ===== Mobile ===== */
    .mobile-menu {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.95);
      backdrop-filter: blur(20px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 24px;
      z-index: 999;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
    }}
    .mobile-menu.open {{ opacity: 1; visibility: visible; }}
    .mobile-menu a {{
      color: #fff;
      text-decoration: none;
      font-size: 1.3rem;
      font-weight: 500;
      padding: 12px;
      transition: var(--transition);
    }}
    .mobile-menu a:hover {{ color: var(--primary-light); }}
    .mobile-close {{
      position: absolute;
      top: 24px; right: 24px;
      background: none;
      border: none;
      color: #fff;
      font-size: 2rem;
      cursor: pointer;
    }}

    @media (max-width: 1024px) {{
      .services-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .about-grid {{ grid-template-columns: 1fr; }}
      .contact-grid {{ grid-template-columns: 1fr; }}
      .footer-grid {{ grid-template-columns: 1fr; }}
    }}

    @media (max-width: 768px) {{
      .section {{ padding: 70px 0; }}
      .nav-links {{ display: none; }}
      .hamburger {{ display: flex; }}
      .features-grid {{
        grid-template-columns: 1fr;
        margin: 0 16px;
      }}
      .feature-item {{ border-right: none; border-bottom: 1px solid var(--border); }}
      .feature-item:last-child {{ border-bottom: none; }}
      .services-grid {{ grid-template-columns: 1fr; }}
      .hero-content {{ padding: 0 24px; }}
      .hero h1 {{ font-size: clamp(1.7rem, 6vw, 2.5rem); }}
      .hero-buttons {{ flex-direction: column; align-items: center; }}
      .btn {{ width: 100%; max-width: 300px; justify-content: center; }}
      .strength-item {{ flex-direction: column; gap: 16px; }}
      .about-stats {{ grid-template-columns: 1fr; }}
      .features-bar {{ margin-top: -40px; }}
    }}
  </style>
</head>
<body>

  <!-- Loading Screen -->
  <div class="loader" id="loader">
    <div class="loader-spinner"></div>
  </div>

  <!-- Navigation -->
  <nav class="navbar" id="navbar">
    <div class="container">
      <a href="#" class="nav-logo">{lead['name']}</a>
      <ul class="nav-links">
        <li><a href="#about">事務所紹介</a></li>
        <li><a href="#services">サービス</a></li>
        <li><a href="#strengths">選ばれる理由</a></li>
        <li><a href="#faq">よくある質問</a></li>
        <li><a href="#contact" class="nav-cta">無料相談</a></li>
      </ul>
      <div class="hamburger" id="hamburger" onclick="toggleMenu()">
        <span></span><span></span><span></span>
      </div>
    </div>
  </nav>

  <!-- Mobile Menu -->
  <div class="mobile-menu" id="mobileMenu">
    <button class="mobile-close" onclick="toggleMenu()">&times;</button>
    <a href="#about" onclick="toggleMenu()">事務所紹介</a>
    <a href="#services" onclick="toggleMenu()">サービス</a>
    <a href="#strengths" onclick="toggleMenu()">選ばれる理由</a>
    <a href="#faq" onclick="toggleMenu()">よくある質問</a>
    <a href="#contact" onclick="toggleMenu()">無料相談</a>
  </div>

  <!-- Hero -->
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="hero-badge"><i class="fas fa-shield-alt"></i>&nbsp; {lead['area']}の信頼できる税理士</div>
      <h1>{lead['area']}で<br class="sp-only">頼れる税務パートナー<br><span class="highlight">{lead['name']}</span></h1>
      <p class="hero-subtitle">
        税務申告・記帳代行・会社設立・相続対策まで<br>
        経験豊富な税理士がお客様の経営を全力でサポートいたします
      </p>
      <div class="hero-buttons">
        <a href="#contact" class="btn btn-primary"><i class="fas fa-envelope"></i> 無料相談はこちら</a>
        <a href="{phone_href}" class="btn btn-outline"><i class="fas fa-phone"></i> {phone_display}</a>
      </div>
    </div>
    <div class="hero-scroll"><a href="#features"><i class="fas fa-chevron-down"></i></a></div>
  </section>

  <!-- Features Bar -->
  <section class="features-bar" id="features">
    <div class="container">
      <div class="features-grid">
        <div class="feature-item" data-aos="zoom-in">
          <div class="icon"><i class="fas fa-comments"></i></div>
          <h4>初回相談無料</h4>
          <p>まずはお気軽にご相談ください</p>
        </div>
        <div class="feature-item" data-aos="zoom-in" data-aos-delay="100">
          <div class="icon"><i class="fas fa-map-marker-alt"></i></div>
          <h4>{lead['station']}からアクセス良好</h4>
          <p>地域密着で安心のサポート</p>
        </div>
        <div class="feature-item" data-aos="zoom-in" data-aos-delay="200">
          <div class="icon"><i class="fas fa-clock"></i></div>
          <h4>迅速な対応</h4>
          <p>お問い合わせから24時間以内に返信</p>
        </div>
      </div>
    </div>
  </section>

  <!-- About -->
  <section class="about section" id="about">
    <div class="container">
      <div class="about-grid">
        <div class="about-image" data-aos="fade-right">
          <img src="{about_img}" alt="{lead['name']}のオフィス">
          <div class="overlay">
            <span><i class="fas fa-map-marker-alt"></i> {lead['area']}</span>
          </div>
        </div>
        <div class="about-text" data-aos="fade-left">
          <div class="section-header" style="text-align:left; margin-bottom:24px;">
            <span class="label">About Us</span>
            <h2>事務所紹介</h2>
          </div>
          <h3>お客様の「困った」に<br>寄り添う税務パートナー</h3>
          <p>{lead['name']}は、{lead['area']}を拠点に、個人事業主から中小企業まで幅広いお客様の税務・会計をサポートしております。</p>
          <p>「わかりやすい説明」と「丁寧な対応」をモットーに、お客様の経営課題に真摯に向き合い、最適なソリューションをご提案いたします。</p>
          <div class="about-stats">
            <div class="stat">
              <div class="stat-num">20<span style="font-size:1rem">年+</span></div>
              <div class="stat-label">実務経験</div>
            </div>
            <div class="stat">
              <div class="stat-num">500<span style="font-size:1rem">件+</span></div>
              <div class="stat-label">年間相談実績</div>
            </div>
            <div class="stat">
              <div class="stat-num">98<span style="font-size:1rem">%</span></div>
              <div class="stat-label">顧客満足度</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Services -->
  <section class="section" id="services">
    <div class="container">
      <div class="section-header" data-aos="fade-up">
        <span class="label">Services</span>
        <h2>サービス内容</h2>
        <p>お客様のあらゆるニーズに応える幅広いサービスをご用意しております</p>
        <div class="divider"></div>
      </div>
      <div class="services-grid">{services_html}
      </div>
    </div>
  </section>

  <!-- Strengths -->
  <section class="strengths section" id="strengths">
    <div class="container">
      <div class="section-header" data-aos="fade-up">
        <span class="label">Why Choose Us</span>
        <h2>選ばれる理由</h2>
        <p>{lead['name']}が多くのお客様に選ばれ続ける理由をご紹介します</p>
        <div class="divider"></div>
      </div>
      <div class="strengths-list">{strengths_html}
      </div>
    </div>
  </section>

  <!-- CTA Banner -->
  <section class="cta-banner">
    <div class="container">
      <h2 data-aos="fade-up">まずはお気軽にご相談ください</h2>
      <p data-aos="fade-up" data-aos-delay="100">初回相談は無料です。税務のことでお悩みなら、私たちにお任せください。</p>
      <a href="#contact" class="btn" data-aos="fade-up" data-aos-delay="200"><i class="fas fa-arrow-right"></i> 無料相談のお申し込み</a>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" id="faq">
    <div class="container">
      <div class="section-header" data-aos="fade-up">
        <span class="label">FAQ</span>
        <h2>よくある質問</h2>
        <p>お客様からよくいただくご質問にお答えします</p>
        <div class="divider"></div>
      </div>
      <div style="max-width: 800px; margin: 0 auto;">{faq_html}
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section class="contact section" id="contact">
    <div class="container">
      <div class="section-header" data-aos="fade-up">
        <span class="label">Contact</span>
        <h2>お問い合わせ</h2>
        <p>ご相談・ご質問はお気軽にお問い合わせください</p>
        <div class="divider"></div>
      </div>
      <div class="contact-grid">
        <div class="contact-info-card" data-aos="fade-right">
          <h3>アクセス・連絡先</h3>
          <div class="info-item">
            <div class="icon-box"><i class="fas fa-building"></i></div>
            <div>
              <h4>事務所名</h4>
              <p>{lead['name']}</p>
            </div>
          </div>
          <div class="info-item">
            <div class="icon-box"><i class="fas fa-map-marker-alt"></i></div>
            <div>
              <h4>所在地</h4>
              <p>〒{lead['zip']} {lead['address']}</p>
            </div>
          </div>
          <div class="info-item">
            <div class="icon-box"><i class="fas fa-phone"></i></div>
            <div>
              <h4>電話番号</h4>
              <p><a href="{phone_href}">{phone_display}</a></p>
            </div>
          </div>
          <div class="info-item">
            <div class="icon-box"><i class="fas fa-train"></i></div>
            <div>
              <h4>最寄駅</h4>
              <p>{lead['station']}</p>
            </div>
          </div>
          <div class="info-item">
            <div class="icon-box"><i class="fas fa-clock"></i></div>
            <div>
              <h4>営業時間</h4>
              <p>平日 9:00〜18:00（土日祝休み）</p>
            </div>
          </div>
        </div>
        <div class="map-wrapper" data-aos="fade-left">
          <iframe
            src="https://www.google.com/maps?q={lead['lat']},{lead['lng']}&z=16&output=embed"
            allowfullscreen
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3>{lead['name']}</h3>
          <p>〒{lead['zip']} {lead['address']}<br>
          TEL: {phone_display}</p>
        </div>
        <div>
          <h4>サービス</h4>
          <ul class="footer-links">
            <li><a href="#services">税務申告</a></li>
            <li><a href="#services">記帳代行</a></li>
            <li><a href="#services">会社設立支援</a></li>
            <li><a href="#services">相続・事業承継</a></li>
          </ul>
        </div>
        <div>
          <h4>ご案内</h4>
          <ul class="footer-links">
            <li><a href="#about">事務所紹介</a></li>
            <li><a href="#faq">よくある質問</a></li>
            <li><a href="#contact">アクセス</a></li>
            <li><a href="#contact">お問い合わせ</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2024 {lead['name']}. All rights reserved.
      </div>
    </div>
  </footer>

  <!-- Back to Top -->
  <button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">
    <i class="fas fa-arrow-up"></i>
  </button>

  <script>
    // Loader
    window.addEventListener('load', function() {{
      setTimeout(function() {{
        document.getElementById('loader').classList.add('hidden');
      }}, 600);
    }});

    // Navbar scroll effect
    var navbar = document.getElementById('navbar');
    var backToTop = document.getElementById('backToTop');
    window.addEventListener('scroll', function() {{
      if (window.scrollY > 80) {{
        navbar.classList.add('scrolled');
        backToTop.classList.add('visible');
      }} else {{
        navbar.classList.remove('scrolled');
        backToTop.classList.remove('visible');
      }}
    }});

    // Mobile menu
    function toggleMenu() {{
      document.getElementById('mobileMenu').classList.toggle('open');
    }}

    // FAQ toggle
    function toggleFaq(el) {{
      var isActive = el.classList.contains('active');
      // Close all
      document.querySelectorAll('.faq-question').forEach(function(q) {{
        q.classList.remove('active');
        q.nextElementSibling.classList.remove('open');
      }});
      if (!isActive) {{
        el.classList.add('active');
        el.nextElementSibling.classList.add('open');
      }}
    }}

    // Scroll animations (AOS-like)
    function initAOS() {{
      var elements = document.querySelectorAll('[data-aos]');
      var observer = new IntersectionObserver(function(entries) {{
        entries.forEach(function(entry) {{
          if (entry.isIntersecting) {{
            var delay = parseInt(entry.target.getAttribute('data-aos-delay') || 0);
            setTimeout(function() {{
              entry.target.classList.add('aos-animate');
            }}, delay);
          }}
        }});
      }}, {{ threshold: 0.1, rootMargin: '0px 0px -50px 0px' }});

      elements.forEach(function(el) {{
        observer.observe(el);
      }});
    }}

    document.addEventListener('DOMContentLoaded', initAOS);

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {{
      anchor.addEventListener('click', function(e) {{
        e.preventDefault();
        var target = document.querySelector(this.getAttribute('href'));
        if (target) {{
          target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}
      }});
    }});

    // Counter animation for stats
    function animateCounters() {{
      var counters = document.querySelectorAll('.stat-num');
      var observer = new IntersectionObserver(function(entries) {{
        entries.forEach(function(entry) {{
          if (entry.isIntersecting && !entry.target.classList.contains('counted')) {{
            entry.target.classList.add('counted');
            var text = entry.target.textContent;
            var match = text.match(/(\\d+)/);
            if (match) {{
              var target = parseInt(match[1]);
              var suffix = text.replace(match[1], '');
              var current = 0;
              var step = Math.ceil(target / 40);
              var timer = setInterval(function() {{
                current += step;
                if (current >= target) {{
                  current = target;
                  clearInterval(timer);
                }}
                entry.target.innerHTML = current + suffix;
              }}, 30);
            }}
          }}
        }});
      }}, {{ threshold: 0.5 }});
      counters.forEach(function(c) {{ observer.observe(c); }});
    }}

    document.addEventListener('DOMContentLoaded', animateCounters);
  </script>
</body>
</html>'''
    return html


def main():
    base_dir = "/Users/Shared/projects/hp-demo"
    for lead in LEADS:
        lead_dir = os.path.join(base_dir, lead["id"])
        os.makedirs(lead_dir, exist_ok=True)
        html = generate_html(lead)
        filepath = os.path.join(lead_dir, "index.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {lead['id']}: {lead['name']} -> {filepath}")

    print(f"\nDone! Generated {len(LEADS)} demo sites.")


if __name__ == "__main__":
    main()
