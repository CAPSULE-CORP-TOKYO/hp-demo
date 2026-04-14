# 分析結果 — L-1733 川村幸子税理士事務所

## アーキタイプ
名前: A: モダンミニマル（士業向け、信頼感と清潔感を重視）
根拠:
- 税理士事務所（士業）で、権威と信頼が重要
- 地方（岩手県盛岡市）の個人会計事務所で派手さは不要
- 元サイトは TKC テンプレートで情報雑然、差別化ポイントが不明確
- 「得意先に喜ばれる仕事」「生きがい・働きがい」「社会貢献」といった経営理念を読ませる構造
- テキスト量は中程度なのでテキストヘビーではなく、余白を活かしたモダンミニマルが適切
- 見出しのみ Noto Serif JP で格調を付加

## カラーパレット
- メイン: #1F3A5F（ネイビーブルー — 信頼・誠実）
- サブ: #E8EEF5（ライトブルーグレー — 清潔・余白）
- アクセント: #C9A14A（ゴールド — 士業の権威・格）
- ベース: #FFFFFF / 文字 #1A1A1A

元サイトはピンク（#cc3366 系）とブルーの TKC テンプレ配色で独自性が薄いため、士業にふさわしいネイビー基調に昇華。色相を全く別系統に変えるのではなく「ブルー」系を継承。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | SP メニューアイコン |
| 2 | library/.../57f703cc9042c3ea401e9177.jpg | template | text-embedded | 差替（HTML テキスト化） | 社名ロゴ画像（焼込） |
| 3 | material/lib01/88278995.jpg | stock | photo | 差替（Unsplash） | スライダー花写真 |
| 4 | material/lib01/1859466.jpg | stock | photo | 差替（Unsplash） | スライダー花写真 |
| 5 | material/lib01/tops-c-flower-0007.jpg | stock | photo | 差替 | スライダー花写真 |
| 6 | material/lib01/tops-a-fl-0117.jpg | stock | photo | 差替 | スライダー花写真 |
| 7 | material/lib01/tops-c-flower-0335.jpg | stock | photo | 差替 | スライダー花写真 |
| 8 | library/.../570cc61568ba6d2622002f4b.jpg | template | text-embedded | 差替 | 経営革新等支援機関バナー |
| 9 | material/lib03/bnr_useful009.png | template | text-embedded | 差替 | TKC バナー |
| 10 | material/lib03/bnr_menu011_a.png | template | text-embedded | 差替 | TKC バナー（相続税額早見表） |
| 11 | design/images/bnr-fixed/bnr-invoice-pc1.png | template | text-embedded | 差替 | 電帳法バナー |
| 12 | design/images/bnr-fixed/bnr-nensyunokabe-pc.png | template | text-embedded | 差替 | 年収の壁バナー |
| 13-16 | icon/sp バナー類 | template | icon/text-embedded | CSS/SVG 代替 | — |
| 17 | material/lib04/bg-illu-A001.png | template | text-embedded | 差替 | 背景イラスト |
| 18 | facebook connect | stock | icon | CSS/SVG 代替 | FB ピクセル |
| **19** | library/.../634ccc20f8027fb1179dac65.jpg | **original** | **photo** | **そのまま引き継ぎ** | **事務所外観（看板あり）** |
| **20** | library/.../634ccc1465d94ab208611118.jpg | **original** | **photo** | **そのまま引き継ぎ** | **事務所外観（建物正面）** |
| 21 | image/title.gif | template | text-embedded | 差替 | サブページタイトル |
| 22-54 | SystemImage.aspx?... | template | text-embedded | 差替 | TKC システムカタログ画像（全除外） |
| 55 | image/footer.gif | template | text-embedded | CSS 代替 | footer 背景 |
| 56 | 570cc61868ba6d2622002f4d.gif | template | text-embedded | 差替 | — |
| 57 | 56a0aaf243770d943aa65c9a.png | template | text-embedded | 差替 | 認定バナー |
| 58-84 | library TKC 広告・資料画像 | template | text-embedded/diagram | 差替 | TKC 共済・インボイス・年収の壁資料（全除外） |
| 85 | 68dcb5d9fe933128e94ce243.jpg | template | text-embedded | 差替 | — |

### 固有画像（そのまま引き継ぐ）
- **#19**: 事務所外観（社名看板入り）
- **#20**: 事務所外観（建物正面全景）

### 重要: TKC 固有画像
- 元サイトは TKC テンプレートで、事務所固有のオリジナル写真は「事務所外観2枚」のみ
- 花のスライダー画像、バナー類、TKC システム・共済・インボイス・年収の壁の資料は全てテンプレ付属のため引き継がない
- ロゴ画像は社名焼込なので HTML テキスト化する

## フォント
- 見出し: Noto Serif JP（権威感）
- 本文: Noto Sans JP（可読性）

## レイアウト方針
- ヒーロー: 事務所外観写真を大判で表示（#20 建物正面）+ キャッチ + CTA
- About: 代表挨拶と経営理念を並べる
- Services: 税務会計4サービスをカード化
- Info: 事務所概要＋交通案内
- Contact: 電話 + フォームリンク
