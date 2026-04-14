# コンポーネント割当表

## サイト構造
Header / Hero / Greeting / Features / Services / Office / Access / Contact / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 森宏一税理士事務所 | ヘッダーロゴ | Header | そのまま |
| T2 | ごあいさつ / 事業所概要 / 経営支援 / 会計支援 / 税務支援 / 開業支援 | ナビリンク | Header | そのまま |
| T3 | 022-797-1155 | ヘッダー電話番号 | Header | そのまま（tel:リンク） |
| T4 | 歯科 税理士、歯科経営、歯科開業のことなら仙台の森宏一税理士事務所 | ヒーロー見出し | Hero | そのまま |
| T5 | 新規開業のご相談、歯科医院経営のことならお任せください！ | ヒーローサブ | Hero | そのまま |
| T6 | はじめまして、税理士の森 宏一 です。（ごあいさつ） | セクション見出し | Greeting | そのまま |
| T7 | 当事務所は、歯科に特化し...私の一番の仕事であると確信しております。 | 挨拶文 | Greeting | そのまま |
| T8 | "業種に特化することの必要性"＋本文 | ポイントカード1 | Features | そのまま |
| T9 | "ブレーンの必要性"＋本文 | ポイントカード2 | Features | そのまま |
| T10 | "計画的な開業準備の必要性"＋本文 | ポイントカード3 | Features | そのまま |
| T11 | 経営支援＋説明文（gyoumu.html） | サービスカード1 | Services | そのまま |
| T12 | 会計支援＋説明文（gyoumu.html） | サービスカード2 | Services | そのまま |
| T13 | 税務支援＋説明文（gyoumu.html） | サービスカード3 | Services | そのまま |
| T14 | 開業支援＋説明文（gyoumu.html） | サービスカード4 | Services | そのまま |
| T15 | 事務所名〜対応システムまでの事務所概要テーブル（syoukai.html） | 事務所概要テーブル | Office | そのまま |
| T16 | 所在地〜駐車場ありまでのアクセス情報（access.html） | アクセス情報 | Access | そのまま |
| T17 | お問い合わせ相談内容リスト＋電話番号＋注意文 | 問い合わせセクション | Contact | そのまま |
| T18 | Copyright c 森宏一税理士事務所. All Rights Reserved. | フッターコピーライト | Footer | そのまま |
| T19 | gyoumu1.html 経営相談・資金調達・キャッシュフロー経営の詳細 | アコーディオン | Services（経営支援詳細） | アコーディオン |
| T20 | gyoumu2.html 会計支援の詳細 | アコーディオン | Services（会計支援詳細） | アコーディオン |
| T21 | gyoumu3.html 税務支援の詳細 | アコーディオン | Services（税務支援詳細） | アコーディオン |
| T22 | gyoumu5.html 開業支援の詳細＋スケジュール | アコーディオン | Services（開業支援詳細） | アコーディオン |
| T23 | oshirase.html セミナー情報（繁栄している歯科医院の特徴 point1-6） | 別セクション | Insights（コラム） | カード化 |
| T24 | contact.html 個人情報の取扱い | フッター注記 | Footer | そのまま |
| T25 | ご開業をお志す先生へ...少しでも不安がある先生はご相談下さい | CTA バナー | Hero下部 | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 11 | images/syoukai/m_01.png | original | photo | 代表者写真 | Greeting | そのまま |
| 28 | images/gyoumu/vision.png | original | diagram | ビジョン図 | Services（経営支援詳細） | そのまま |
| 32 | images/gyoumu/g_12-c.png | original | diagram | 税務フロー図 | Services（税務支援詳細） | そのまま |
| 34 | images/gyoumu/sch3.jpg | original | diagram | 開業スケジュール | Services（開業支援詳細） | そのまま |
| 40 | images/gyoumu/vision2.png | original | diagram | 仕組み図 | Insights | そのまま |
| 41 | images/gyoumu/vision3.png | original | diagram | 患者接点図 | Insights | そのまま |
| - | Unsplash（税理士事務所/オフィス） | - | - | ヒーロー背景 | Hero | Unsplash差替 |
| - | Unsplash（歯科医院） | - | - | サービスアイコン的装飾 | Services | CSS/SVG代替（アイコン） |

## 不要（使用しない画像）
- #1-9: テキスト焼込のナビ・ヘッダー画像 → CSS/HTMLテキストで代替
- #10: ヒーロー画像（テキスト焼込） → Unsplash差替
- #12-18: テキスト焼込画像 → CSS/HTMLテキストで代替
- #19-27,29-31,33,35-36: テンプレ見出し画像 → CSS代替
- #23-26: 犬のストック写真 → 不要
- #37-39,42: ストック素材写真 → 不要
