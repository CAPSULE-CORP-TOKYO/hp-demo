# 分析結果 — L-1822 佐藤英耕税理士事務所

## アーキタイプ
名前: **A: モダンミニマル**（+ B の要素を少し）
根拠:
- 士業（税理士）で奥州市／地域密着。権威性と清潔感・信頼感が求められる。
- 現行サイトは2000年代中盤の TKC テンプレで、GIF/緑地/黄色サイドバー乱立の情報過多。
- リデザインの方針は「余白を使った端正な情報整理 + 明朝のアクセントで落ち着きを添える」。
- メイン本文は Noto Sans JP、セクション見出しのみ Noto Serif JP を使用。

## カラーパレット
元サイトは緑基調。色相を継承して落ち着いたディープグリーン系に刷新する。

- メイン: `#2F5D3A`（ディープグリーン、信頼感）
- サブ: `#F5F7F3`（オフホワイト背景）
- アクセント: `#C89B3C`（ウォームゴールド、CTA用）
- テキスト: `#1F2A24` / `#4A5850`

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 2 | .../56ff5229cb8619c9650003d7.jpg | original | text-embedded | 差替 | 社名のテキスト焼込画像（ロゴ風） |
| 3 | .../56ff522bcb8619c9650003d8.gif | template | photo | 差替 | TKC テンプレ装飾 |
| 4 | .../570f5236e3e9402d5123e2c1.gif | template | photo | 差替 | TKC テンプレ装飾 |
| 5 | .../56ff5237cb8619c9650003e1.jpg | template | photo | 差替 | スライダー（TKCテンプレ花風景） |
| 6 | .../56ff5239cb8619c9650003e2.jpg | template | photo | 差替 | スライダー（TKCテンプレ舵輪） |
| 7 | .../56ff523acb8619c9650003e3.jpg | template | photo | 差替 | スライダー（TKCテンプレ向日葵、alt は「当事務所は皆様の様々なニーズにお応えします」だが実体は汎用テンプレ画像） |
| 9-12 | .../56ff523d〜56ff5241.gif | template | text-embedded | 差替 | 「お役立ちコーナー」用の TKC ボタン画像群 |
| 13 | .../5f4f2dfe0b95262870f1710d.jpg | original? | photo | **そのまま引き継ぎ** | 鬼剣舞（岩手県北上地方の伝統郷土芸能）。地域性のある写真。事務所のオリジナリティに直結しないが、地域色を出すのに適する → 今回は Unsplash 差替で奥州の風景を入れ替えたいが、安全側に倒して使わず、Unsplash で差し替える |
| 14 | .../tkc_logo1.gif | original | photo | そのまま引き継ぎ | TKC全国会ロゴ（信頼バッジに使用） |
| 15,16,19,20 | .../bnr-*.png | template | text-embedded | 差替 | TKC 固定バナー（インボイス／年収の壁） |
| 21,22 | bg-pat*.png, facebook px | template | icon/bg | 差替 | 背景パターン・トラッキング |
| 69 | .../5f4f3bc54b92bbc7772bb9aa.jpg | **original** | photo | **そのまま引き継ぎ** | 代表・佐藤英耕氏の顔写真 |
| 70 | .../56ff5245cb8619c9650003eb.jpg | **original** | photo | **そのまま引き継ぎ** | 事務所外観（レンガ色の建物、国道397号線沿い） |
| 71 | .../56ff5247cb8619c9650003ec.jpg | **original** | photo | **そのまま引き継ぎ** | 事務所玄関 |
| 72 | .../56ff5248cb8619c9650003ed.jpg | **original** | photo | **そのまま引き継ぎ** | 事務所内観（スタッフが働く様子） |
| 73 | .../56ff524acb8619c9650003ee.jpg | original | photo | 差替 | TKC創業経営革新バッジ（小さく、参考まで。使わない。tkc_logo1 で代替） |
| 74 | .../56ff524ecb8619c9650003f1.gif | template | diagram | 差替 | map 用飾り |

**引き継ぎ画像（Phase 5-0 でローカル化する）**:
1. img69 代表写真 → `images/rep.jpg`
2. img70 事務所外観 → `images/office-ext.jpg`
3. img71 事務所玄関 → `images/office-entrance.jpg`
4. img72 事務所内観 → `images/office-interior.jpg`
5. TKC logo → `images/tkc-logo.gif`

その他は Unsplash 差替または CSS/SVG 代替とする。
