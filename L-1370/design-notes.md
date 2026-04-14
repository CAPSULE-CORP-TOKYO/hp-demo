# 分析結果 — L-1370 関根秀子税理士事務所

## アーキタイプ
名前: A（モダンミニマル） + 一部 C（ウォームフレンドリー）の要素
根拠:
- 業種=税理士（士業）で信頼性・清潔感が必須。モダンミニマルが基本方針。
- 2代目女性所長による継承事務所で、文体が「税理士は経営者の心のパートナーです」「女性ならではの繊細なサービス」「関与先企業様との繋がりが唯一の自慢」と親しみやすい → 冷たすぎる完全ミニマルではなく、緑の暖かさと余白で柔らかさを持たせる。
- 情報量は中程度（経営理念・業務案内・料金・採用）→ テキストヘビー(E) までは不要。E ではなく A をベースにセクション分けで読みやすく。
- 「エメラルドグリーンの屋根」が事務所の物理的アイデンティティ → ヒーローに事務所外観写真を活かす構成が自然。

## カラーパレット
- メイン（Primary）: #3a8a3a（深緑 — 信頼感・エメラルドグリーンの屋根のイメージ継承）
- サブ（Secondary / base 60%）: #f7f5ef（オフホワイト〜淡ベージュ — 元サイトの背景紙色を継承）
- アクセント（Accent 10%）: #d4a53a（マスタードイエロー — 元サイトのゴールド系アクセント、CTA 集中）
- テキスト: #2d2d2d / サブテキスト #5a5a5a / ボーダー #e5e2d8

色相継承: 元サイトは緑基調 + ベージュ背景 + 金属的ゴールドライン → 緑主軸は維持、明度・彩度を整えて現代的に。

## 画像分類

image-inventory.md の全174画像のうち、sekinekaikei 配下の固有写真は以下2枚のみ（office ページ）。他はすべて TKC 共通テンプレ・バナー（tkc_logo / bnr_useful / bnr-fixed / material/lib）または経営記事サムネイル（tkc-management-qa）で引き継ぎ対象外。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 40 | https://www.tkcnf.com/library/57173b4d5d2fb30a9bdcccf3/5717646ff6161e5b2f001e22.jpg | original | photo | そのまま | 2代目所長・関根秀子氏の執務写真（デスクで撮影、笑顔） |
| 41 | https://www.tkcnf.com/library/57173b4d5d2fb30a9bdcccf3/57176470f6161e5b2f001e23.jpg | original | photo | そのまま | 事務所外観（エメラルドグリーン屋根＋「関根会計事務所」看板） |
| — | .../design/images/common/btn-sp-menu.png | template | icon | CSS/SVG代替 | ハンバーガーアイコン |
| — | .../material/lib02/tkc_logo1.gif | template | photo | 差替 | TKC全国会ロゴ。不要（テキスト表記で代替） |
| — | .../design/images/bnr-fixed/bnr-*.png | template | text-embedded | 差替 | TKC 固定バナー（年収の壁・電帳法）。差替不要 |
| — | .../library/57173b4d5d2fb30a9bdcccf3/57176462〜.jpg (id 2-5) | template | photo | 差替 | トップのビル群イラストスライダー。汎用イラスト |
| — | .../library/.../5717646[8-d].jpg/gif (id 6-9) | template | text-embedded | 差替 | 「経営改善計画」「FX4クラウド」「創業の夢を…」バナー |
| — | .../material/lib03/bnr_menu011_a.png | template | text-embedded | 差替 | TKC 経営情報バナー |
| — | その他 tkc-* ページ内バナー・記事サムネ (id 46〜174) | template | mixed | 差替 | TKC 共通コンテンツ。引き継がない |

**結論**: ローカル化する画像は office ページの2枚のみ。ヒーロー背景など必要に応じて Unsplash で補完する（税理士事務所/和モダンオフィス/千葉の緑の木々 など）。

## フォント選定
- 見出し: Noto Sans JP 700 / サブ見出しに Noto Serif JP（権威感の演出）
- 本文: Noto Sans JP 400/500
- 士業だが女性所長の親しみ系テキストが多いため、完全な明朝主体(B伝統重厚)にはしない。Noto Sans JP をメインに、アクセントとして Serif を少量採用。
