# コンポーネント割当表 — 堺田幸志税理士事務所 (L-1726)

## サイト構造（単一ページ）
Header / Hero / About（所長紹介）/ Philosophy（経営理念）/ Services（業務案内）/ FAQ / Office Info（事務所概要・交通案内）/ Recruit / Contact / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 堺田幸志税理士事務所 | ヘッダーロゴ | Header | そのまま |
| T2 | 企業の繁栄をお手伝いします。 | ヒーロー主見出し | Hero | そのまま |
| T3 | 会社発展の全てをサポートし、経営者の皆様の悩みを解決する堺田幸志税理士事務所のHPへようこそ！ | ヒーローリード | Hero | そのまま |
| T4 | 事業計画策定・金融支援案の策定を支援いたします。 | ヒーロー補足 | Hero | そのまま |
| T5 | 事務所紹介 / 所長挨拶文 「私は税理士事務所を開設してから今日まで…」 | Aboutリード | About | そのまま |
| T6 | 所長経歴（昭和50年〜盛岡ロータリークラブ会計就任まで） | About経歴リスト | About | そのまま |
| T7 | 所属団体・資格一覧 | About団体・資格リスト | About | そのまま |
| T8 | 経営理念「人とのご縁を大切にしながら…」 | Philosophyカード | Philosophy | そのまま |
| T9 | 行動指針 6 項目 | Philosophyカード（numbered list） | Philosophy | そのまま |
| T10 | 業務案内リード「業務の内容や金額については…まずは何でも、ご相談ください。」 | Servicesリード | Services | そのまま |
| T11 | ≪業務案内≫ 13項目（法人税〜建設業許可申請） | Servicesカード（4カテゴリに分類してカード化） | Services | カード化 |
| T12 | ＜記帳指導＞＜記帳代行＞＜税務調査立会い＞＜決算業務＞の詳細説明 | Services詳細アコーディオン | Services | アコーディオン |
| T13 | 会計業務 5項目 / 経営コンサルティング業務 6項目 | Services詳細リスト | Services | そのまま |
| T14 | よくある質問 3 組 Q&A | FAQアコーディオン | FAQ | アコーディオン |
| T15 | 事務所概要（事務所名・所在地・電話・FAX・業務内容9項目） | Office Infoテーブル | Office Info | そのまま |
| T16 | 交通案内（〒020-0021 岩手県盛岡市中央通1-11-17 第2大通ビル４Ｆ / 019-652-7910） | Office Info | Office Info | そのまま |
| T17 | 採用情報（新卒・中途・パート、募集職種4種、業務内容、資格、給与、勤務時間、休日休暇） | Recruitセクション | Recruit | そのまま |
| T18 | お知らせ 2件（コロナページ / 確定申告の時期） | News（Heroサブ or お知らせ帯） | Hero補足 | そのまま |
| T19 | TEL 019-652-7910 / FAX 019-652-7912 | Contactブロック | Contact + Footer | そのまま |
| T20 | Copyright (c) 2021 - 2026 Koji Sakaida All Rights Reserved. | Footer | Footer | そのまま |
| T21 | 個人情報保護方針（リンクのみ表示） | Footerリンク | Footer | そのまま（別ページ扱いだがここでは Footer リンクに） |
| T22 | 東日本大震災により被災された皆さま…一刻も早く復興することができるよう、サポートを行って参ります。 | Message帯（About下） | About | そのまま |

## テキスト除外（別ページ的コンテンツ・TKC 共通素材）

以下は TKC 共通ポータル・機能紹介・セミナー履歴（古い日付）・個別 Q&A 記事 等、事務所固有性が低く、リデザインのメインに含めない:
- tkc-corona / tkc-system015 / tkc-hozyokin / tkc-introduce-financing / tkc-menu2-003 / tkc-administrative-information / tkc-management-qa / tkc-tax-calendar / tkc-tax-qa / tkc-system-qa / tkc-syatyou-menu-asp / tkc-link / tkc-nintei-shienkikan001 / free1-5 / link2 の TKC 共通コンテンツ
- セミナー案内 3 件（2015-2016 年と古く陳腐化。Recruit/About 程度に要素として掲載しない）
- reCAPTCHA モーダルテキスト（機能文言）

※ これらは元サイトの TKC ASP 共通機能であり、事務所固有の情報発信コンテンツではない。リデザイン後は「TKC 経営支援ツール（外部）」としてリンク参照する形にするのが本来望ましいが、今回のデモは事務所紹介に集中する。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 | ローカル名 |
|---|-------|------|------|----------------|-----------|------|---|
| 1 | library/575526a6e4e0c92ab1621279/201507181443_WNy3n.jpg | original | photo | 所長写真（丸型） | About | そのままローカル化 | `sakaida-daihyo.jpg` |
| H1 | Unsplash | — | photo | Heroビジュアル（背景オーバーレイ付） | Hero | Unsplash 直接参照 | — |
| H2 | Unsplash | — | photo | Services セクション装飾（オフィス/書類系） | Services | Unsplash 直接参照 | — |
| H3 | Unsplash | — | photo | Contact セクション装飾（電話/相談） | Contact | Unsplash 直接参照 | — |

**引き継ぎ画像（ローカル化対象）**: 1件のみ（所長写真）。

**Unsplash 差替方針**:
- Hero: 盛岡〜岩手地方のイメージは避け、士業オフィス・書類・ビル街の中性的な画像（business/office/building）
- Services: 会計・書類・電卓系
- Contact: 電話・相談・握手（avoid cliché）

## 統一性ルール
- Services カード 4 枚は全て「アイコン（SVG）+ タイトル + 説明」で統一。写真は使わない（混在禁止）。
- About の所長写真は 1 枚のみ使用、丸型トリミングで配置。
