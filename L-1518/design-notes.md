# 分析結果

## アーキタイプ

名前: **A: モダンミニマル**（+ E: テキストヘビー 寄り）

根拠:
- 業種は税理士法人。士業・コンサル領域。権威性・信頼性を表現しつつ、情報量（11 業務・認定支援・事務所概要・募集情報）が多く、テキストヘビーな読み物構成にも対応が必要。
- 元サイトは 2015-2018 年頃の WordPress で、青ベースの堅い配色・画像ボタン主体・情報ぎっしりのレイアウト。ブランドアイデンティティ（AMAGUCHI ロゴの赤）と信頼感（青）を残しつつ、現代的な余白・タイポ・セクション分割にリデザインする。
- 顧客層は中小企業経営者・医業経営者・相続相談者。落ち着き + 読みやすさが重要。
- → モダンミニマルをベースに、必要箇所で縦長の情報カード/アコーディオン的な構成を挿入。

## カラーパレット

元サイト screenshot.png の色相を継承。

- **メイン**: `#0B3A6B`（ネイビーブルー / 信頼・士業らしさ、元サイトのヘッダ紺を踏襲して明度調整）
- **サブ**: `#1E6FB8`（ミッドブルー / 業務ボタン・アクセントバーの青を踏襲）
- **アクセント**: `#C8222F`（AMAGUCHI ロゴの赤 / CTA ボタンに集中）
- **背景**: `#FFFFFF` / `#F5F7FA`（淡グレー）
- **テキスト**: `#1A1A1A` / `#555`（セカンダリ）
- **ボーダー**: `#E4E8EE`

60-30-10:
- 60%: 白 + 淡グレー背景
- 30%: ネイビー/ミッドブルー（ヘッダ、見出し下線、リンク）
- 10%: 赤（CTA ボタン、電話番号強調）

## フォント

