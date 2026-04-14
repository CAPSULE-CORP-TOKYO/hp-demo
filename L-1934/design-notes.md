# 分析結果 — L-1934 澤村正夫税理士事務所

## アーキタイプ
名前: **A: モダンミニマル**
根拠: 業種は税理士（士業・コンサル）。客層は地域中小企業オーナー（保守的・信頼性重視）。所長挨拶と理念ページに知的・哲学的トーン（自利利他、般若心経の引用）があり、伝統重厚（B）も検討余地ありだが、現代のリニューアル提案として「読みやすく整理された情報設計」が訴求の中心になるため A: モダンミニマル を主軸に、見出しに Noto Serif JP を併用してわずかに重厚さを足す折衷型。

## カラーパレット
- メイン: `#2C3E5C`（ネイビー／元サイトの紺系を継承）
- サブ: `#F4F6FA`（オフホワイト・ライトグレー）
- アクセント: `#D97A1A`（オレンジ／元サイトのサイドバー強調色「TKC全国会員」帯のオレンジを継承）
- テキスト: `#1A1F2C`（ダークネイビー）
- ボーダー/罫線: `#E2E6EE`

## 画像分類

| # | URL（短縮） | 出自 | 適性 | 処理 | 備考 |
|---|---|---|---|---|---|
| 1 | btn-sp-menu.png | template | icon | CSS/SVG 代替 | TKC共通ハンバーガー |
| 2 | 201603281432_GCAWs.jpg | template | text-embedded | 差替 | ヒーロー（キャッチコピー焼込）→ Unsplash 差替、テキストはHTMLへ |
| 3 | 570cb7ff..b0.gif | template | text-embedded | 差替 | サイドバー販促バナー |
| 4 | 570cb802..b2.jpg | template | text-embedded | 差替 | 経営革新等支援機関バナー |
| 5 | tkc_logo1.gif | template | text-embedded | CSS/SVG 代替 | TKCロゴ（テキストで代替） |
| 6-11 | bnr-*.png | template | text-embedded | 不要 | 固定追従バナー、新サイトでは不要 |
| 12 | facebook .png | tracking | icon | 不要 | FB トラッキング |
| **13** | **5eaa1d6b..be9.jpg** | **original** | **photo** | **そのまま引き継ぎ** | **事務所外観の固有写真（最重要）** |
| 14 | 570cb805..b4.jpg | original | photo | 差替 | 320x240 ピンボケ・低解像度の謎写真 |
| 15 | 570cb806..b5.jpg | template | photo | 差替 | コーヒーカップのストック画像 |
| 16 | 570cb807..b6.png | original | text-embedded | そのまま引き継ぎ | 「自利利他」書道作品（理念の象徴、原文と非重複の装飾） |
| 17 | 570cb809..b7.png | template | text-embedded | 差替 | TKC全国研修会の集合写真 |
| 18-19 | 570cb80a/d..b8/ba.jpg | template | text-embedded | 差替 | TKCセミナー報告チラシ画像 |
| 20-129 | TKC リンク先ページ各種 | template | various | 不要 | サブページ（リンク集・QA・カレンダー等）の TKC テンプレ画像。今回のリデザインは「事務所固有情報」の再編成に集中するため引き継がない |

### 引き継ぐ画像（最終）
1. `5eaa1d6bf29e8a526fb84be9.jpg` → `images/office-exterior.jpg`（事務所外観、Hero/About で使用）
2. `570cb80768ba6d26220011b6.png` → `images/jiri-rita.png`（自利利他の書、理念セクションで使用）

その他はすべて差替または不要。

## 注意事項（builder v6 / DEC-026 関連）
- ベースサイト URL は `https://www.tkcnf.com/sawamurakaikei` で、TKC NF プラットフォーム上の「澤村正夫税理士事務所」固有ページ。**別会社サイトではない**（事務所概要・所長挨拶・所長経歴に「澤村正夫」「024-961-3200」「土瓜１－１９５－２」が leads.json と完全一致）。停止対象ではない。
- 元サイトは TKC 共通テンプレートで装飾画像が全て TKC 提供素材。固有画像は事務所外観 1 枚のみ。
- ヒーローのキャッチコピーは焼込画像（#2）にのみ存在するが、これはサイトの主要メッセージのため **HTML テキストとして再現**（焼込から OCR 的に転記、原文一字一句保持）。画像自体は Unsplash の office/business 系に差替。
