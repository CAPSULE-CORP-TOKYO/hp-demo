# コンポーネント割当表

## サイト構造
Header / Hero / Intro / Services / Features(8) / Office(representative + facilities) / Access / Contact / Footer + Mobile CTA

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 中島税理士事務所 | ロゴ/タイトル | Header/Footer | そのまま |
| T2 | 茨城県 土浦市・つくば市の税理士事務所 | サブタイトル | Header | そのまま |
| T3 | 中小企業・個人の税務に関するさまざまなサービスを提供しております。会社決算・相続・確定申告・会社設立などでお困りの方はぜひ一度ご相談にお越しください。 | ヒーロー見出し/本文 | Hero | そのまま |
| T4 | 029-821-0568 | 電話番号 | Header/CTA/Footer | そのまま（tel:） |
| T5 | ご相談受付時間：平日9:00～17:30 | 営業時間 | Header/Footer | そのまま |
| T6 | 主な業務内容（4項目：会計・税務 / 相続・贈与 / 確定申告 / 創業・会社設立 + それぞれの一文説明） | サービスカード | Services | そのまま |
| T7 | 中島税理士事務所の8つの特徴（8項目見出し＋本文） | 特徴アコーディオン/カード | Features | そのまま |
| T8 | 業務対象地域段落 + つくばエクスプレス段落 | エリア紹介 | Intro/About | そのまま |
| T9 | 事務所玄関 / 事務所デスク / 打ち合わせルーム | 施設写真キャプション | Office | そのまま |
| T10 | げんき畑関連（福利厚生段落） | 事務所文化 | Office | そのまま |
| T11 | 電車の場合/お車の場合 | アクセス | Access | そのまま |
| T12 | 〒300-0037 茨城県土浦市桜町3-8-7 / TEL / FAX / E-Mail / 営業時間 / 休業日 | コンタクト情報 | Contact/Footer | そのまま |
| T13 | 代表「中島 孝」ご挨拶（事務所概要ページ） | 代表挨拶 | Office | そのまま（該当全文） |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | images/corp-index001.jpg | original | photo | 代表ポートレート | Office | そのまま（images/corp-index001.jpg） |
| 2 | images/corp-index01.jpg | original | photo | 施設カード1 | Office | そのまま（images/corp-index01.jpg） |
| 3 | images/corp-index02.jpg | original | photo | 施設カード2 | Office | そのまま（images/corp-index02.jpg） |
| 4 | images/corp-index03.jpg | original | photo | 施設カード3 | Office | そのまま（images/corp-index03.jpg） |
| 5 | images/corp-index04.jpg | original | photo | げんき畑カード1 | Office | そのまま |
| 6 | images/corp-index05.jpg | original | photo | げんき畑カード2 | Office | そのまま |
| 7 | images/corp-index06.jpg | original | photo | げんき畑カード3 | Office | そのまま |
| 8 | — | — | — | Hero 背景 | Hero | Unsplash（office/business） |
| 9-12 | srv-0[1-4].jpg | stock | — | サービスカード背景 | Services | CSS（SVG アイコン＋グラデーション） |

**統一性ルール**: サービスカード4枚は CSS アイコンで統一。施設カード3枚は original 写真で統一。げんき畑3枚は original 写真で統一。