- 見出し: **Noto Serif JP**（700） — 権威性・士業の落ち着き
- 本文 / UI: **Noto Sans JP**（400/500/700）
- 業種は現代的な士業なので「伝統重厚」までは振らず、見出しのみ明朝にして本文はサンセリフ。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../themes/ama/img/logo.jpg | original | photo(ロゴ) | そのまま | 社名ロゴ 400x99、赤丸 AMAGUCHI マーク |
| 2 | .../themes/ama/img/tel.jpg | template | text-embedded | CSS 代替 | TEL 番号焼込、HTML で再現 |
| 3-9 | .../themes/ama/img/b01-b07.jpg | template | text-embedded | CSS 代替 | 画像ナビ（事務所案内等） |
| 10 | .../uploads/2024/05/gaikan-01.jpg | original | photo | そのまま | 事務所外観（黄色い建物、経営応援団の垂れ幕） |
| 11 | .../uploads/2017/09/DSCF0848-750x520.jpg | original | photo | そのまま | 年末提言セミナー会場写真 |
| 12 | .../themes/ama/img/top_mykomon.jpg | template | text-embedded | CSS 代替 | Mykomon バナー、テキスト焼込 |
| 13 | .../themes/ama/img/top_igyoshien.jpg | template | text-embedded | CSS 代替 | 「認定支援機関」焼込、握手写真 |
| 14 | .../themes/ama/img/top_g_title.jpg | template | text-embedded | CSS 代替 | 「業務内容」見出し焼込 |
| 15 | .../themes/ama/img/top_g_img01.jpg | stock | photo | 差替 | ダルマ画像、汎用ストック |
| 16-26 | .../themes/ama/img/top_g_b01-b11.jpg | template | text-embedded | CSS 代替 | 業務ボタン（11 種） |
| 27 | .../themes/ama/img/top_g_img02.jpg | stock | photo | 差替 | 汎用 |
| 28 | .../themes/ama/img/top_g_img03.jpg | stock | photo | 差替 | 汎用 |
| 29 | .../uploads/2020/04/bnr_useful011.png | template | text-embedded | CSS 代替 | お役立ちバナー |
| 30 | .../themes/ama/img/new.gif | template | icon | CSS 代替 | NEW バッジ |
| 31 | .../themes/ama/img/top_sidebn01.jpg | template | text-embedded | CSS 代替 | スタッフブログバナー |
| 32 | .../themes/ama/img/top_sidebn02.jpg | template | text-embedded | CSS 代替 | 人財募集バナー |
| 33 | .../themes/ama/img/top.gif | template | icon | CSS 代替 | トップへ戻る |
| 34 | .../themes/ama/img/footer_title.jpg | template | text-embedded | CSS 代替 | 「天口会計事務所」フッタ焼込 |
| 35-38 | .../themes/ama/img/footer_*.jpg | template | text-embedded | CSS 代替 | フッタバナー群 |
| 39 | .../themes/ama/img/footer_bnimg01.jpg | template | text-embedded | CSS 代替 | アルファコム |
| 40-41 | .../themes/ama/img/footer_bnimg02-03.jpg | template | text-embedded | CSS 代替 | 関連会社バナー |
| 42 | .../uploads/2019/11/caption1.gif | template | text-embedded | CSS 代替 | 「ご挨拶」見出し焼込 |
| 43 | .../uploads/2019/01/所長.jpg | original | photo | そのまま | 代表 天口信裕 顔写真 |
| 44 | .../uploads/2015/08/caption2.gif | template | text-embedded | CSS 代替 | 「発行書籍のご案内」見出し焼込 |
| 45 | .../uploads/2015/08/a.jpg | original | photo | そのまま | 書籍表紙「企業承継の考え方と実務」 |
| 46 | .../uploads/2015/08/b.jpg | original | photo | そのまま | 書籍表紙「医業経営支援のスペシャリスト」 |
| 47 | .../uploads/2015/08/c.jpg | original | photo | そのまま | 書籍表紙「会社と社員が元気になる 実践経営計画」 |
| 48 | .../uploads/2015/08/d.jpg | original | photo | そのまま | 書籍表紙「税理士がホンネで語る 税務調査の急所」 |
| 49 | .../uploads/2015/08/e.jpg | original | photo | そのまま | 書籍表紙「さあ会社を起こそう」 |
| 50-60 | .../uploads/2015/12/gyomu_01-11.jpg | template | text-embedded | CSS 代替 | 青色業務ボタン（11 種）、HTML ボタンで再現 |
| 61 | .../uploads/2015/10/jyunkai1.jpg | template | diagram (text-embedded) | CSS 代替 | 巡回審査の必要性図解、HTML で再現可能 |
| 62 | .../uploads/2015/10/img011.jpg | template | diagram (text-embedded) | CSS 代替 | 決算前検討会フロー図、HTML で再現可能 |
| 63 | .../uploads/2015/10/kessan.jpg | template | diagram (text-embedded) | CSS 代替 | 決算の流れ step1-3 図解 |
| 64-71 | .../uploads/2015/10/{zaimu,kaieikeikaku,shikinkuri,img031,kigyosyokei,souzoku,kakutei,img02}.jpg | template | diagram (text-embedded) | CSS 代替 | 各業務ページの図解、HTML で再現 |
| 72-74 | .../themes/ama/img/oyakudachi_01-03.jpg | template | text-embedded | CSS 代替 | お役立ちページバナー |
| 75 | .../uploads/2015/10/recruit_bnr.jpg | template | text-embedded | CSS 代替 | 募集バナー |
| 76 | https://s.w.org/.../27a1.svg | template | icon | CSS 代替 | 矢印絵文字 |
| 77-84 | お知らせ記事内画像 | — | — | 不要 | お知らせ記事は概要のみ掲載、画像は引き継がない |

## 引き継ぎ画像一覧（ローカル化対象、Phase 5-0 で download）

1. `logo.jpg` — AMAGUCHI ロゴ
2. `gaikan-01.jpg` — 事務所外観
3. `DSCF0848-750x520.jpg` — セミナー会場写真
4. `所長.jpg` — 代表者写真（ファイル名日本語 → `shocho.jpg` にリネーム）
5. `a.jpg` → `book-a.jpg`
6. `b.jpg` → `book-b.jpg`
7. `c.jpg` → `book-c.jpg`
8. `d.jpg` → `book-d.jpg`
9. `e.jpg` → `book-e.jpg`

計 9 点。
