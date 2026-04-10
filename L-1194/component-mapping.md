# コンポーネント割当表

## サイト構造
Header / Hero / About（企業経営を手厚くサポート）/ Representative（代表紹介）/ Services（6つ）/ Price / FAQ / Office（事務所概要）/ Contact / Footer

## テキストマッピング（要点のみ）

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | いばらき会計税務事務所 | ロゴテキスト | Header | そのまま |
| T2 | 茨城県の皆様を応援する会計税務事務所です | ヘッダータグライン | Header | そのまま |
| T3 | 地元茨城県の中小企業の皆様のために 会計・税務・経営を全力支援いたします！ | ヒーロー見出し | Hero | そのまま |
| T4 | お客様の事業の成長をサポート | ヒーローサブ | Hero | そのまま |
| T5 | ABOUT 企業経営を手厚くサポート + 本文4文 | About セクション | About | そのまま |
| T6 | 代表紹介（中山 和弘 プロフィール＋キャリア＋経歴年表） | 代表セクション | Representative | そのまま |
| T7 | SERVICE01-06（会計・税務、自計化支援、記帳代行、給与計算、相続税申告、コンサルティング） 各説明文 | サービスカード6枚 | Services | そのまま |
| T8 | PRICE 料金表（記帳代行、申告作業、自計化、相続税） | 料金カード | Price | そのまま |
| T9 | FAQ 6件 | アコーディオン | FAQ | アコーディオン |
| T10 | 事務所概要（名称・代表・所在地・TEL・携帯・FAX・事業内容） | 事務所情報テーブル | Office | そのまま |
| T11 | お電話 029-846-0706 受付時間：平日 9:00～18:00 | CTA | Contact + モバイル追従 | そのまま |
| T12 | NEWS 最新3件 | ニュースリスト | News | そのまま |
| T13 | 住所 〒300-0332 茨城県稲敷郡阿見町中央4丁目8-19 ウイングテナント中央2F | アクセス | Office | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | logo-1.png | original | - | - | - | CSS テキストロゴで代替 |
| 2 | mv_pc02-1.jpg | - | text-embedded | ヒーロー背景 | Hero | Unsplash 差替（office/business） |
| 3 | pic_content1.jpg | original | photo | 代表写真 | Representative | **そのまま（ローカル化: images/pic_representative.jpg）** |
| 4 | office_img01.jpg | original | photo | 事務所内観 | Office | **そのまま（ローカル化: images/office.jpg）** |
| 5 | service_top01-06.jpg | stock | photo | サービスカード | Services | CSS アイコン代替（Unicode / SVG）で統一 |
| 6 | access_img01.jpg | stock | photo | - | - | 不要（Google Maps 埋め込みで代替しない → テキストのみ） |
| 7 | faq_img01.jpg | stock | photo | - | FAQ | 不要 |

## メモ
- 統一性: Services の 6 枚はアイコン統一（SVG）
- ヒーロー: Unsplash の business/office 画像でダークオーバーレイ
- Representative 写真は元サイト通り使用
- Office セクションに事務所内観写真を配置
