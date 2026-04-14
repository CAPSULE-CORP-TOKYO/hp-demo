# コンポーネント割当表

## サイト構造
- Header（ロゴ + ナビ + TEL）
- Hero（スライドショー風ヒーロー + キャッチコピー）
- News（新着情報）
- About（法人会の概要・沿革）
- Services（主要事業: セミナー・福利厚生・税務コンプライアンス・労務相談・健診）
- Membership（入会案内・メリット・会費）
- Members（会員紹介 - アコーディオン）
- Contact（お問合せ・アクセス）
- Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 公益社団法人 日立法人会 | ヘッダーロゴテキスト | Header | そのまま |
| T2 | 0294-24-2211 | ヘッダー電話番号 | Header | そのまま |
| T3 | ホーム / 法人会の概要 / セミナー・講演会 / 会員紹介 / 入会案内 / お問合せ | ナビメニュー | Header | そのまま |
| T4 | 日立法人会は税を中心とした研修会や租税教育などを行っております。 | ヒーローサブテキスト | Hero | そのまま |
| T5 | 税のオピニオンリーダーとしての貢献や各種研修会の開催、社会貢献活動など地域に密着した活動を展開しています。 | ヒーロー説明文 | Hero | そのまま |
| T6 | 新着情報（4月2日更新〜2月20日更新の4件） | ニュースリスト | News | そのまま |
| T7 | 社団法人日立法人会は、従来日立税務署管内...公益社団法人日立法人会となりました。（profile.htmlの沿革全文） | 概要本文 | About | そのまま |
| T8 | 管内の概要（茨城県の北東部を占め...） | 概要本文（管内） | About | アコーディオン |
| T9 | 組織の状況（社団法人設立年月日...計1,582） | 概要本文（組織） | About | アコーディオン |
| T10 | 市町別概況（日立市・高萩市・北茨城市） | 概要本文（市町別） | About | アコーディオン |
| T11 | 管内の主要産業及び主要企業等 | 概要本文（産業） | About | アコーディオン |
| T12 | セミナー情報4件（経理の基礎・改正労働法・経理入門・新入社員セミナー） | セミナーカード | Services | カード化 |
| T13 | 企業の税務コンプライアンス向上（compliance.html本文） | サービスカード | Services | カード化 |
| T14 | 福利厚生制度（hukuri.html本文: 企業向け・個人向け保険制度一覧） | サービスカード | Services | カード化 |
| T15 | 生活習慣病健診（health.html本文: コース名・検査項目・価格） | サービスカード | Services | カード化 |
| T16 | 無料労務相談（advice.html本文） | サービスカード | Services | カード化 |
| T17 | 法人会って何ですか?〜入会してのメリットは?（nyukai.html前半） | 入会案内本文 | Membership | そのまま |
| T18 | 入会メリット7項目（①〜⑦） | メリットリスト | Membership | カード化 |
| T19 | 日立法人会年会費（正会員・賛助会員の料金表） | 会費テーブル | Membership | そのまま |
| T20 | 会員紹介企業一覧（kaiin.html 30社以上） | 会員一覧 | Members | アコーディオン |
| T21 | 第16回 税に関する絵はがきコンクール受賞作品 | 租税教育セクション | Services | カード化 |
| T22 | 問合せ・アクセス情報（住所・TEL・FAX・メール） | コンタクト情報 | Contact | そのまま |
| T23 | Copyright 公益社団法人 日立法人会 All Rights Reserved. | フッターコピーライト | Footer | そのまま |
| T24 | Sub Menu全項目（会員専用〜サイトマップ） | フッターリンク | Footer | そのまま |
| T25 | 社会保険料算出ツール（hokenryou_n.html） | 別ページ | - | 別ページ |
| T26 | プライバシーポリシー（privacy.html） | 別ページ | - | 別ページ |
| T27 | サイトマップ（sitemap.html） | 別ページ | - | 別ページ |
| T28 | 入札情報（nyusatu.html） | 別ページ | - | 別ページ |
| T29 | 共催・後援（kyou-kou.html） | 別ページ | - | 別ページ |
| T30 | 401 Unauthorized ページ（member/dl.html, yakuin/meeting.html） | 不要 | - | 不要 |
| T31 | メール登録フォーム（mail.html, mailto.html） | 別ページ | - | 別ページ |
| T32 | しんぶん.yomu（yomu.html） | 別ページ | - | 別ページ |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | images/logo.gif | original | photo | ヘッダーロゴ | Header | CSS/SVG代替（テキストロゴ化。画像DL不可のためCSS再現） |
| 8 | images/1.jpg | original | photo | ヒーロー背景1 | Hero | Unsplash差替（画像DL不可。日本の夜景） |
| 9 | images/2.jpg | original | photo | ヒーロー背景2 | Hero | 不要（ヒーローは1枚に統合） |
| 10 | images/3.jpg | original | photo | ヒーロー背景3 | Hero | 不要（ヒーローは1枚に統合） |
| 50 | images/soudan_1.jpg | original | photo | 労務相談カード画像 | Services | CSS/SVG代替（画像DL不可。アイコンで代替） |
| 51 | images/soudan_2.jpg | original | photo | 労務相談カード画像2 | Services | 不要 |
| 53-63 | aletter/image1-11.jpg | original | photo | 絵はがきギャラリー | Services | 不要（リデザインではテキストのみ。コンクール結果リスト化） |
| 2-7,42-49 | images/menu_*.gif | template | text-embedded | - | - | CSS/SVGナビに差替 |
| 13-22 | images/*.gif (バナー群) | template | text-embedded | - | - | 不要（テキストでカバー） |
| 23-40 | images/side_bnr*_on.gif | stock/template | text-embedded | - | - | 不要（外部リンクバナー） |

### 画像DL不可による変更点
- Bash権限が Phase 1-2 以降ブロックされたため、ローカル画像ダウンロード不可
- ロゴ: CSSテキストロゴに代替（元GIFも文字ベース）
- ヒーロー: Unsplash URLで直接参照（日本の風景写真）
- その他: CSS/SVG/テキスト代替
