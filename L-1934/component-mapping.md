# コンポーネント割当表 — L-1934 澤村正夫税理士事務所

## サイト構造（1ページ完結）

1. Header（ロゴテキスト + ナビ + TEL）
2. Hero（キャッチコピー + サブ + CTA）
3. About（事務所概要 + 外観写真）
4. Greeting（所長挨拶）
5. Philosophy（経営理念 + 自利利他）
6. Services（業務案内 4カテゴリ）
7. Affiliations（所長経歴 + 所属団体）
8. Contact（住所・電話・メール）
9. Footer

## テキストマッピング

| ID | 元テキスト（出典ページ） | 新コンポーネント | セクション | 処理 |
|----|---|---|---|---|
| T1 | 澤村正夫税理士事務所 (/) | ヘッダーロゴテキスト + Footer | Header / Footer | そのまま |
| T2 | 『経営者と共に考える』という基本スタンスで、日々努力しています。 (/ Hero画像内) | ヒーロー見出し（H1） | Hero | そのまま（焼込画像から原文転記） |
| T3 | 正しい会計帳簿を作成することは経営の基本です。法令に完全準拠した会計帳簿は、法人税や消費税などの適正な申告に役立つだけでなく、会社の社会的信用を築く大前提となります。 (/ Hero画像内) | ヒーローサブテキスト | Hero | そのまま（焼込画像から原文転記） |
| T4 | 事務所概要 / 事務所名 / 所在地 / 電話番号 / FAX番号 / 業務内容（10項目） (/) | 事務所概要テーブル | About | そのまま |
| T5 | 澤村正夫税理士事務所はＴＫＣ全国会会員です／ＴＫＣ全国会は、租税正義の実現をめざし関与先企業の永続的繁栄に奉仕するわが国最大級の職業会計人集団です。／東北税理士会所属 (/) | 所属バッジ | About | そのまま |
| T6 | 所長挨拶 / 私は平成２年に税理士事務所を開設してから今日まで…『むずかしいことをやさしく・やさしいことをふかく・ふかいことをおもしろく』をモットーにがんばります。 (/office) | 所長挨拶ブロック | Greeting | そのまま |
| T7 | 事務所の経営理念について 昔なら決算申告書を作成するだけでも良かったのかも知れません… (/philosophy) | 理念リード文 | Philosophy | そのまま |
| T8 | 「自利利他」の理念の実践とは ＴＫＣ全国会の基本理念である「自利利他」について…(/philosophy 全文) | 理念詳細（折りたたみ可） | Philosophy | そのまま（アコーディオン化） |
| T9 | ＴＫＣ会計人の行動指針 / 1.〜6. 各項目（24項目） (/philosophy) | 行動指針リスト（折りたたみ可） | Philosophy | そのまま（アコーディオン化） |
| T10 | 業務案内 / 会計業務・税務申告だけが税理士業務では有りません。会社発展の全てをサポートするのが澤村正夫税理士事務所です！何でもご遠慮なくご相談ください。 (/service) | サービスリード文 | Services | そのまま |
| T11 | 税務・会計（記帳指導/記帳代行/税務調査立会い/決算業務） (/service) | サービスカード1 | Services | そのまま |
| T12 | 会計業務（月次決算/会計処理/会計システム導入/決算事前対策/節税） (/service) | サービスカード2 | Services | そのまま |
| T13 | 経営コンサルティング業務（資金計画/融資先紹介/経営計画/売上向上/事務合理化/経営管理システム） (/service) | サービスカード3 | Services | そのまま |
| T14 | その他業務（提携企業のご紹介） (/service) | サービスカード4 | Services | そのまま |
| T15 | 所長経歴 平成２年５月　税理士登録／税理士事務所開業／ＴＫＣ全国会入会 (/office) | 経歴リスト | Affiliations | そのまま |
| T16 | 所属団体 日本税理士協同組合連会会 専務理事ほか10件 (/office) | 所属団体リスト | Affiliations | そのまま |
| T17 | お知らせ「お金の計算」当事務所では、お金の計算（税金の計算も含め）を仕事としておりますが…仕事に取り組んでいます。 (/info) | コラム枠 | Greeting 内 | そのまま |
| T18 | 福島県郡山市土瓜１－１９５－２ / 024-961-3200 / 024-961-3828(FAX) / sawamura-masao@tkcnf.or.jp | コンタクト情報 | Contact / Footer | そのまま |
| T19 | 『むずかしいことをやさしく・やさしいことをふかく・ふかいことをおもしろく』 (/office) | モットー（再掲、Hero補助 or Greeting内強調） | Greeting | そのまま |

> seminar / tkc-link / tkc-hozyokin / tkc-tax-calendar / tkc-management-qa / tkc-on-demand001 / tkc-ebooks-invoice / tkc-nensyunokabe 等のサブページは TKC 共通コンテンツ（事務所固有性なし）のため、リデザイン版では除外。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|---|---|---|---|---|---|
| 13 | https://www.tkcnf.com/library/570b87d74351b3167f4e5ae0/5eaa1d6bf29e8a526fb84be9.jpg | original | photo | About 内ビジュアル + Hero 背景候補 | About | **そのまま引き継ぎ** → `images/office-exterior.jpg` |
| 16 | https://www.tkcnf.com/library/570b87d74351b3167f4e5ae0/570cb80768ba6d26220011b6.png | original | text-embedded(書道) | Philosophy 装飾 | Philosophy | **そのまま引き継ぎ** → `images/jiri-rita.png` |
| Hero BG | — | — | — | Hero 背景 | Hero | Unsplash 差替（office/professional 系） |
| その他全画像 | TKC共通テンプレ・ロゴ・トラッキング | template/stock | various | — | — | 不要 / CSS代替 |

### Unsplash 差替候補
- Hero 背景: `https://images.unsplash.com/photo-1554224155-6726b3ff858f` (calculator/desk/office)
- セクション装飾は使わず、CSS 罫線・余白・タイポグラフィで構造を作る（モダンミニマル方針）

## ローカル化必須リスト（Phase 5-0 で curl）
1. `https://www.tkcnf.com/library/570b87d74351b3167f4e5ae0/5eaa1d6bf29e8a526fb84be9.jpg` → `images/office-exterior.jpg`
2. `https://www.tkcnf.com/library/570b87d74351b3167f4e5ae0/570cb80768ba6d26220011b6.png` → `images/jiri-rita.png`
