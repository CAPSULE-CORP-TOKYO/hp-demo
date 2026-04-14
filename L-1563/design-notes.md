# 分析結果 — 鈴木誠税理士事務所 (L-1563)

## アーキタイプ

**名前**: A: モダンミニマル（士業・権威寄り）

**根拠**:
- 業種: 税理士事務所（山形市）
- 顧客層: 中小企業経営者・個人事業主・資産承継ニーズのある層
- 文体: 硬めの専門用語（巡回監査・自計化・ＰＤＣＡ・書面添付）。信頼性訴求
- 強み訴求: 黒字決算支援・経営計画策定・ＴＫＣ全国会員としての権威性
- 情報量: 中程度（トップ + 事務所紹介 + 経営理念 + 料金 + 業務内容）
- 写真の使い方: 固有写真なし。元サイトは全てＴＫＣテンプレート素材

これらから「モダンミニマル（A）」を採用。見出しは Noto Serif JP で士業らしい重厚感、本文は Noto Sans JP で可読性を担保。余白を大きく取り、情報を整理して表示する。伝統重厚（B）ほど和風に寄せると税理士としての現代的な実務感が薄れるため、A を選ぶ。

## カラーパレット

元サイトは青紫〜藍系のＴＫＣテンプレ配色。色相は継承しつつ、明度・彩度を調整して現代的に。

- **メイン（primary）**: `#1e3a8a`（深い藍）
- **サブ（base）**: `#f8fafc`（ほぼ白のクール系背景）/ `#0f172a`（テキスト濃色）
- **アクセント（accent）**: `#c9a961`（落ち着いた金茶。ＣＴＡに集中）
- セクション区切りに淡い `#eef2ff`（藍の超淡色）を使用

60-30-10 の法則: 白 60% / 藍 30% / 金茶 10%（ＣＴＡ・ホバー・アンダーライン）。

## 画像分類

元サイトは TKC テンプレート＋バナー素材のみで、代表写真・スタッフ写真・事務所外観等の**固有写真は一切存在しない**。全て template 分類で差替対象となる。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | SPメニューボタン |
| 2 | material/lib02/tkc_logo1.gif | template | text-embedded | 差替 | TKC全国会ロゴ（テキストで表現） |
| 3 | material/lib01/bannerContact09.png | template | text-embedded | 不要 | 「お問合せフォーム」バナー |
| 4 | material/lib02/temp02_main01.jpg | template | photo | Unsplash 差替 | TKC トップスライド |
| 5 | material/lib02/temp02_main02.jpg | template | photo | Unsplash 差替 | 同上 |
| 6 | material/lib02/temp02_main03.jpg | template | photo | Unsplash 差替 | 同上 |
| 7 | material/lib02/temp02_pic01.jpg | template | photo | Unsplash 差替 | サービス紹介写真（テンプレ） |
| 8 | material/lib02/temp02_pic02.jpg | template | photo | Unsplash 差替 | 特長紹介写真（テンプレ） |
| 9-13 | material/lib02/KFS_0[1-5].png | template | text-embedded | 不要 | KFS バナー（焼込テキスト） |
| 14 | design/images/bnr-fixed/bnr-invoice-pc1.png | template | text-embedded | 不要 | 固定バナー |
| 15 | design/images/bnr-fixed/bnr-nensyunokabe-pc.png | template | text-embedded | 不要 | 固定バナー |
| 16-19 | icon-close/open/SP bnr 各種 | template | icon/text-embedded | 不要 | UIアイコン・固定バナー |
| 20 | design/images/bg/bg-pat-A008.png | template | icon | CSS/SVG 代替 | 背景パターン |
| 21 | connect.facebook.net/... | template | icon | 不要 | FB トラッキング |
| 22 | material/lib01/756f67...jpg | template | photo | Unsplash 差替 | 事務所紹介ページ写真 |
| 23 | material/lib02/tempcommon_p03_01.jpg | template | photo | Unsplash 差替 | 経営理念ページ |
| 24-25 | material/lib02/tempcommon_p07_0[1-2].jpg | template | photo | 不要 | 料金ページ背景（Hero で統一） |
| 26-30 | material/lib02/tempcommon_p04_0[1-5].jpg | template | photo | 不要 | 業務内容ページ（文章で表現） |
| 31-73 | material/lib03/bnr_*.png | template | text-embedded | 不要 | TKC共通バナー群（全て差替不要） |
| 74+ | 他ページ画像 | template | mixed | 不要 | TKC共通素材 |

**方針まとめ**:
- 固有画像が存在しないため、**ダウンロード対象画像はゼロ**。`images/` フォルダは空でも OK。
- ヒーロー画像のみ Unsplash の士業/ビジネス系画像を1点使用
- アイコン類は全て SVG で描画
- ロゴは社名テキストをそのまま表示（Noto Serif JP で重厚に）

## レイアウト方針

- Header: 固定ヘッダー、左ロゴ（社名テキスト）、右ナビ + TEL
- Hero: フルワイド背景に Unsplash 画像 + オーバーレイ、キャッチ「貴社を毎月訪問し、自計化システムの活用と経営改善計画策定により黒字決算を支援します」
- About: 事務所紹介（開業以来〜精進〜）、所長挨拶（激動の時代〜）
- Philosophy: 経営理念（使命 3 項目 + 行動指針 4 項目）
- Services: 業務内容 11 項目をアイコン付きグリッドで
- Process/Features: 当事務所の特長（月次損益把握・FX自計化・PDCA）
- Pricing: 料金（法人 3 万 / 個人 2 万）をカード2枚で
- TKC: TKC全国会員バッジ + 東北税理士会
- Contact: 事務所概要 + TEL + 問合せフォームへのリンク
- Footer: サイト内リンク + コピーライト
