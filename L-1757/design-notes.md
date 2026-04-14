# 分析結果: L-1757 小野寺孝一税理士事務所

## アーキタイプ
名前: A（モダンミニマル）+ 一部 B（落ち着き・権威感）の要素
根拠:
- 業種: 税理士事務所（士業）。信頼感・誠実さが重要。
- 元サイトの文体は説明的で情報量が多く、「自利利他」という経営理念や行動指針など、倫理・堅実性を打ち出している。
- 集合写真・過度な装飾はテンプレート由来で価値が低い一方、事務所外観・内観写真・書道作品「自利利他」は固有価値が高い。
- 現代的な士業サイトの王道 = モダンミニマル（高コントラスト、広い余白、サンセリフ見出し、読みやすい明朝体補助）で再設計する。
- ただし堅実・権威感を損なわないよう、配色は元サイトの紺色（ネイビー）を基調にし、装飾は控えめに。

## カラーパレット

元サイト screenshot から抽出:
- 事務所建物の紺色、バナー類の水色、TKC のブルーが基調。

新サイト適用:
- メイン: `#0f2f5a`（深いネイビー。信頼・安定感）
- サブ（ベース）: `#f4f6fa`（わずかに青みを帯びたオフホワイト）
- テキスト: `#1a2332`（ほぼブラック）
- アクセント: `#c9a44c`（落ち着いた金。CTA・見出しアクセント）
- 罫線: `#d9dee7`

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../571f3616...gif (240x60) | original | text-embedded | CSS/SVG 代替 | 小野寺孝一税理士事務所 テキストロゴ |
| 2 | .../571f3617...jpg (経営アドバイス) | template | text-embedded | 差替 | TKC テンプレバナー |
| 3 | .../60d14258...png (BESTホームページ) | template | text-embedded | 差替 | TKC 広告バナー |
| 4 | .../571f361a...gif (140x80) | template | text-embedded | 差替 | 動画バナー・焼込 |
| 5 | .../571f361c...jpg (560x420) | **original** | **photo** | **そのまま引き継ぎ** | 事務所外観（看板あり） |
| 6 | .../571f361f...jpg (560x420) | **original** | **photo** | **そのまま引き継ぎ** | 事務所内観（スタッフ執務） |
| 7 | .../571f3629...png | template | text-embedded | 差替 | TKC 大会集合写真にテキスト焼込 |
| 8 | .../bnr_useful011.png | template | text-embedded | 差替 | TKC 経営アドバイスバナー |
| 9 | .../571f3620〜3626...jpg | template | text-embedded | 差替 | TKC KFS バナー |
| 10 | .../KFS_01〜05.png | template | diagram | 差替 | TKC テンプレダイアグラム |
| 11 | .../tkc_logo1.gif | template | photo | 差替 | TKC ロゴ（外部） |
| 12 | .../bnr-invoice-pc1.png, bnr-nensyunokabe-pc.png | template | text-embedded | 差替 | TKC 固定バナー |
| 13 | .../btn-sp-menu.png, icon-close.png, icon-open.png | template | icon | CSS/SVG 代替 | UI アイコン |
| 14 | office.html: 201208010954_YH3KL.JPG (717x538) | **original** | **photo** | **そのまま引き継ぎ** | 事務所外観（正面・駐車場つき） |
| 15 | info.html: 201210121425..., 201210121457... | template | text-embedded | 差替 | 小さい広告画像（210x100, 175x55） |
| 16 | philosophy.html: 571f3627...png (自利利他) | **original** | **photo/artwork** | **そのまま引き継ぎ** | 書道作品「自利利他」320x240 |
| 17 | philosophy.html: 571f3629...png | template | text-embedded | 差替 | 集合写真（重複） |
| 18 | free3.jpg (885x1024) | template | text-embedded | 差替 | TKC PX まいポータル広告 |
| 他 TKC システム系ページの多数画像 | template | text-embedded/diagram | 差替（= 使用しない） | TKC 商品説明用テンプレ画像 |

### 引き継ぎ画像（ローカル化対象）

以下3点のみを images/ にダウンロードして使用する:
1. `571f361ce2e8177f7b00279d.jpg` → `office-exterior-1.jpg`（事務所外観・看板）
2. `571f361fe2e8177f7b00279f.jpg` → `office-interior.jpg`（事務所内観）
3. `201208010954_YH3KL.JPG` → `office-front.jpg`（事務所正面）
4. `571f3627e2e8177f7b0027a5.png` → `jiri-rita.png`（書道「自利利他」）

Unsplash や外部画像は Hero 背景として業種イメージ（盛岡市・東北・ビジネス）を使用する代わりに、モダンミニマルなので Hero は **大判テキスト + ネイビー背景グラデ**のみで構成し、画像に依存しない。
