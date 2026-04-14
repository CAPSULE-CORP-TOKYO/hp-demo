# 分析結果

## アーキタイプ

**名前**: A（モダンミニマル） + B（伝統重厚）のハイブリッド

**根拠**:
- 業種: 税理士（士業）→ 信頼・権威を訴求する必要
- 文体: 「お客様に寄り添って」「親身に」など、堅苦しすぎず親しみのあるトーン
- 顧客層: 地方（山形市）の個人・中小企業、特に不動産相続ニーズ
- 情報量: 中程度。業務説明・代表経歴・FAQ・流れなど読み物要素あり
- 強み訴求: 「不動産に強い」「代表自らが不動産投資家」という明確な差別化ポイント
- 元サイト: 余白が効いたカードレイアウト、数字 01-06 のセクション番号、緑基調

→ モダンミニマルをベースに、見出しに明朝体(Noto Serif JP)を混ぜて士業らしい格調を付与する。元サイトの「お客様に寄り添って」という親しみやすさは継承しつつ、情報階層をクリアに整える。

## カラーパレット

元サイトは深い緑（濃緑 #1F3A28 付近）+ 温かみのあるクリーム/ベージュ背景 + 白で構成されている。

- **メイン**: `#1F3A28`（深緑。ヘッダー背景・フッター・見出し強調）
- **サブ**: `#F5F1E8`（クリームベージュ。セクション背景）
- **アクセント**: `#C9A961`（ゴールド寄りのベージュ。CTA・見出しの装飾）
- **テキスト**: `#2B2B2B`（本文）/ `#6B6B6B`（サブテキスト）
- **白**: `#FFFFFF`（カード背景）

60-30-10: 白/クリーム 60%、深緑 30%、ゴールド 10%

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../img/logo.png | original | text-embedded | そのまま | 会社ロゴ。text-embeddedだがロゴは例外で引き継ぎ |
| 2 | .../img/index/mv_01.jpg | original | photo | そのまま | 代表写真（メインビジュアル）。hero 用 |
| 3 | .../ph_index_01-1.jpg | original? | photo | 差替 | 賃貸マンション。文脈不明瞭、汎用感あり |
| 4 | .../ph_index_02-1.jpg | original | photo | そのまま | 玄関写真。理念セクションの添景に |
| 5 | .../ph_index_03.jpg | original | photo | そのまま | 事務所の看板。About セクション |
| 6 | .../ico_arrow_right_01.png | stock | icon | CSS/SVG 代替 | 矢印アイコン |
| 7 | .../ph_index_04.jpg | stock | photo | 差替 | 書類と手の汎用ストック |
| 8 | .../ph_index_05-1.jpg | original | photo | そのまま | 和風の応接テーブル（事務所内観） |
| 9 | .../ph_index_06.jpg | stock | photo | 差替 | FAQとペンの汎用ストック |
| 10 | .../foot_logo.png | original | text-embedded | そのまま | フッター用ロゴ（logo.png と統合可） |
| 11 | .../reloclub_logo.jpg | template | text-embedded | 不要 | RELO CLUB 提携バッジ。再利用しない |
| 12 | .../mv_about_01.jpg | template | photo | 不要 | About ページ MV（テンプレ背景） |
| 13 | .../ph_about_greeting_01.jpg | original | photo | そのまま | 代表写真（和装背景）。About セクション |
| 14 | .../refusal.png | template | icon | 不要 | 断りマーク。使わない |
| 15-20 | .../ph_work_*.jpg | stock | photo | 差替 | 業務紹介用の汎用ストック（高層ビル、家模型、書類、PC等） |
| 21-31 | 各ページ mv_*.jpg / noimage.png | template | any | 不要 | 下層ページのヘッダー装飾背景等 |

**引き継ぐ画像（ローカル化対象）**:
- logo.png （ヘッダー/フッター両方で使用）
- mv_01.jpg → hero-main.jpg にリネーム
- ph_index_02-1.jpg → entrance.jpg
- ph_index_03.jpg → office-sign.jpg
- ph_index_05-1.jpg → reception-room.jpg
- ph_about_greeting_01.jpg → representative.jpg

**差替は Unsplash 画像を使用**（士業系: office/desk/document/building 系）。
