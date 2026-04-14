# 分析結果

## アーキタイプ
名前: A: モダンミニマル
根拠: 税理士法人（士業）。5人の税理士による法人・5拠点ネットワーク・TKC全国会会員という権威情報と、経営理念（当たり前のことを当たり前に）を明快に打ち出したい。元サイトは青系ネイビーを使った士業らしいトーン。古い TKC テンプレの「バナー・アイコンを並べる情報過多なレイアウト」を整理し、余白を活かしたモダンミニマルで再構成する。サンセリフ（Noto Sans JP）メイン、見出しは Noto Serif JP で権威感を軽く加える。

## カラーパレット
- メイン: #0B3D91（ネイビー／元サイトの青系ヘッダーを継承しつつ深める）
- サブ: #E8F0F7（ベリーライトブルー／背景分離）
- アクセント: #F4A11A（オレンジ寄り／元サイトの CTA 緑はくすみやすいので、ネイビー×暖色でコントラストを取る）
- ベース: #FFFFFF / #1A2B42（テキスト濃紺）

※ 元サイトの色相（青＋緑系アクセント）を尊重。彩度のみ現代的に調整。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS代替 | SPメニューボタン |
| 2 | library/.../5ad83684e30bf7204b12c619.png | original | text-embedded | 差替 | 社名ロゴ（ヘッダー）→ HTML テキスト+SVG |
| 3 | library/.../5ad83843059b2188421b7b7b.png | original | text-embedded | 差替 | 「メール問い合わせ」焼込ボタン |
| 4 | library/.../5ad83842e30bf7204b12c65c.png | original | text-embedded | 差替 | 電話番号焼込画像 |
| 5 | library/.../5ad843a1b9708bad54ac067f.png | original | text-embedded | 差替 | 「当たり前のことを正しく処理」焼込 |
| 6 | library/.../5ee072c8bafbe7c01fed380d.png | original | text-embedded | 差替 | スライダーキャッチ焼込 |
| 8-17 | material/lib03/bnr_*.png | template | text-embedded | 差替 | TKC 提供バナー群（Q&A・カレンダー等） |
| 18 | library/.../5ad844a9efa7f49d5eb54ec8.png | original | text-embedded | 差替 | 「相続手続きでお困り」焼込 |
| 19 | material/lib03/bnr_management-innovation001.png | template | text-embedded | 差替 | 経営革新支援機関バナー |
| 20 | library/.../5ad8407ffe1557f851ac601f.png | original | text-embedded | 差替 | フッターロゴ（Peer to Peer） |
| 22 | material/lib02/tkc_logo1.gif | template | diagram | 差替 | TKC 全国会ロゴ → SVG バッジで代替 |
| 40 | .../5ad83982059b2188421b7bb6.jpg | original | photo | **そのまま** | 阿部？代表の半身写真（絵画バック） |
| 41 | .../5ad83a09e30bf7204b12c6c3.png | original | text-embedded | 差替 | 「ピアツーピア・グループ代表」焼込バナー |
| 42 | .../5ad839b1059b2188421b7bbc.jpg | stock | photo | 差替 | 握手ストック写真 |
| 43 | .../5ad83ba7fe1557f851ac5ee8.png | original | photo | **そのまま** | 木口隆（本店）顔写真 |
| 44 | .../5ad83ba8efa7f49d5eb54c89.jpg | original | photo | **そのまま** | 森谷和則（天童事務所）※絵画バックの大きい写真 |
| 45 | .../5ad83ba9fe1557f851ac5ee9.png | original | photo | **そのまま** | 工藤春男（山辺支店）顔写真 |
| 46 | .../5ad83ba8b9708bad54ac04f0.png | original | photo | **そのまま** | 大津史彦（山形北事務所）顔写真 |
| 47 | .../5ad83ba8e30bf7204b12c751.png | original | photo | **そのまま** | 早坂吉孝（新庄事務所）顔写真 |
| ヒーロー背景 | — | — | — | Unsplash 差替 | 山形の山岳／緑の大地系（元サイトスライダーは空と草原の焼込画像だったため代替） |
| 事務所外観 | — | — | — | Unsplash 差替 | オフィスビル外観（元サイトに建物写真なし） |
| その他装飾 | — | — | — | CSS/SVG | アイコン類は全て SVG／Unicode で代替 |

## 注意事項

- 代表写真 (img40, img42, img44) の扱い：img44 が一番クオリティ高い大判写真。introduction ページの順序では img44 は森谷氏の位置だが、画像を見ると絵画バックの同じ人物に見える。ソース順序通りに配置する（森谷氏の位置）。ただし代表メッセージ欄には img40/42 の小さい写真ではなく「所長挨拶」テキストのみで代表写真を別途使わない。5人並列の税理士紹介セクションでのみ使用する。
- 代表写真 img40: 業務内容カード等の装飾に使わない（不自然なため）。使用しない。
- img42（握手ストック）: 差替対象。
