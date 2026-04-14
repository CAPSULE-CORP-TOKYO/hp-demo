# 分析結果 — L-1407 加藤修税理士事務所

## アーキタイプ

名前: **A: モダンミニマル**（サブ要素として E: テキストヘビーの情報量を吸収）

根拠:
- 業種は税理士（士業）、宮城県石巻市という地方都市の権威系事務所
- 元サイトは TKC テンプレートベースの 2010 年代中盤〜後半の古めなデザイン（診断コメント通り）
- テンプレ文言（「ここにキャッチフレーズの説明を入力してください」「ここに説明文を入力してください」等）が残存し、ページ下半分が空白の未完成感
- 一方で企業概要・サービス・採用情報・経営理念（「自利利他」）は実質的な情報量が豊富 (text-inventory.txt に 1400 行以上)
- リデザイン方針: 大胆な余白・サンセリフ主体・高コントラストで信頼感と清潔感を出しつつ、実テキストの情報量を構造化して見せる
- 所長写真・事務所外観/内観のオリジナル写真が複数あり、視覚的な信頼感を補強できる

## カラーパレット

screenshot.png 目視: 元サイトはブルー系（TKC ブランドカラー近似）をメインにした爽やかな配色。白背景 + 濃紺ヘッダー + ブルーの装飾ライン。

- メイン (primary): `#1e3a8a` — 濃紺（元サイトの濃青ヘッダー帯を継承）
- サブ (secondary): `#2563eb` — 中間ブルー（CTA・アクセント兼用）
- アクセント (accent): `#0ea5e9` — スカイブルー（ボタン/ハイライト）
- ベース (base): `#ffffff` — 白
- テキスト: `#1f2937` (見出し) / `#4b5563` (本文)
- 薄背景: `#f8fafc` — 交互セクションの塗り分け用

60-30-10: base 60% / primary(濃紺) 30% / accent(スカイブルー) 10%

## 画像分類

スクリーンショット・ダウンロード実物確認・alt と URL パターンから分類。

