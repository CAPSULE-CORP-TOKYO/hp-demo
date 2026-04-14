# 分析結果

## アーキタイプ
名前: A（モダンミニマル）+ E（テキストヘビー）のハイブリッド
根拠:
- 業種: 税理士・会計事務所（士業）。客層は中小企業経営者・個人事業主。
- 情報量はそれなりに豊富（経営理念・業務案内）。権威系。
- 創業昭和35年の老舗だが TKC 全国会会員で保守的な堅実さを重視。
- 現代的な士業サイトに倣い、Aモダンミニマル基調で、必要な所に情報密度を持たせる。
- 装飾は最小限、タイポグラフィ（日本語見出しは Noto Sans JP、アクセントで Noto Serif JP）で信頼感を演出。

## カラーパレット
元サイトは TKC テンプレの緑系（葉っぱ背景）。色相を継承しつつ、現代的に洗練させる。
- メイン: #1a4d3a（深緑、信頼・堅実）
- サブ: #f3f7f4（オフホワイト寄りの薄緑グレー、背景）
- アクセント: #c9a227（落ち着いたゴールド、CTA用）
- テキスト: #1c2624（濃グレー）
- 罫線: #d8e3dc

60-30-10: 背景#f3f7f4(60) / メイン#1a4d3a(30) / アクセント#c9a227(10)

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 2 | .../571f3bb7...e3.jpg | original | photo | そのまま | 事務所内の窓辺・植物。所長挨拶脇で使う |
| 5 | .../571f3bb0...df.jpg | stock | photo | 差替 | 黄色い花。汎用ストック |
| 6 | .../571f3bb3...e0.jpg | stock | photo | 差替 | 緑の並木道。汎用ストック |
| 7 | .../571f3bb4...e1.jpg | stock | photo | 差替 | 草原と青空。汎用ストック |
| 8 | .../571f3bb6...e2.jpg | stock | photo | 差替 | ねこやなぎ。汎用ストック |
| 9 | .../KFS_01.png | template | text-embedded | 差替 | TKC KFSバナー |
| 10 | .../KFS_02.png | template | text-embedded | 差替 | TKC KFSバナー |
| 11 | .../KFS_03.png | template | text-embedded | 差替 | TKC KFSバナー |
| 12 | .../KFS_04.png | template | text-embedded | 差替 | TKC KFSバナー |
| 13 | .../KFS_05.png | template | text-embedded | 差替 | TKC KFSバナー |
| 14 | .../tkc_logo1.gif | template | diagram | 差替 | TKC 全国会ロゴ。ブランド名テキスト表示で代替 |
| 15-20 | .../bnr-*.png | template | text-embedded | 差替 | インボイス等バナー |
| 21 | .../571f3bb9...e4.png | template | text-embedded | 差替 | 「自利利他」焼込画像 |
| 22 | .../571f3bba...e5.png | template | text-embedded | 差替 | 「わたしたちにお任せください」焼込 |
| 23 | .../571f3bbc...e6.jpg | template | text-embedded | 差替 | 大ホール TKC 集合写真＋テキスト焼込 |
| 24 | .../571f3bbd...e7.gif | original | diagram | 差替 | 地図。Google Maps iframe で代替 |
| 25 | .../571f3bbe...e8.jpg | stock | photo | 差替 | 新聞+電卓。汎用ストック |
| 26 | .../571f3bc0...e9.jpg | original | photo | そのまま | 会議室の実スタッフ写真（後ろ姿のため顔なし） |
| 27-39 | TKC 各種バナー | template | text-embedded | 差替 | 全て TKC 共通素材 |
| 40-74 | .../SystemImage.aspx?... | template | icon/diagram | 差替 | TKC システム Q&A アイコン群（本デモでは使わない） |

### 引き継ぎ画像リスト（Phase 5-0 でローカル化対象）
- #2: 571f3bb7e2e8177f7b0032e3.jpg → images/office-window.jpg
- #26: 571f3bc0e2e8177f7b0032e9.jpg → images/office-meeting.jpg

### 差替画像方針
- ヒーロー背景: Unsplash の office/tax/accounting 系
- サービス紹介: 無し（CSS のアイコンで表現）
- 事務所概要: そのまま写真を使用
