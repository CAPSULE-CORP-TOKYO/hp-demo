# 分析結果（L-1959 決算申告サポートセンター郡山）

## アーキタイプ
名前: A モダンミニマル（+ 士業の信頼感を補強）
根拠: 税理士事務所（決算申告特化サポートセンター）。元サイトは2017年頃のグリーン基調 LP テンプレートで、テキスト焼込画像と吹き出しでチラシ感が強い。リデザインでは情報密度を保ちつつ、白基調 + グリーンのアクセントで現代的な士業サイトに刷新する。

## カラーパレット
元サイトのグリーンを継承。
- メイン: #2E7D32（深いグリーン、見出し・アクセント）
- サブ: #66BB6A（明るいグリーン、ハイライト・装飾）
- 背景ベース: #FFFFFF / #F5F8F4（カードや交互背景）
- テキスト: #1F2A24（ほぼ黒）/ #4F5B53（サブテキスト）
- アクセント: #FF8A00（CTA ボタンに集中、暖色アクセント）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../logo.png | original | text-embedded | 差替 | テキストロゴ → HTML テキスト |
| 2 | .../TEL_header.png | original | text-embedded | 差替 | TEL 焼込 → HTML 表示 |
| 3 | .../header-1.jpg | original | photo | そのまま | スタッフ集合写真（淡緑背景）。Hero 用 |
| 4 | .../menu-icon*.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 5 | .../spmenu_*.png | template | icon | CSS/SVG 代替 | スマホ補助アイコン |
| 6 | .../TOP_image.jpg | stock | photo | 差替 | サラリーマン困り顔ストック |
| 7 | .../TOP1.png 〜 TOP4.png | original | text-embedded | 差替 | 緑の見出し焼込画像 → HTML 見出し |
| 8 | .../check.png | template | icon | CSS/SVG 代替 | チェックマーク |
| 9 | .../TEL.png | template | text-embedded | 差替 | 電話番号焼込 |
| 10 | .../ppr_*.png | template | icon | CSS/SVG 代替 | 紙アイコン |
| 11 | .../muryousoudan.jpg | stock | photo | 差替 | 電卓ストック |
| 12 | .../mitsumori.jpg | stock | photo | 差替 | 商談ストック |
| 13 | .../inkan.jpg | stock | photo | 差替 | 印鑑ストック |
| 14 | .../nouzei.jpg | stock | photo | 差替 | 納税ストック |
| 15 | .../staff_.png | original | photo | そのまま | スタッフ集合写真（黒背景） |
| 16 | .../denkyu.png | template | icon | CSS/SVG 代替 | 電球アイコン |
| 17 | .../afterfollow.png | template | photo | 差替 | サポート背景 |
| 18 | .../hissu.png | template | text-embedded | 差替 | 必須ラベル |
| 19 | .../photo_gunji.jpg | original | photo | そのまま | 代表 郡司洋一 |
| 20 | .../photo_gunji_n.jpg | original | photo | そのまま | 郡司紀代 |
| 21 | .../photo_akimoto.jpg | original | photo | そのまま | 秋元郁子 |
| 22 | .../photo_bannai.jpg | original | photo | そのまま | 坂内幸代 |
| 23 | .../photo_takahashi.jpg | original | photo | そのまま | 高橋佳奈 |
| 24 | .../photo_shiraiwa.jpg | original | photo | そのまま | 白岩大輔 |
| 25 | .../photo_konno.jpg | original | photo | そのまま | 紺野 |
| 26 | .../photo_senzaki.jpg | original | photo | そのまま | 先崎 |
| 27 | .../photo_sasagawa.jpg | original | photo | そのまま | 笹川 |

## 引き継ぎ画像（ローカル化対象）
- header-1.jpg
- staff_.png
- photo_gunji.jpg, photo_gunji_n.jpg, photo_akimoto.jpg, photo_bannai.jpg, photo_takahashi.jpg, photo_shiraiwa.jpg, photo_konno.jpg, photo_senzaki.jpg, photo_sasagawa.jpg

## Unsplash 差替方針
- Hero セクションは header-1.jpg を使うため、Unsplash 不要
- 「税理士に依頼するメリット」セクションのアイコンは CSS / SVG / Unicode で統一
- 4 つのプロセスカード（無料相談・見積・必要書類・納税）はテキスト + アイコン構成にしてストック画像置換は不要
