# 分析結果

## アーキタイプ
名前: A: モダンミニマル（B: 伝統重厚のエッセンスを混合）
根拠:
- 士業（税理士事務所）で信頼性・権威性が重要
- 所長挨拶は長文で読み物的な要素が強いが、サイト全体の訴求は「未来的思考」「熱と誠」など合理的・前向き
- 40代〜経営者層が主要顧客で、読みやすさ・清潔感・堅実さが必要
- モダンミニマル基調で、見出しと所長挨拶に明朝体を使い「熱と誠」「信用第一」の理念を視覚的に補強する

## カラーパレット
元サイトから抽出（青＋白＋濃灰の士業定番配色）:
- メイン（primary）: `#1e5fa6`（元サイトの青ボタン・バナー・見出し帯）
- ベース（base）: `#ffffff`（白）/ `#f5f7fa`（薄灰のセクション背景）
- サブ（dark）: `#2a3441`（濃紺グレー、元サイトのダークセクション）
- アクセント（accent）: `#c8102e`（ロゴの赤印 = 澁谷印章の赤を拾い、CTA に集中投下）
- テキスト: `#1f2937`（本文）/ `#6b7280`（補助）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | images/logo01.png | original | text-embedded | CSS/SVG 代替 | 社名＋赤い判子風マーク。HTML テキスト（serif）＋CSS で代替 |
| 2 | images/full_image_1.jpg | stock | photo | Unsplash 差替 | 抽象グラデ背景。ヒーロー画像として再利用不可（情報量ゼロ）→ 業務建物/夜景/山形城の桜系を Unsplash から |
| 3 | images/e-kessai.jpg | stock | text-embedded | CSS/SVG 代替 | 電子決済サービスロゴの集合画像。テキスト（サービス名列挙）で代替 |
| 4 | images/tel_bnr.png | template | text-embedded | CSS/SVG 代替 | 電話番号・営業時間焼込バナー。HTML テキスト＋tel リンクで代替 |
| 5 | images/img_7.jpg | stock | photo | Unsplash 差替 | 抽象グラデ、情報価値なし |
| 6 | images/img_8.jpg | stock | photo | Unsplash 差替 | 抽象グラデ |
| 7 | images/img_10.jpg | stock | photo | Unsplash 差替 | 抽象グラデ |
| 8 | images/qanda-q.png | template | icon | CSS/SVG 代替 | Q 吹き出しアイコン。`Q` 文字＋CSS |
| 9 | images/qanda-a.png | template | icon | CSS/SVG 代替 | A 吹き出しアイコン。`A` 文字＋CSS |
| 10 | images/rec1.jpg | stock | photo | Unsplash 差替 | 電卓とノート（汎用ストック） |
| 11 | images/rec2.jpg | stock | photo | Unsplash 差替 | 女性2人ミーティング（汎用ストック） |
| 12 | images/rec-3-1〜6.jpg | stock | photo | Unsplash 差替 | いずれも汎用ストック |
| 13 | wordpress/cropped-5561.jpg | stock | photo | 不要 | ブログサイトヘッダ。本サイトでは使わない |
| 14 | wordpress/*-640x340.jpg | stock | photo | 不要 | ブログ記事サムネ。ニュース欄には日付＋タイトルのみ掲載 |
| 15 | wordpress/logo01.png | original | text-embedded | 不要 | ブログ側のロゴ複製 |

## 方針サマリ

- 元サイトに固有の写真（代表写真・外観・スタッフ）が一切存在しない → Unsplash に頼る
- ヒーローは山形城＋桜 or ビジネス系の Unsplash 写真を使用
- ロゴはテキスト化（serif + 赤丸アクセント）
- 電話番号バナー・電子決済バナーは HTML テキストで再現（情報保持）
- 画像は全て「そのまま継承」ゼロ。ローカル化対象なし → images/ ディレクトリは作るが空でよい
