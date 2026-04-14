# コンポーネント割当表

## サイト構造
- Header / Hero / About（相続の悩み・当事務所の方針） / Services（業務内容） / Souzoku Flow（相続手続きの流れ） / FAQ / Clients（顧問先紹介） / Director（所長紹介） / Contact / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 大原・齋藤会計事務所 | ヘッダーロゴ | Header | そのまま |
| T2 | ホーム / 業務内容 / 相続手続きの流れと当事業所の強み / よくある質問 / 顧問先のご紹介 / お問い合せ | ナビリンク | Header | そのまま |
| T3 | 相続の心配事ご相談ください！ | ヒーロー見出し | Hero | そのまま（元バナーテキストをHTML化） |
| T4 | 相続の悩みや疑問（何から始めれば〜費用はどのくらいか？の4項目） | 悩みリスト | About | そのまま |
| T5 | 大切なご家族が旅立った時〜お気軽にご相談ください。（トップページ本文全体） | メイン訴求テキスト | About | そのまま |
| T6 | 所長紹介〜等幅広くご支援させて頂いております。 | 所長プロフィール | Director | そのまま |
| T7 | 事務所所在地〜makoto-ohara0405@tkcnf.or.jp | 事務所情報 | Director | そのまま |
| T8 | 1.業務案内（相続のご相談）全文 | サービスカード1 | Services | カード化 |
| T9 | 2.業務案内（経営者のお客様、顧問契約先様）全文 | サービスカード2 | Services | カード化 |
| T10 | 3.業務案内（所得税・確定申告のお手伝い）全文 | サービスカード3 | Services | カード化 |
| T11 | お客様の声（相続関連6件） | お客様の声 | Services | カード化 |
| T12 | お客様の声（確定申告3件） | お客様の声 | Services | カード化 |
| T13 | 相続に関するご質問（6問） | FAQ | FAQ | アコーディオン |
| T14 | 顧問契約に関するご質問（4問） | FAQ | FAQ | アコーディオン |
| T15 | 顧問先4社の紹介テキスト全文 | 顧問先カード | Clients | カード化 |
| T16 | 当事務所へのご質問やご要望は下記フォームよりご連絡下さい。 | お問い合わせ説明 | Contact | そのまま |
| T17 | 022-224-0375 / 受付時間 9:00-18:00 [ 土・日・祝日除く ] | CTAバー・フッター | Footer / CTA | そのまま |
| T18 | Copyright大原・齋藤会計事務所 All Rights Reserved. | フッター | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | .../header_logo4.jpg | original | photo | ヘッダーロゴ | Header | そのまま |
| 2 | .../top_banner5.jpg | template | text-embedded | -- | Hero | CSS背景+テキストHTML化 |
| 3 | .../img_oohara.jpg | original | photo | 所長写真 | Director | そのまま |
| 4 | .../souzoku_flow6-scaled.jpg | original | text-embedded | -- | Souzoku Flow | CSS/SVG代替（フローチャートをCSSで再現） |
| 5 | .../img_qa-1024x724.jpg | original | photo | QAセクション装飾 | FAQ | そのまま |
| 6 | .../img_komonsaki01_b.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 7 | .../img_komonsaki01_a.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 8 | .../img_komonsaki02_a-768x1024.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 9 | .../img_komonsaki02_b-768x1024.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 10 | .../img_komonsaki03_a-768x1024.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 11 | .../img_komonsaki03_b-768x1024.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 12 | .../img_komonsaki04_a.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 13 | .../img_komonsaki04_b.jpg | original | photo | 顧問先カード写真 | Clients | そのまま |
| 14 | .../img_contact01-1024x724.jpg | original | photo | お問い合わせ画像 | Contact | そのまま |
