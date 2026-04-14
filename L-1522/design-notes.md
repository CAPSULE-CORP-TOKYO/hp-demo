# 分析結果

## アーキタイプ
名前: **A: モダンミニマル**（士業の権威性を担保するため B 寄りの要素も混ぜる）
根拠:
- 業種は税理士事務所（山形）。ターゲットは中小企業経営者・農業法人・医療法人・個人事業者など。
- 元サイトは 2012 年リニューアルの水色テンプレートで、サイドバー中心の2カラム構成。情報量は多いが雑多。
- 士業ブランドとして信頼性・落ち着き・誠実さを打ち出す必要がある。
- 現代的に刷新するなら、情報を整理し余白を大きくとるモダンミニマル。見出しに Noto Serif JP を混ぜることで権威感を担保する（士業の「格」）。
- 顧客層は経営者層のため B の伝統重厚寄りも適するが、サービスが多岐にわたるので情報構造を活かせるミニマルベースを選択。

## カラーパレット
- メイン（primary）: `#1a3a6e`（濃紺 — 元サイト水色テンプレートの色相を継承しつつ、彩度を抑え深みを出した士業らしいネイビー）
- サブ（secondary）: `#e8eef5`（非常に淡いブルーグレー — 背景ブロック用）
- アクセント（accent）: `#c79a2b`（落ち着いた金・真鍮色 — 士業の権威を表現。CTA に集中）
- 基調（base）: `#ffffff`（白）
- テキスト（text）: `#1a2333`（濃紺寄りのダーク）/ `#5a6678`（サブテキスト）
- 区切り（border）: `#d8e1ec`

**色相継承**: 元サイトの水色系（≈ #3c8fdb）の hue を保ちつつ、明度を下げて濃紺（#1a3a6e）へ。金アクセントは新規導入だが、税理士の公的資格ブランド（士業）と整合する。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガーアイコン |
| 2 | /library/.../201603041145_pW0fx.jpg | original | text-embedded | 差替（ロゴに統合不可、Unsplash 差替） | 「山形県五十鈴の奥山享税理士事務所」ロゴ画像。ヘッダー帯 |
| 3 | /library/.../201603041145_l14RN.png | original | text-embedded | 差替（HTML 再現） | 電話番号焼込（TEL 023-641-8596） |
| 4 | /library/.../5721bf20e77a4f5f592fbe5d.jpg | template | text-embedded | 差替 | ISO9001 バナー（テキスト焼込） |
| 5-8 | /library/.../5721bf2*.gif | template | text-embedded | 差替（実績テキストで代替） | 出演告知・M&A・bizup バナー等 |
| 9 | /material/lib02/tkc_logo1.gif | template | icon | CSS/SVG 代替 | TKC ロゴ（認定情報はテキスト化） |
| 10 | /library/.../5721ce0a3209ae3d6b8137fc.jpg | template | text-embedded | 差替 | JPBM DailyNews バナー |
| 11 | /library/.../571787882fd8cc9211002026.jpg | original | text-embedded | 差替 | 代表奥山氏+「山形放送・ラジオでおなじみの奥山です」テキスト焼込 |
| 12 | /library/.../5717878a2fd8cc9211002027.jpg | original | text-embedded | 差替 | 事務所外観+テキスト焼込 |
| 13 | /library/.../5717878b2fd8cc9211002028.jpg | stock | text-embedded | 差替 | 都市ビル ストック+テキスト焼込 |
| 14-34 | /library/.../57178...jpg 系 | template | text-embedded | 差替 | スライダーバナー各種（全てテキスト焼込） |
| 35-41 | /material/lib03/bnr_*.png, /design/images/bnr-fixed/* | template | text-embedded | 差替 | TKC 固定バナー類 |
| 43 | /library/.../571787a12fd8cc9211002038.jpg | **original** | **photo** | **そのまま引き継ぎ** | **代表 奥山亨氏の顔写真（純写真、テキストなし）。/office ページ** |
| 44 | /library/.../575f77c4e207da715033cc92.png | original | text-embedded | 差替（HTML 再現） | 「奥山 亨 OKUYAMA TORU」名前ロゴ |
| 45 | /library/.../571787a42fd8cc921100203a.png | original(?) | text-embedded | 差替 | 「自利利他」画像（HTML で再現） |
| 46 | /library/.../571787a52fd8cc921100203b.png | template | text-embedded | 差替 | 「わたしたちにお任せください！」 |
| 47 | /library/.../571787a72fd8cc921100203c.jpg | template | text-embedded | 差替（Google Maps 埋め込み代替不可→地図画像も除外、住所のみ） | /map の地図画像 |
| 48-147 | 各 free ページのバナー等 | template/stock | text-embedded | 差替 | サービス個別バナー群 |

**処理方針サマリ**:
- **引き継ぐ画像（ローカル化）**: 画像 43（代表 奥山亨氏の顔写真）1 枚のみ。純写真で価値が高い。
- **差替方針**: 士業のヒーローは建物外観/街並み/書類などオフィス系 Unsplash 画像で統一。各サービスアイコンは Unicode/SVG で代替（統一性を保つ）。
- **CSS/SVG 代替**: ナビアイコン、サービスアイコン、ソーシャルアイコン、TKC 認定バッジ（テキスト表示）。

## フォント方針
- メイン: **Noto Sans JP**（本文・UI）
- 見出しアクセント: **Noto Serif JP**（h1, h2, キャッチコピー）→ 士業の権威感を出す
