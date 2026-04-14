# 分析結果

## アーキタイプ
名前: A（モダンミニマル）+ B 寄り（士業の権威感を出すため見出しに Noto Serif JP を併用）
根拠: 福島県郡山市の総合会計事務所。クライアントは中小企業・医療・福祉の経営者層。文体は丁寧で論理的、情報量多め。元サイトもブルー基調・カード型・サンセリフで現代寄り。リデザインは余白を広げ・タイポを整え・配色を絞り、信頼感のある士業らしさを強化する。

## カラーパレット
- ベース: #ffffff
- メイン（深い紺）: #0F2D52
- サブ（インディゴブルー）: #1E4F8A
- アクセント（ブライトブルー）: #2D8BD6
- テキスト本文: #1F2937
- テキスト副: #4B5563
- ボーダー / グレー: #E5E7EB
- 背景セクション交互: #F5F8FC

元サイトの青系トーンを継承（メインロゴ・スライドオーバーレイ・カードの青）。色相 200〜220 を維持。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | http://www.araikaikei.co.jp/images/logo-wide.svg | original | photo (ロゴ) | そのまま | ヘッダー / フッター ロゴ |
| 2 | http://www.araikaikei.co.jp/images/access-01.jpg | original | photo | そのまま | 事務所外観（ヒーロー & About） |
| 3 | http://www.araikaikei.co.jp/images/access-02.jpg | original | photo | そのまま | AMC エントランス看板 |
| 4 | http://www.araikaikei.co.jp/images/access-03.jpg | original | photo | そのまま | 待合室・庭 |
| 5 | http://www.araikaikei.co.jp/images/slide-01.jpg | original | text-embedded | 差替（access-01 を使用） | 同じ外観だがテキスト焼込 |
| 6 | http://www.araikaikei.co.jp/images/slide-02.jpg | stock | text-embedded | 差替 | 握手＋焼込「豊富な実績と信頼。」 |
| 7 | http://www.araikaikei.co.jp/images/slide-03.jpg | stock | text-embedded | 差替 | 都市景観＋焼込 |
| 8 | http://www.araikaikei.co.jp/images/top_service-01.jpg | stock | photo | 差替（CSS/SVG アイコン） | 電卓ストック |
| 9 | http://www.araikaikei.co.jp/images/top_service-02.jpg | stock | photo | 差替（CSS/SVG アイコン） | 握手ストック |
| 10 | http://www.araikaikei.co.jp/images/top_service-03.jpg | stock | photo | 差替（CSS/SVG アイコン） | コンサル男性ストック |
| 11 | http://www.araikaikei.co.jp/images/top_service-04.jpg | stock | photo | 差替（CSS/SVG アイコン） | スーツ女性ストック |
| 12 | http://www.araikaikei.co.jp/images/top_service-05.jpg | stock | photo | 差替（CSS/SVG アイコン） | 書類ストック |
| 13 | http://www.araikaikei.co.jp/images/top_service-06.jpg | stock | photo | 差替（CSS/SVG アイコン） | 会議ストック |
| 14 | http://www.araikaikei.co.jp/images/top_service-07.jpg | stock | photo | 差替（CSS/SVG アイコン） | 創業 |
| 15 | http://www.araikaikei.co.jp/images/top_service-08.jpg | stock | photo | 差替（CSS/SVG アイコン） | 相続 |
| 16 | http://www.araikaikei.co.jp/images/top_service-09.jpg | stock | photo | 差替（CSS/SVG アイコン） | 医療福祉 |
| 17 | http://www.araikaikei.co.jp/images/top_service-10.jpg | stock | photo | 差替（CSS/SVG アイコン） | 補助金 |
| 18 | https://www.gazou-data.com/contents_share/files/title/news-contents_top.png | template | text-embedded | 不要 | 外部 PHP の見出し画像 |
| 19 | http://www.araikaikei.co.jp/images/top_news-01.svg | template | text-embedded | 不要 | コラム見出し（テキスト焼込） |
| 20 | http://www.araikaikei.co.jp/images/top_news-02.svg | template | text-embedded | 不要 | 同上 |
| 21 | http://www.araikaikei.co.jp/images/top_news-03.svg | template | text-embedded | 不要 | 同上 |
| 22 | http://www.araikaikei.co.jp/images/top_news-04.svg | template | text-embedded | 不要 | 同上 |
| 23 | http://www.araikaikei.co.jp/images/top_news-05.svg | template | text-embedded | 不要 | 同上 |
| 24 | http://www.araikaikei.co.jp/images/top_news-06.svg | template | text-embedded | 不要 | 同上 |
| 25 | http://www.araikaikei.co.jp/images/top_news-07.svg | template | text-embedded | 不要 | 同上 |
| 26 | http://www.araikaikei.co.jp/images/banner-01.jpg | original/text-embedded | text-embedded | 差替（access-01 流用） | 「事業所概要」焼込 |
| 27 | http://www.araikaikei.co.jp/images/banner-02.jpg | stock | text-embedded | 差替 | 「リクルート」焼込 |
| 28 | message-01.jpg | original/photo? | photo | 不要 | 上空建物トリミング、access-01 で代替 |
| 29 | recruit-*.jpg | stock | photo | 不要（リデザインで使わない） | リクルートはテキストのみで構成 |

## お知らせ（news）の扱い

トップページの「相続の最新動向・記事」セクションは、外部 PHP（contents.araikaikei.co.jp/top.php）が CP932 系で生成しており、HTML 抽出時に文字化け（mojibake）した。そのため記事タイトルは原文として復元不能。リデザインではお知らせ最新5件は省略する（誤った文字列を表示しない）。代わりに、固定の「相続コラムシリーズ」一覧（top_news-01〜07.svg の alt から取得した7つの相続コラムタイトル）はテキストとして掲載する（alt は UTF-8 で正常に取れている）。

## レイアウト方針

- ヘッダー: 白背景・ロゴ左・ナビ右・モバイルはハンバーガー
- ヒーロー: 事務所外観（access-01.jpg）を背景に、深い紺のグラデーションオーバーレイ、白文字でキャッチ「士業協業ワンストップサービスで、経営課題の解決を支援いたします。」（原文一字一句）。サブテキストは説明文と CTA。
- About（事業方針より引用）: 2 カラム（写真 + 文章）
- Services: 6 カードグリッド（税務会計／相続事業承継／コンサル／社労／行政手続／経理アウトソーシング） — アイコンは SVG
- お悩み別ニーズ: 4 カード（創業・起業／相続・事業承継／医療・福祉／補助金・助成金）
- 相続コラムシリーズ: 2 列リスト（7 項目）
- 事業所概要: テーブル + 写真（access-02 看板, access-03 待合室）
- 契約までの流れ: 4 ステップ
- お問い合わせ CTA: 大きな TEL + フォームリンク
- フッター: 法人名・住所・TEL・各種リンク
- モバイル下部追従 CTA: TEL + お問い合わせフォーム
