# 分析結果

## アーキタイプ
名前: B 伝統重厚 + E テキストヘビーのハイブリッド（B 主体）
根拠:
- 士業（公認会計士・税理士）。福島県郡山市の地域密着、昭和61年登録の老舗。
- コンテンツが「経理の窓・税務の壷」など長文の自筆コラム中心で、所長の「読み物」志向が強い。
- 単なるモダンミニマルではなく、明朝体ベースで「老舗の信頼感」を演出するのが適切。
- 一方、料金表・派遣監査・コラムなど情報量が多いので、テキストを丁寧に読ませる構造（E）も併用。

## カラーパレット
- メイン（深い藍色 / ネイビー）: #1a3a5f
- サブ（金茶系アクセント）: #b88339
- ベース: #faf8f3（オフホワイト和紙系）
- テキスト: #2a2a2a
- 補助グレー: #6b6b6b
- ボーダー: #e3ddd0

元サイトは赤茶系の見出しと白背景、シンプルな文字主体だったので、色相は自由度が高い。
士業・伝統系のイメージを担保するために、信頼感のあるネイビー + 金茶アクセントの和モダン配色を採用。

## フォント
- 見出し: Noto Serif JP（伝統・権威感）
- 本文: Noto Sans JP（可読性）
- 重要見出しと本文を明確に書き分ける

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | dango.gif | template/外部 | text-embedded | 不要 | 外部広告（藤菜美） |
| 2 | fmgig_banner.gif | template/外部 | text-embedded | 不要 | FM 局バナー |
| 3 | logo_nomap.gif | template/外部 | text-embedded | 不要 | SimulRadio バナー（外部サービス） |
| 4 | ad.jp.ap.valuecommerce.com (×2) | template/外部 | icon | 不要 | アフィリエイト広告 |
| 5 | i.imgvc.com / a.imgvc.com | template/外部 | icon | 不要 | 外部広告 |
| 6 | eki.gif | original? | photo | 不要 | 郡山駅前の古い街並み写真。画質低・古い |
| 7 | hisashi220830-30.jpg | original | photo | **そのまま引き継ぎ** | **所長 橋本寿氏 の顔写真**。最重要素材 |
| 8 | f-counter.net | template/外部 | icon | 不要 | アクセスカウンター |
| 9 | kobito_c.gif / kobito_d.gif | template/外部 | icon | 不要 | 汎用キャラクター素材 |
| 10 | www20.a8.net / www11.a8.net | template/外部 | icon | 不要 | アフィリ広告 |
| 11 | maru.gif | template | icon | CSS/SVG 代替 | 緑色の小さい丸印（リスト bullet） |
| 12 | mapimg.gif | original | diagram | **そのまま引き継ぎ** | 事務所所在地のマップ画像（手描き地図） |
| 13 | yayoi.jpg | template/ベンダー | text-embedded | 不要 | 弥生会計の商品画像（商標問題あり） |
| 14 | freee.png | template/ベンダー | text-embedded | 不要 | freee の商品画像 |
| 15 | mfc.jpg | template/ベンダー | text-embedded | 不要 | マネーフォワード商品画像 |
| 16 | obc.jpg | template/ベンダー | text-embedded | 不要 | 勘定奉行商品画像 |
| 17 | pcac.jpg | template/ベンダー | text-embedded | 不要 | PCA会計商品画像 |
| 18 | price.jpg | original | text-embedded | **HTMLテーブルで再現** | 料金表（記帳代行/自計化/決算申告のみ）を HTML 表に書き起こし |
| 19 | price2.jpg | original | text-embedded | **HTMLテーブルで再現** | 料金表（年末調整等の追加料金）を HTML 表に書き起こし |
| 20 | gava.jpg | original | diagram (text-embedded) | **HTMLテーブルで再現** | 法人統治機構比較表 |

### ローカル化対象（images/ にダウンロードする画像）
- `hisashi220830-30.jpg` → `images/hashimoto-cpa.jpg`（所長写真。プロフィール / About セクションで使用）
- `mapimg.gif` → `images/mapimg.gif`（アクセスマップ画像。Access セクションで使用）

### Hero ビジュアル
- 元サイトには Hero に使える「事務所外観」「事務所内観」写真がない
- 所長写真は About セクションで使用するため Hero には使わない
- Hero 背景は Unsplash の「office / business / Japan」系の落ち着いた写真を使用、または CSS グラデーション + 装飾で構成
- 採用方針: Unsplash の office desk 系の落ち着いた写真を Hero 背景にし、上にネイビー透過オーバーレイ
