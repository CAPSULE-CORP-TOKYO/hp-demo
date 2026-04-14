# 分析結果

## アーキタイプ
名前: A（モダンミニマル）＋ B（伝統重厚）のハイブリッド、主軸は A
根拠:
- 業種が税理士法人で士業の権威性と誠実さが必要（B 要素）
- いわき市の地域密着・中小企業支援という顧客層を考えると、重たすぎず読みやすい方が良い（A 寄り）
- 結論: サンセリフ主体 (Noto Sans JP) + 見出しのみ Noto Serif JP、ゆったりした余白、クリーンなカード配置で「モダンで信頼感のある士業サイト」に寄せる。

## カラーパレット
元サイトのヘッダーナビが濃グリーン、ロゴが鮮やかな青 + 黒。
- メイン: #1F6FB5（ロゴの青を基調に士業向けに少し深みを持たせたネイビーブルー）
- サブ: #F4F6F8（ベースの淡いグレーホワイト）
- アクセント: #0F5E2E（元サイトの緑系を CTA に継承、落ち着いたディープグリーン）
- テキスト: #1A2433（ダークスレート）
- ボーダー/副次: #E4E8EE

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | files/事務所ロゴ横カラー01.jpg | original | photo（ロゴ） | そのまま引き継ぎ | ヘッダーロゴ・フッターロゴに使用 |
| 2 | files/Inked事務所外観01_LI.jpg | original | photo | そのまま引き継ぎ | Hero またはセクション背景候補 |
| 3 | files/事務所外観02.jpg | original | photo | そのまま引き継ぎ | About/Access セクションに使用 |
| 4 | design/menu_*.png, top_caption_*.png, caption_*.png | template | text-embedded | 差替 | TKC テンプレのテキスト焼込キャプション、全部不要 |
| 5 | gazou-data.com/contents_share/*.jpg (top-image) | template | text-embedded | 差替 | 外部コンテンツプロバイダの挿絵、会社固有ではない |
| 6 | gazou-data.com/.../dot.gif, to-pagetop.png, icon-*.gif | template | icon | CSS/SVG 代替 | 小アイコンは CSS で代替 |
| 7 | gazou-data.com/contents_share/105/139/*.gif (書式集アイコン) | template | icon/thumbnail | CSS/SVG 代替 | 書式集アイコンは SVG で代替 |
| 8 | gazou-data.com/contents_share/-9999/-9999/ao-*.gif | template | illustration | 差替 | キャラクターイラストはテンプレ、不要 |

**結論**: 引き継ぎ対象は 3 枚（ロゴ、事務所外観 2 枚）。その他はテンプレ素材として全て除外。テンプレ画像の代替は Unsplash の税理士/オフィス系写真 or CSS/SVG アイコン。
