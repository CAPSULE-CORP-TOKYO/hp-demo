# 分析結果

## アーキタイプ
名前: **B: 伝統重厚** 寄り + A: モダンミニマル のハイブリッド
根拠:
- 税理士事務所（士業・権威系）。顧客層は中小企業経営者・個人事業主
- 代表の経営理念が「自利利他」など哲学・仏教的語彙で構成されており、落ち着き・信頼感が訴求の中核
- ただし業務内容は自計化・PDCA・事業再生・事業承継などモダン/実務的
- → 見出しに Noto Serif JP、本文に Noto Sans JP を使う落ち着いた配色の「モダン士業」路線
- ヒーロー大判ビジュアル + 読み物的な読ませるボディ

## カラーパレット

元サイトはティール（青緑）系のヘッダー・左ナビ（おそらく #3FB8B0 前後）と水色背景。
継承した上で明度・彩度を現代化:

- メイン: **#0E6B64**（ダークティール / ヘッダー・見出し・セクションタイトル）
- サブ: **#F4F9F8**（ごく淡いティールベージュの背景）
- アクセント: **#D4A017**（ゴールド寄りの黄、CTA・強調・和の落ち着き）
- テキスト: **#1C2B2A**（ほぼ黒、やや緑寄り）
- ミュート: **#6B7D7C**（補足テキスト）

## 画像分類

元サイトの画像はほぼ全て TKC 全国会テンプレートの付属素材（ボタン・バナー・ロゴ・イラスト）およびストックフォト。代表写真・事務所外観・ロゴマーク等の**事業体固有画像はゼロ**。

| # | URL / 種別 | 出自 | 適性 | 処理 | 備考 |
|---|-----------|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | スマホ MENU ボタン |
| 2 | library/.../pic0.jpg（芽生え） | template | photo | 差替 | トップヒーロー。TKC テンプレ標準写真 |
| 3 | library/.../pic1.jpg | template | photo | 差替 | 同上スライダー |
| 4 | library/.../pic2.jpg | template | photo | 差替 | 同上スライダー |
| 5 | material/lib02/tkc_logo1.gif | template | icon | CSS/SVG 代替 | TKC 全国会ロゴ（組織ロゴ、事務所ロゴではない） |
| 6 | .../経営革新等支援機関.jpg | template | text-embedded | 差替 | 認定バナー画像（HTML で文言化） |
| 7 | material/lib03/bnr_menu011_a.png | template | text-embedded | 差替 | テンプレバナー |
| 8-13 | design/images/bnr-fixed/... | template | text-embedded | 差替 | 電帳法・年収の壁 固定バナー |
| 14 | connect.facebook.net/... | template | icon | CSS/SVG 代替 | FB トラッキング画像 |
| 15 | office ページ 2884024.jpg（コーヒー） | stock | photo | 差替 | 事務所外観ではなくストック |
| 16-17 | philosophy ページ .png 2枚（自利利他書・集合写真） | template | text-embedded | 差替 | TKC 組織画像 |
| 18-24 | service ページ illust_*.png | template | diagram | 差替 | TKC テンプレイラスト |
| 25 | map ページ tkcetax01_a.jpg | template | text-embedded | 差替 | e-Tax バナー |
| 26 | map ページ 54424396.jpg（握手） | stock | photo | 差替 | ストックフォト |
| 27-124 | その他 tkc-* 各ページ bnr/lib 画像 | template | text-embedded / diagram | 差替 | TKC 記事サムネ・テンプレバナー。本デモでは該当セクションそのもの（Q&A・経営者情報一覧）を HTML で再構成しないので不要 |

**結論**: 引き継ぐ画像はゼロ。ヒーローおよびセクションビジュアルは全て Unsplash の業種適合画像（office / business / japanese / calligraphy / consulting）で構成する。ローカル images/ に予めダウンロードする画像も無し。

## 引き継ぎ画像リスト（Phase 5-0 でローカル化する対象）

なし。images/ ディレクトリは空のままで Phase 5 HTML 生成に進む。
