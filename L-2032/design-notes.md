# 分析結果

## アーキタイプ
名前: A: モダンミニマル（ベース） + E: テキストヘビー（コンテンツ要素）

根拠:
- 税理士業種で権威と信頼を訴求する必要あり
- 情報量が多い（業務案内・経営理念・行動指針など読み物が豊富）
- 士業のため過度な装飾より余白・タイポグラフィで品質を出す方が合う
- 明朝体は見出しにのみ使用（Noto Serif JP）し、本文は Noto Sans JP で可読性確保
- 会津若松の自然写真（本物のオリジナル）があるため、Hero はフルバナー写真で「地域密着」を訴求

## カラーパレット
元サイトは薄イエロー（#FFFBE6 付近）+ 緑ロゴ（#2E7D4A 付近）+ 青のバナー群。
TKC テンプレが混在しているが、ロゴの緑を主軸として継承する。

- メイン（プライマリ）: #1F5A3A（深緑、ロゴ色をやや暗め寄りに）
- サブ（アクセントライン用）: #C9A227（金茶、会津盆地のイメージ）
- ベース: #FFFFFF / #F7F5EE（温かみのあるオフホワイト）
- テキスト: #1A1A1A / #555555
- CTA アクセント: #C0392B（決断を促すレッド、控えめに使用）

60-30-10:
- 60% ベース白・オフホワイト
- 30% 深緑プライマリ（ヘッダー・セクションタイトル・アイコン）
- 10% 金茶アクセント（アンダーライン・区切り線）＋ CTA レッド

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 2 | library/.../201210011628_Rr2IV.gif (400x100 logo) | original | text-embedded | そのまま | 事務所ロゴ。テキスト焼込だが企業アイデンティティ＝そのまま採用 |
| 3 | library/.../573185c5f490ead1690036c0.gif (140x80) | template | text-embedded | 差替/不使用 | TKC テンプレ差込、テキスト焼込 |
| 4 | library/.../575e58414ccb60eb6dd49737.jpg | original | photo | そのまま | 会津のニッコウキスゲ（自然写真） |
| 5 | library/.../575e4c25323d0f1a42bcea05.jpg | original | photo | そのまま | 鶴ヶ城（会津若松） |
| 6 | library/.../5b3a4489ec2c87911c1a5e88.jpg | original | photo | そのまま | 初夏の会津盆地（水田） |
| 7 | library/.../5b3a42c7b92543eb10f38f01.jpg | original | photo | そのまま | 秋の会津盆地（稲） |
| 8 | library/.../5b3a4865f08b3b181d9bc12e.jpg | original | photo | そのまま | 残雪の会津盆地（飯豊連峰） |
| 9-20 | library/.../bnr 系 *.jpg | template | text-embedded | 差替/不使用 | TKC バナーサムネ、文字焼込 |
| 21-25 | material/lib02/KFS_0*.png | template | text-embedded | 差替/不使用 | TKC 用素材 |
| 26 | material/lib02/tkc_logo1.gif | template | icon | CSS/テキスト代替 | TKC 全国会ロゴはテキストで明記 |
| 27-32 | design/images/bnr-fixed/*.png | template | text-embedded | 差替/不使用 | 電帳法・インボイス固定バナー |
| 33 | facebook rsrc | tracking | — | 除外 | トラッキング |
| 34 | library/.../201406080031_V0fbd.png (office) | original | photo | そのまま | 所長本人の写真（認定証と書を背景に） |
| 35 | library/.../573185def490ead1690036d0.png | template | text-embedded | 不使用 | 「自利利他」テキスト画像 |
| 36 | library/.../573185dff490ead1690036d1.png | template | text-embedded | 不使用 | 「わたしたちにお任せください！」 |
| 37-39 | library/.../service の JPG | template | photo | 不使用 | 握手・電卓等のストック風 |

## 引き継ぐ画像（5点）

1. 事務所ロゴ (img2.gif → logo.gif)
2. 会津ニッコウキスゲ (img4.jpg → aizu-lily.jpg)
3. 鶴ヶ城 (img5.jpg → tsurugajo.jpg)
4. 会津盆地・初夏 (img6.jpg → aizu-early-summer.jpg)
5. 会津盆地・秋 (img7.jpg → aizu-autumn.jpg)
6. 会津盆地・残雪 (img8.jpg → aizu-snow.jpg)
7. 所長写真 (img34.png/jpg → shozo-matsuzaki.jpg)

写真は「会津の四季」スライダー/ギャラリーとして Hero 背景もしくは About セクションに配置し、「地域密着」を視覚的に訴求する。
