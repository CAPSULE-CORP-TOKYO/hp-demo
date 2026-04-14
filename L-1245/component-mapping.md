# コンポーネント割当表

## サイト構造
- Header / Hero / Message (Concept) / About (代表挨拶) / Services (業務案内) / Flow (ご相談) / Online (オンライン相談) / Office (事務所案内) / Contact (お問い合わせ) / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 鷲尾税理士事務所 | ヘッダーロゴテキスト | Header | そのまま |
| T2 | WAK会計事務所 | ヘッダーサブテキスト | Header | そのまま |
| T3 | メッセージ / 代表挨拶 / 業務案内 / ご相談 / 事務所案内 / お問い合わせ | ナビリンク | Header | そのまま |
| T4 | 経営課題の解決支援 | ヒーロー見出し | Hero | そのまま |
| T5 | 経営者の心強い味方 | ヒーローサブ | Hero | そのまま |
| T6 | 効果的な問題解決へのアプローチ | セクション見出し（テキスト化） | Message | そのまま（画像からテキストに変換） |
| T7 | 当社は基本的に、有資格者がお客様へ対応いたしております。...経営課題の解決支援を多方面から行っております。 | メッセージ本文 | Message | そのまま |
| T8 | 代表挨拶 | セクション見出し | About | そのまま |
| T9 | 当社は創業以来、税務・会計を通じて...私たちに是非お任せください。 | 代表挨拶本文 | About | そのまま |
| T10 | 所長税理士 鷲尾秀樹 | 代表者名 | About | そのまま |
| T11 | 業務案内 | セクション見出し | Services | そのまま |
| T12 | 税理士顧問（税務＆会計）/ 決算... / 相続 | サービスリスト | Services | カード化 |
| T13 | ご相談 | セクション見出し | Flow | そのまま |
| T14 | 税務、会計、経営等に関するご相談を承っております。お電話またはお問合せフォームよりご予約ください。 | 相談導入文 | Flow | そのまま |
| T15 | 1.お問い合わせ ... まずは、お電話または... | フローステップ1 | Flow | そのまま |
| T16 | 2.ご相談 ... 直接お会いし... | フローステップ2 | Flow | そのまま |
| T17 | 3.ご契約 ... 料金やご提案に... | フローステップ3 | Flow | そのまま |
| T18 | 4.サービス開始 ... ここから正式に... | フローステップ4 | Flow | そのまま |
| T19 | オンライン相談のご案内 | サブセクション見出し | Online | そのまま |
| T20 | 当社ではオンラインによる税務相談も実施しております。...是非ご利用ください。 | オンライン導入文 | Online | そのまま |
| T21 | Web会議サービス「ZOOM」または「Google Meet」を使い...招待メールをお送りいたします。 | オンライン詳細 | Online | そのまま |
| T22 | 必要な環境 / ・インターネット接続環境 / ・ウェブカメラ付属の... | 環境要件 | Online | そのまま |
| T23 | 事務所案内 | セクション見出し | Office | そのまま |
| T24 | 名称: WAK株式会社 / 代表者: 鷲尾秀樹 / 所在地: 宮城県仙台市... / 電話番号: 022-748-4580 / FAX番号: 022-748-4581 | 事務所情報テーブル | Office | そのまま |
| T25 | お問い合わせ | セクション見出し | Contact | そのまま |
| T26 | ご依頼、ご質問など、お気軽にお問い合わせください。担当者より折り返しご連絡させて頂きます。 | 問い合わせ本文 | Contact | そのまま |
| T27 | メールでお問い合わせ | メールリンク | Contact | そのまま |
| T28 | ©WAK Tax Accounting Office | コピーライト | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 2 | https://040tax.jp/img/logoS.png | original | photo | ヘッダーロゴ | Header | そのまま |
| 3 | https://040tax.jp/img/mainLogo.svg | original | photo | ナビロゴ | Header | そのまま |
| 4 | https://040tax.jp/img/mainLogo-w.svg | original | photo | ヒーローロゴ | Hero | そのまま |
| 5 | https://040tax.jp/img/message.png | stock | text-embedded | — | Message | CSS/SVG代替（テキストをHTMLで再現） |
| 6 | https://040tax.jp/img/service.png | stock | photo | — | Services | Unsplash差替 |
| 7 | https://040tax.jp/img/flow1.png | template | icon | フローアイコン1 | Flow | CSS/SVG代替 |
| 8 | https://040tax.jp/img/flow2.png | template | icon | フローアイコン2 | Flow | CSS/SVG代替 |
| 9 | https://040tax.jp/img/flow3.png | template | icon | フローアイコン3 | Flow | CSS/SVG代替 |
| 10 | https://040tax.jp/img/flow4.png | template | icon | フローアイコン4 | Flow | CSS/SVG代替 |
| 11 | https://040tax.jp/img/info.png | stock | photo | — | Online | Unsplash差替 |
| 12 | https://040tax.jp/img/map.png | template | icon | — | Office | CSS/SVG代替 |
| 13 | https://040tax.jp/img/mail.png | template | icon | — | Contact | CSS/SVG代替 |

## ヒーロー背景
現サイトのヒーローはCSSバックグラウンド画像（ビジネスマンが都市を見下ろすモノクロストック写真）。
→ Unsplash差替: 仙台/オフィス/ビジネス系の落ち着いた写真
