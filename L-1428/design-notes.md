# 分析結果 — L-1428 ㈲扇谷会計事務所

## アーキタイプ

名前: **B: 伝統重厚** + **E: テキストヘビー** のハイブリッド（主軸は B）

根拠:
- 業種: 公認会計士・税理士事務所（石巻の老舗、1986年開業、代表は1954年生）。士業の中でも「権威・信頼」を強く求める層。
- 文体: 代表の一人称による長文のご挨拶、「社是」「陶冶」「研鑽」等の重厚な語彙、業務内容の詳細解説。文学的で熟考型。
- 情報量: 代表プロフィール、業務内容(11ページ)、アクセス、お問合せと非常に情報量が多い。読み物としての価値あり。
- 強み訴求: 「単なる書類作成屋にはなりません」「行動の伴わぬ会計評論家にはなりません」「最適な会計情報の提供を通じて会社発展に寄与します」の3本柱を打ち出している。
- よって Noto Serif JP を主軸にした伝統重厚アーキタイプが適切。情報量を活かすため、読み物セクションはテキストヘビー寄りのレイアウトを採用する。

## カラーパレット

元サイトは biz-vektor テーマのデフォルト（黄色 #f7d700 系ヘッダー + 白背景 + 黒文字 + 緑アクセント）。色相をそのまま使うと黄色がテンプレ臭を強めるため、士業にふさわしい「落ち着いた深緑 + 金(黄土寄り)」に調整する。色相は元サイトの「黄緑〜黄色」を引き継ぎ、明度・彩度のみ深める。

- メインカラー（primary）: `#0f3b2e`（深緑 / 信頼・品格）
- サブカラー（secondary base）: `#f8f5ec`（温かみのあるアイボリー / ベース背景）
- アクセントカラー: `#c8a24b`（アンティークゴールド / CTA・見出しライン）
- テキスト: `#1f1f1f`（墨）／サブテキスト `#555`
- ボーダー: `#e5dfc9`

60-30-10: アイボリー 60% / 深緑 30% / ゴールド 10%

## フォント

- 見出し: **Noto Serif JP**（weight 500-700）
- 本文: **Noto Sans JP**（weight 400-500）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /2016/05/01.png | original | text-embedded | 差替 | 「単なる書類作成屋にはなりません」焼込 → HTML 見出しで表現 |
| 2 | /2016/05/02_02.png | original | text-embedded | 差替 | 「行動の伴わぬ会計評論家にはなりません」焼込 → HTML 見出しで表現 |
| 3 | /2016/05/03.png | original | text-embedded | 差替 | 「最適な会計情報の提供を通じて会社発展に寄与します」焼込 → HTML 見出しで表現 |
| 5 | /2026/04/2026年4月投稿-scaled.jpg | original | photo | そのまま引き継ぎ | 顧問先写真部 今月の１枚（桜） |
| 6-11 | pr01.png/pr02.png/pr03.png | template | text-embedded | 差替 | biz-vektor テンプレのリンクアイコン画像 |
| 12-14 | biz-calendar/*.png | template | icon | 不要 | 営業日カレンダー自体を不採用 |
| 15 | bnr_contact_ja.png | template | text-embedded | 差替 | テンプレバナー |
| 16 | footer_pagetop.png | template | icon | CSS/SVG 代替 | PAGETOP 矢印 |
| 17 | daihyo-150x150.jpg | original | photo | そのまま引き継ぎ | 代表 扇谷雄哉の顔写真 |
| 18 | themes/biz-vektor/images/bt_contact_ja.png | template | text-embedded | 差替 | テンプレバナー |
| 19 | /2016/03/事務所風景2_R-300x225.jpg | original | photo | そのまま引き継ぎ | 事務所風景 |
| 20 | /2016/03/事務所風景3_R-300x225.jpg | original | photo | そのまま引き継ぎ | 事務所風景 |
| 21-30, 32-52 | work/*/サブページ画像 | 混在（一部stock/一部original） | photo/text-embedded | 差替 | 統一性のため、業務カードの画像は使わず CSS/ピクトグラムで統一 |
| 53 | /2016/03/連絡先_R-300x225.jpg | original | photo | そのまま引き継ぎ | アクセスの地図代替写真 |
| 54-80 | マイコレクション/エッセイ配下画像 | original（趣味） | photo/diagram | 不要 | 業務サイト本体では使用しない。趣味コレは Off-topic なので除外 |

### 引き継ぎ画像リスト（Phase 5-0 でローカル化する対象）

| ファイル名 | URL |
|---|---|
| sakura-2026-04.jpg | http://cpaogiya.co.jp/wp/wp-content/uploads/2026/04/2026年4月投稿-scaled.jpg |
| daihyo.jpg | http://cpaogiya.co.jp/wp/wp-content/uploads/2016/03/daihyo-150x150.jpg |
| office-01.jpg | http://cpaogiya.co.jp/wp/wp-content/uploads/2016/03/事務所風景2_R-300x225.jpg |
| office-02.jpg | http://cpaogiya.co.jp/wp/wp-content/uploads/2016/03/事務所風景3_R-300x225.jpg |
| access-location.jpg | http://cpaogiya.co.jp/wp/wp-content/uploads/2016/03/連絡先_R-300x225.jpg |

### 業務カード（11 サービス）の画像方針

原サイトでは各サービスに小サムネイルが付いているが、出自が stock/original 混在で統一感がない。新デザインでは **CSS で作るアイコンボックス（ゴールドの細線枠 + Noto Serif JP のナンバリング）** を使用して統一する。画像なし。
