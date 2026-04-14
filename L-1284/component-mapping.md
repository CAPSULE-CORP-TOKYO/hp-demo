# コンポーネント割当表

## サイト構造
Header / Hero / About（代表あいさつ+強み） / Services（3法人サービス概要） / Staff（専門家紹介） / Testimonials（お客様の声） / Offices（オフィス紹介） / Recruitment（採用情報 - アコーディオン） / Contact / Footer

## テキストマッピング

| ID | 元テキスト（先頭30字） | 新コンポーネント | セクション | 処理 |
|----|----------------------|----------------|-----------|------|
| T1 | みらいプロシーズグループ | ヘッダーロゴテキスト | Header | そのまま |
| T2 | トップページ / グループ案内 / サービス案内 / お客様の声 / お問合せ / 社内活動 | ナビメニュー | Header | そのまま |
| T3 | 人と人とのつながりを大切に、皆様に満足... | ヒーロー見出し | Hero | そのまま |
| T4 | 専門サービスを素早く、ワンストップで提供... | ヒーローサブテキスト | Hero | そのまま |
| T5 | ワンストップサポートでお客様の業務を円滑に... | About 見出し+本文 | About | そのまま |
| T6 | 代表社員・CEOの小山と申します... | 代表あいさつ | About | そのまま |
| T7 | グループ内で複数の専門サービスを... | 強み説明 | About | そのまま |
| T8 | 経営理念 一．私たちはお客様にとって... | 経営理念 | About | そのまま |
| T9 | 税理士法人みらいプロシーズ サービス提供方針... | サービスカード（税理士） | Services | カード化 |
| T10 | 社会保険労務士法人みらいプロシーズ サービス提供方針... | サービスカード（社労士） | Services | カード化 |
| T11 | 行政書士法人みらいプロシーズ サービス提供方針... | サービスカード（行政書士） | Services | カード化 |
| T12 | Ⅰ税務・会計・経営支援〜Ⅴ相続・贈与 | 税理士サービス詳細 | Services | アコーディオン |
| T13 | ①労働保険・社会保険〜⑤雇用助成金申請 | 社労士サービス詳細 | Services | アコーディオン |
| T14 | ①法人設立〜⑤その他 | 行政書士サービス詳細 | Services | アコーディオン |
| T15 | 報酬一例（税理士/社労士/行政書士 全テーブル） | 料金表 | Services | アコーディオン |
| T16 | 小山 智 代表社員・CEO... | 専門家カード | Staff | カード化 |
| T17 | 君嶋 大輔 社員税理士... | 専門家カード | Staff | カード化 |
| T18 | 渡邉 秀世 社員税理士... | 専門家カード | Staff | カード化 |
| T19 | 清水 尋子 社員社会保険労務士... | 専門家カード | Staff | カード化 |
| T20 | グループ沿革（2016年〜2025年） | 沿革タイムライン | About | アコーディオン |
| T21 | 有限会社日立断熱工事 様 お客様の声... | お客様の声カード1 | Testimonials | カード化 |
| T22 | しどり園芸 様 お客様の声... | お客様の声カード2 | Testimonials | カード化 |
| T23 | 宮部接骨院 様 お客様の声... | お客様の声カード3 | Testimonials | カード化 |
| T24 | 水戸オフィス/茨城町オフィス/日立オフィス 住所・TEL | オフィス情報カード | Offices | カード化 |
| T25 | 採用情報（正社員税理士法人/社労士法人/パート） | 採用情報 | Recruitment | アコーディオン |
| T26 | 福利厚生制度（①退職金〜⑤レクリエーション） | 福利厚生 | Recruitment | アコーディオン |
| T27 | 社内活動（ランニングクラブ） | 社内活動 | Activities（Footer付近） | カード化 |
| T28 | お名前/メールアドレス/電話番号/お問合せ | お問合せフォーム | Contact | そのまま |
| T29 | Copyright (C) 2020 Mirai Proceeds... | フッター | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | images/logo5.jpg | original | text-embedded | ヘッダーロゴ | Header | そのまま |
| 11 | images/blanding.jpg | original | text-embedded | ヒーロー背景 | Hero | Unsplash 差替（日本の街並み/ビジネス） |
| 14 | images/t04.jpg | original | diagram | ワンストップ図 | About | そのまま |
| 18 | images/logo6.jpg | original | text-embedded | フッターロゴ | Footer | そのまま |
| 20 | images/s00-1.jpg | original | photo | 代表写真 | About/Staff | そのまま |
| 21 | images/s05.jpg | original | photo | 君嶋税理士写真 | Staff | そのまま |
| 22 | images/s06.jpg | original | photo | 渡邉税理士写真 | Staff | そのまま |
| 23 | images/s04.jpg | original | diagram | 清水社労士イラスト | Staff | そのまま |
| 27 | images/mo07.jpg | original | photo | 水戸オフィス外観 | Offices | そのまま |
| 29 | images/mo03.jpg | original | photo | 茨城町オフィス | Offices | そのまま |
| 32 | images/io07.jpg | original | photo | 日立オフィス | Offices | そのまま |
| 37 | images/ho01.jpg | original | photo | グループ集合写真 | About | そのまま |
| 41 | images/u06.jpg | original | photo | お客様の声1写真 | Testimonials | そのまま |
| 43 | images/u01.jpg | original | photo | お客様の声2写真 | Testimonials | そのまま |
| 45 | images/u04.jpg | original | photo | お客様の声3写真 | Testimonials | そのまま |
| 47 | images/s10.jpg | original | photo | 社内活動写真 | Activities | そのまま |
| 50 | images/s08.jpg | original | diagram | 齊藤イラスト | Activities | 不要 |
| 2-10 | t01-t09.gif, m01-m06.gif | template | text-embedded/icon | — | — | CSS/SVG 代替 |
| 12 | images/blanding-under04.png | original | text-embedded | — | — | CSS/SVG 代替（テキストでカード化） |
| 13,19 | point.gif, point2.gif | template | icon | — | — | CSS/SVG 代替 |
| 15-17 | t10-t12.jpg | stock | text-embedded | — | — | 不要 |

## 引き継ぎ画像一覧（Phase 5-0 でローカル化必須）

1. logo5.jpg - ヘッダーロゴ
2. t04.jpg - One Stop Support 図
3. logo6.jpg - フッターロゴ
4. s00-1.jpg - 代表 小山智
5. s05.jpg - 君嶋大輔
6. s06.jpg - 渡邉秀世
7. s04.jpg - 清水尋子（イラスト）
8. mo07.jpg - 水戸オフィス外観
9. mo03.jpg - 茨城町オフィス
10. io07.jpg - 日立オフィス
11. ho01.jpg - グループ集合写真
12. u06.jpg - しどり園芸写真
13. u01.jpg - 日立断熱工事写真
14. u04.jpg - 宮部接骨院写真
15. s10.jpg - マラソン大会写真
