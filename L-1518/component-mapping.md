# コンポーネント割当表

## サイト構造

1. Header（ロゴ + ナビ + TEL）
2. Hero（社名 + キャッチ + CTA）
3. About 概要（事業定義・代表メッセージ）
4. Services（業務内容 11 種 + 認定支援機関）
5. Books（発行書籍のご案内 5 冊）
6. Recruit（人財募集サマリ + 詳細アコーディオン）
7. News（お知らせ + セミナー情報）
8. Office（事務所概要・経営理念・アクセス）
9. Contact（TEL + 問い合わせフォームリンク）
10. Footer
11. Mobile sticky CTA bar（768px 以下）

## テキストマッピング

| ID | 元テキスト | セクション | 処理 |
|----|-----------|-----------|------|
| T1 | 税理士法人AMAGUCHIパートナーズ | Header / Hero / Footer | そのまま |
| T2 | 経営応援団 | Hero サブコピー / Office | そのまま（元サイト「経営応援団」横断バナー + 事業定義文より） |
| T3 | 夢・志を持つと、人は生き生きします。〜いろんな形で応援して行きます。（代表挨拶全文） | About 代表メッセージ | そのまま |
| T4 | 〜 青 春 〜 サムエル・ウルマン（青春の詩） | About 代表メッセージ（アコーディオン折りたたみ） | そのまま（長文なので折りたたみ） |
| T5 | 代表社員 税理士 天口信裕 | About 署名 | そのまま |
| T6 | 月次巡回監査本文 | Services カード 1 | そのまま |
| T7 | 決算前検討会本文 | Services カード 2 | そのまま |
| T8 | 決算申告本文 | Services カード 3 | そのまま |
| T9 | 財務分析本文 | Services カード 4 | そのまま |
| T10 | 経営計画書作成本文 | Services カード 5 | そのまま |
| T11 | 資金繰り本文 | Services カード 6 | そのまま |
| T12 | リスクマネジメント本文 | Services カード 7 | そのまま |
| T13 | 企業継承本文 | Services カード 8 | そのまま |
| T14 | 相続本文 | Services カード 9 | そのまま |
| T15 | 確定申告本文 | Services カード 10 | そのまま |
| T16 | 資産運用本文 | Services カード 11 | そのまま |
| T17 | 認定支援機関本文（経営改善 8 ステップ含む） | Services 認定支援機関ブロック | そのまま |
| T18 | 書籍 5 冊の書名・著者・紹介文 | Books セクション | そのまま |
| T19 | 募集情報（監査担当・税理士 2 職種） | Recruit セクション | そのまま |
| T20 | 応募情報 / 選考プロセス / 連絡先 | Recruit 下部 | そのまま |
| T21 | 事業所概要（商号/所在地/TEL/FAX/創業/所長/従業員数/業務内容） | Office 概要テーブル | そのまま |
| T22 | 経営理念（一、二） | Office 経営理念 | そのまま |
| T23 | お知らせ 4 件（日付 + タイトル） | News お知らせ列 | そのまま（タイトル末尾「･･･」含む原文） |
| T24 | セミナー情報 4 件（日付 + タイトル） | News セミナー列 | そのまま |
| T25 | TEL 023-625-2773 | Header / Contact / Footer / Sticky bar | そのまま（tel: リンク付き） |
| T26 | FAX 023-625-2774 | Office / Contact | そのまま |
| T27 | 〒990-0053 山形県山形市薬師町1丁目16-1 | Contact / Office / Footer | そのまま |
| T28 | 受付時間：9:00〜18:00（土日祝日を除く） | Header 上部 / Footer | そのまま |
| T29 | お問い合わせフォーム → https://amaguchi.com/otoiawase | CTA ボタンリンク | そのまま（外部リンク） |
| T30 | Copyright (C) 税理士法人AMAGUCHIパートナーズ.All Rights Reserved. | Footer 下部 | そのまま |
| T31 | 経営理念の宣言文（山形県一の挨拶と掃除 等） | Office 経営理念 | そのまま |
| T32 | 事業定義=経営応援団 / 企業再生支援業務・医業経営支援業務・増販増客支援センター・財産プランニング協会・人生企画塾 | About 補足 | そのまま |
| T33 | Information / Seminar / お知らせ情報 一覧 / セミナー情報 一覧 | News 見出し | そのまま |

**お知らせ/セミナー記事の個別本文（post-ama4168 等）はメインから除外**（News 一覧の日付＋タイトルのみ掲載）。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 | ローカル名 |
|---|-------|------|------|----------------|-----------|------|-----------|
| 1 | .../logo.jpg | original | photo | ヘッダーロゴ画像 | Header | そのまま | images/logo.jpg |
| 2 | .../gaikan-01.jpg | original | photo | Office 外観写真 | Office | そのまま | images/gaikan-01.jpg |
| 3 | .../DSCF0848-750x520.jpg | original | photo | About ビジュアルアクセント（セミナー会場） | About | そのまま | images/DSCF0848-750x520.jpg |
| 4 | .../2019/01/所長.jpg | original | photo | 代表メッセージ顔写真 | About | そのまま | images/shocho.jpg |
| 5 | .../2015/08/a.jpg | original | photo | 書籍カード 1 | Books | そのまま | images/book-a.jpg |
| 6 | .../2015/08/b.jpg | original | photo | 書籍カード 2 | Books | そのまま | images/book-b.jpg |
| 7 | .../2015/08/c.jpg | original | photo | 書籍カード 3 | Books | そのまま | images/book-c.jpg |
| 8 | .../2015/08/d.jpg | original | photo | 書籍カード 4 | Books | そのまま | images/book-d.jpg |
| 9 | .../2015/08/e.jpg | original | photo | 書籍カード 5 | Books | そのまま | images/book-e.jpg |
| 10 | その他すべて（top_g_b01-b11, gyomu_01-11, 図解画像 等） | template | text-embedded / diagram | — | — | CSS/HTML 代替 | — |
| 11 | top_g_img01/02/03, 汎用写真 | stock | photo | — | — | 不要 | — |

**統一性ルール**: Books セクションは 5 冊とも original 写真で統一。Services カードには画像を使わず、SVG アイコン + テキストのみで構成（11 種の統一性確保）。

## テキスト→コンポーネント割当完全性

- ヘッダナビ: 事務所案内 / 業務案内 / 業務内容 / お知らせ情報 / お役立ち情報 / 採用情報 → サブメニュー含めアンカーリンクで埋め込み（About / Services / News / Office / Recruit）
- 全テキストブロックを上記 T1-T33 に割当済み
- 404 の gyom12 は除外
- お知らせ/セミナー記事の個別本文はメインから除外（News 一覧のタイトル＋日付のみ表示）

## テキスト処理種類の内訳

- そのまま: T1-T33 ほぼ全て
- アコーディオン: T4（青春の詩）、T19-T20（募集情報詳細）
- 別ページ除外: 個別記事本文（post-ama*）

## 画像処理種類の内訳

- そのまま: #1-9（9 点）
- CSS/SVG 代替: ボタン・ナビ・図解・バナー類
- 不要: stock 写真、お知らせ記事内画像
