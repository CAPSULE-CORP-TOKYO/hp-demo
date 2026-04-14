# コンポーネント割当表

## サイト構造
Header / Hero / Policy / Services / Company / FAQ / Contact / Access / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 税理士法人 北見会計 | ヘッダーロゴ | Header | そのまま |
| T2 | お客様にとって最も信頼できるパートナーであり続けます | ヘッダーコピー | Header | そのまま |
| T3 | ホーム/業務内容/会社案内/よくある質問/アクセス | ナビメニュー | Header | そのまま |
| T4 | 創業40年 信頼と実績で、未来を支える経営パートナー | ヒーロー見出し | Hero | そのまま |
| T5 | 税務・財務・会計コンサルティング・相続・事業承継など あらゆる専門分野からお客さまをサポートいたします。 | ヒーローサブ | Hero | そのまま |
| T6 | 常にお客さま目線で向き合うことで これからも選ばれ続けます。 | ポリシー見出し | Policy | そのまま |
| T7 | 親切丁寧な対応を評価いただき、お客さまからのご紹介を数多くいただいております。お客さまと真摯に向き合い、深く理解し、未来を見据えたご提案を続けてきました。 | ポリシー本文 | Policy | そのまま |
| T8 | 業務内容 | セクション見出し | Services | そのまま |
| T9 | 会計・税務・財務 / 個人の確定申告、法人の決算・税務申告...すべての業務をお手伝いさせて頂きます。 | サービスカード1 | Services | カード化 |
| T10 | コンサルティング / 資金調達、業務フローの最適化...企業価値を高めるご提案をいたします。 | サービスカード2 | Services | カード化 |
| T11 | 相続・事業承継 / 安心した相続の実現のため...最適なご提案をいたします。 | サービスカード3 | Services | カード化 |
| T12 | 監査 / 会社法監査・学校法人監査...効率よく正確に実施いたします。 | サービスカード4 | Services | カード化 |
| T13 | サービス詳細テキスト（会計・税務・財務 取り扱い業務リスト） | サービス詳細 | Services-detail | アコーディオン |
| T14 | サービス詳細テキスト（コンサルティング 取り扱い業務リスト） | サービス詳細 | Services-detail | アコーディオン |
| T15 | サービス詳細テキスト（相続・事業承継 取り扱い業務リスト） | サービス詳細 | Services-detail | アコーディオン |
| T16 | サービス詳細テキスト（監査 取り扱い業務リスト） | サービス詳細 | Services-detail | アコーディオン |
| T17 | 会社案内 | セクション見出し | Company | そのまま |
| T18 | 代表のごあいさつ + 代表挨拶文 | 代表メッセージ | Company | そのまま |
| T19 | 税理士法人北見会計 代表社員 北見喜隆 | 代表署名 | Company | そのまま |
| T20 | 社員税理士3名の経歴情報（北見喜隆・北見赳夫・北見芳史郎） | メンバーカード | Company | カード化 |
| T21 | 会社概要（名称・所在地・沿革・代表者・税理士法人番号・社員数・有資格者・メール） | 会社概要テーブル | Company | そのまま |
| T22 | 加盟団体 | 加盟団体セクション | Company | そのまま |
| T23 | よくある質問（はじめて税理士をお探しの方 4問 + 相続についてお悩みの方 4問 + その他 1問） | FAQアコーディオン | FAQ | アコーディオン |
| T24 | アクセス情報（日立オフィス・東京オフィス 住所・交通） | アクセスカード | Access | カード化 |
| T25 | お問い合わせ / 日立オフィスへのお電話 0294-23-3966 / 東京オフィスへのお電話 03-6826-2380 / 受付時間：9：00～17：00（土日祝休み） | お問い合わせセクション | Contact | そのまま |
| T26 | メールでのお問い合わせ | メールCTA | Contact | そのまま |
| T27 | フッター情報（ナビ・住所・TEL・コピーライト） | フッター | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | .../img/common/logo03.png | original | photo | ヘッダーロゴ | Header | そのまま |
| 2 | .../img/common/logo04.png | original | photo | フッターロゴ | Footer | そのまま |
| 3 | .../img/office/pic_staff01.jpg | original | photo | 代表写真 | Company | そのまま |
| 4 | .../img/office/pic_staff02.jpg | original | photo | メンバー写真 | Company | そのまま |
| 5 | .../img/home/img_mv01-pc.png | stock | photo | ヒーロー背景 | Hero | Unsplash差替（都市/ビジネス） |
| 6 | .../img/common/img_service01_01.png | stock | photo | サービスカード1 | Services | Unsplash差替（会計/ビジネス） |
| 7 | .../img/common/img_service02_01.png | stock | photo | サービスカード2 | Services | Unsplash差替（コンサル） |
| 8 | .../img/common/img_service03_01.png | stock | photo | サービスカード3 | Services | Unsplash差替（相続） |
| 9 | .../img/common/img_service04_01.png | stock | photo | サービスカード4 | Services | Unsplash差替（監査/ビル） |
| 10 | .../img/common/ico02.png | template | icon | デコレーション | Policy | CSS/SVG代替 |
| 11 | .../img/common/ico_service01-04.png | template | icon | サービスアイコン | Services | CSS/SVG代替 |
| 12 | .../img/home/txt_office02.png | original | text-embedded | 会社案内装飾テキスト | Company | CSSテキストで再現 |
| 13 | .../img/home/img_office01_pc.png | stock | photo | 会社案内背景 | Company | Unsplash差替 |
| 14 | .../img/office/img_bnr01-08.png | original | text-embedded | 加盟団体バナー | Company | そのまま（全8枚） |