| # | URL slug | 出自 | 適性 | 処理 | 備考 |
|---|---|---|---|---|---|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | モバイルメニューアイコン |
| 2 | library/.../6968d8d5e9fa8629b21f5b91.png (ヘッダーロゴ) | original | text-embedded | 差替 | テキストロゴ焼込、HTML テキストで再現 |
| 3 | library/.../696668aaabf395369735611c.png (TEL画像) | original | text-embedded | 差替 | 電話番号焼込 → HTML テキスト |
| 4 | library/.../698151839b3e067d70a2f9f6.png (お問合せボタン) | original | text-embedded | 差替 | ボタン焼込 |
| 5 | library/.../69b20a13c408e571ed08fb64.png (経営所と共に未来へ) | template | text-embedded | 差替 | スローガン焼込 |
| 6 | library/.../69ba5a0adbbfb236f9223a49.png (ヒーロー合成) | original | text-embedded | 差替 | 外観＋イラスト＋自利利他額装の合成、一部が焼込 |
| 8 | library/.../69b1482308af1f72af7a673f.jpg (所長顔) | original | photo | **そのまま** | 加藤修所長 (shocho) |
| 9 | library/.../698150e115d1e014fc16dbbc.png (事務所案内ボタン) | template | text-embedded | 差替 |  |
| 10 | library/.../698150e83f8db124debe2e3f.png (税理士紹介ボタン) | template | text-embedded | 差替 |  |
| 11 | library/.../69b145f6b65dec716fa51d2a.jpg (bg-image) | unknown | photo | Unsplash 差替 | 背景装飾 |
| 12 | material/lib01/106230503.jpg (bg-image) | template | photo | 差替 | TKC テンプレ素材 |
| 13 | material/lib01/22479616.jpg (bg-image) | template | photo | 差替 | TKC テンプレ素材 |
| 14 | library/.../69b1465ac6a13c6171b5dbe7.jpg (サービス案内) | template | text-embedded | 差替 |  |
| 15-20 | library/.../69685*・69814*.png (サービスアイコン) | template | text-embedded | 差替 | サービス名焼込 |
| 21 | library/.../69b14679f0a736751af0d304.jpg (bg-image) | unknown | photo | Unsplash 差替 |  |
| 22 | library/.../69688540e9c4070be709b408.png (TOPへ戻る) | template | icon | CSS/SVG 代替 |  |
| 23 | library/.../6968d8f1a17a3b0d38017a72.png (フッターロゴ) | original | text-embedded | 差替 | テキストロゴ |
| 26-27 | design/.../bnr-*.png (バナー) | template | text-embedded | 差替 |  |
| 28-29 | design/.../icon-*.png (close/open icon) | template | icon | CSS/SVG 代替 |  |
| 30-31 | design/.../bnr-*-sp*.png | template | text-embedded | 差替 |  |
| 37 | 上記 #8 と同じ URL | original | photo | **そのまま** | 所長顔（company ページ参照） |
| 38 | library/.../69b20a8708af1f72af7a6b40.jpg (外観) | original | photo | **そのまま** | 事務所外観 (exterior1) |
| 39 | library/.../69b1486e4b67647029fd355d.jpg (外観) | original | photo | **そのまま** | 事務所外観 (exterior2) |
| 40 | library/.../69b1486ec408e571ed08f705.jpg (内観) | original | photo | **そのまま** | 事務所内観 (interior1) |
| 41 | library/.../69b1486ec6a13c6171b5dbe7.jpg (外観) | 不明 | - | 差替 | 403 応答（243B）→取得不可 |
| 42 | library/.../69b1486e65b4417572977a00.jpg (外観) | original | photo | 取得確認後 可 | 未確認 |
| 43 | library/.../69b1486ef0a736751af0d32a.jpg (内観) | original | photo | 取得確認後 可 | 未確認 |
| 44 | library/.../57176095f6161e5b2f00167a.png (経営理念) | template | text-embedded | 差替 | |
| 45 | material/lib01/38788971.jpg (行動指針) | template | photo | 差替 | TKC テンプレ素材 |
| 46 | library/.../69c607210be60e4276e27859.jpg (スタッフ) | original | photo | **そのまま** | 所長・加藤修 外 (staff1) |
| 47 | library/.../69c932cb584ce30bd7767c6b.jpg (スタッフ) | original | photo | **そのまま** | 所属税理士・加藤由里絵 (staff2) |
| 48-50 | library/.../FEATURE0*.png | template | text-embedded | 差替 | FEATURE1/2/3 焼込 |
| 51-81 | material/lib07/... | template | text-embedded | 差替 | TKC テンプレ付属のサービスカード/バナー |
| 82-85 | library/.../bg-image | unknown | photo | 差替 | 背景 |
| 86-89 | material/.../recruit-message_img06_0* | template | text-embedded | 差替 | STEP 図 → HTML で再現 |
| 93-113 | tkc-ebooks-invoice / tkc-nensyunokabe | template | diagram | 差替 | サブページ固有画像、メインに含めない |

## メイン採用画像（Phase 5-0 でローカル化する対象）

1. `69b1482308af1f72af7a673f.jpg` — 所長顔写真（バストアップ）
2. `69b20a8708af1f72af7a6b40.jpg` — 事務所外観1
3. `69b1486e4b67647029fd355d.jpg` — 事務所外観2
4. `69b1486ec408e571ed08f705.jpg` — 事務所内観
5. `69c607210be60e4276e27859.jpg` — 加藤修（スタッフショット）
6. `69c932cb584ce30bd7767c6b.jpg` — 加藤由里絵（所属税理士）

合計 6 点を images/ 配下に保存する。全て original × photo で最高価値。

## サイト構造（Phase 4 で詳細化）

Header / Hero / About / Staff / Services / Philosophy / Access / Footer  
（診断コメントの「空白・未完成感」を解消するため、実コンテンツを全て構造化する）
