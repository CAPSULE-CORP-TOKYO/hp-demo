# 分析結果 — L-1751 八戸美千春税理士事務所／有限会社扇藤会計

## アーキタイプ

名前: **A: モダンミニマル**（一部 B: 伝統重厚の要素を混合）

根拠:
- 業種は税理士（士業）であり、顧客層は盛岡市内中小企業の経営者
- 現サイトは TKC 固定テンプレのパステル・2010 年代中期デザインで陳腐化・未レスポンシブ
- 文体は論理的・堅実・情報量多め（創業 1972 年、「自利利他」理念、ＰＤＣＡ・巡回監査・書面添付等の専門語）
- 士業としての信頼感・権威感を保ちつつ、現代的な可読性・余白を確保するモダンミニマル基調が適切
- 「自利利他」や「1972 年創業」など歴史感を出したいので、見出しに Noto Serif JP を部分的に使用

## カラーパレット

元サイトはパステル調（薄い黄色ベースに青緑）だが、パステル特有の軽さが士業の信頼性を損ねている。**色相は継承しつつ彩度を下げ、現代的な深みを出す**。

- メイン（primary）: `#0f3c5c` — 深いネイビーブルー（信頼・権威・士業の定番）
- サブ（base/surface）: `#f7f5ef` — 温かみのあるオフホワイト（元サイトのベージュ系パステルを継承して落ち着かせた色）
- アクセント（accent）: `#c89b3c` — 落ち着いたゴールド（CTA・ハイライト用。伝統感を出しつつ現代的）
- テキスト: `#1a1a1a` — 濃いめチャコール
- サブテキスト: `#5c5c5c`
- ボーダー: `#d9d4c6`

60-30-10: base（オフホワイト）60% / primary（ネイビー）30% / accent（ゴールド）10%。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガーアイコン |
| 2 | .../tkc_logo1.gif | template | text-embedded | 差替 | TKC 全国会ロゴ（テキスト焼込） |
| 3 | .../temp11_main01.jpg | template | photo | 差替 | TKC テンプレ汎用ヒーロー画像 |
| 4 | .../temp11_main02.jpg | template | photo | 差替 | 同上 |
| 5 | .../temp11_main03.jpg | template | photo | 差替 | 同上 |
| 6 | .../76421211_10.png | template | photo | 差替 | TKC 付属イラスト |
| 7 | .../1371742.jpg | stock | photo | 差替 | 税金・家・車のストック画像 |
| 8 | .../bnr-nensyunokabe-pc.png | template | text-embedded | 差替 | 「年収の壁」バナー（焼込） |
| 9-11 | .../icon-*.png, bnr-sp.png | template | icon/text-embedded | CSS/SVG 代替 | |
| 12-14 | .../bg-pat-*.png, fb-pixel | template/tracking | — | 差替/無視 | |
| 15 | .../76421210_03.png | template | photo | 差替 | TKC 付属の男性イラスト（alt「所長の写真」だが実物は所長ではない） |
| 16 | .../54813830.jpg | stock | photo | 差替 | TAX / 家 / 車 のストック画像（alt「事務所内」だが実物は stock） |
| 17 | .../jiririta2012_02.jpg | template | text-embedded | 差替 | 「自利利他」揮毫画像（TKC 共通・テキスト焼込） |
| 18 | .../56fb394ef296d4c46fa87758.jpg | template | photo | 差替 | TKC 全国会会員大会の集合写真（共通素材） |
| 19-24 | .../service 系各種 | template | text-embedded/diagram | 差替 | 巡回監査・自計化・書面添付等の TKC 共通イラスト |
| 25+ | スタッフ/joboffer/kyosai/system-qa/nensyunokabe 等 | template/stock | various | 差替 | 全て TKC 共通素材 |

**結論**: このサイトには会社固有のオリジナル写真・ロゴ・代表写真等が **一切存在しない**。全画像が TKC 全国会共通の template 素材または汎用 stock。

**引き継ぐ画像**: ゼロ。`images/` ディレクトリにはロゴ文字ロゴ（SVG）を生成するか、全て Unsplash / CSS / SVG で構築する。

## 画像戦略

- ロゴ: テキストロゴ（SVG or HTML + 日本語フォント）で生成
- ヒーロー: Unsplash の「office / accounting / morioka / japanese business」系の落ち着いた画像
- セクション区切り: Unsplash の「business meeting / consulting / calculator / documents」系
- アイコン: Unicode / インライン SVG
- スタッフ写真: なし（Unsplash も使わず、テキスト中心のカードにする方が誠実）
- 事務所外観/内観: Unsplash の「japanese office interior」系で代替

## 業種プロファイル

- 業種: 税理士事務所
- フォント: Noto Sans JP（本文）+ Noto Serif JP（見出し・経営理念・「自利利他」等の歴史要素）
- 伝統系アクセント: 経営理念セクションで Serif + ゴールド罫線
- モバイルファースト必須（現サイトは viewport 未設定）
