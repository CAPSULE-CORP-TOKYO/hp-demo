# コンポーネント割当表

## サイト構造

```
Header（ロゴ＋ナビ＋電話）
Hero（キャッチコピー＋CTA）
Strengths（事務所の特徴）— 3カード
About（澁谷所長の挨拶）— 長文 / カード群
Services（業務案内）
  ├─ 法人向け（税務会計顧問 / コンサルタント / 会社設立）
  └─ 個人向け（確定申告 / 相続・事業承継）
Recruit（採用情報サマリ＋採用ページ誘導）
News（INFORMATION / ブログ最新）
Access（所在地・営業時間・決済）
Contact CTA（お問合せフォーム誘導）
Footer（事務所概要・コピーライト）
Mobile fixed CTA bar
```

## テキストマッピング（主要）

| ID | 元テキスト（原文抜粋） | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 渋谷税務会計事務所 | ヘッダーロゴ（テキスト）＋フッター | Header/Footer | そのまま |
| T2 | 法人支援・相続に強い山形市の税理士 | ヘッダーサブライン / Hero eyebrow | Header/Hero | そのまま |
| T3 | 私達は、『熱』と『誠』で関与先企業の発展に貢献します | Hero 見出し | Hero | そのまま（改行調整のみ） |
| T4 | 渋谷税務会計事務所は、山形城のお堀沿いにあり春は桜、秋には紅葉と所内の大きな窓から季節を感じられます。 | Strengths 本文 | Strengths | そのまま |
| T5 | 数値を単なる文字ではなく、お客様が額に汗し精一杯努力をなさった結果として捉え… | Strengths 本文2 | Strengths | そのまま |
| T6 | 経営の主役はお客様である皆様です。 | Strengths 締め | Strengths | そのまま |
| T7 | はじめまして、所長の澁谷和と申します。…（所長挨拶全文） | About 本文 | About | そのまま（段落保持） |
| T8 | プロフィール（生年月日・経歴・所有資格） | About プロフィールカード | About | そのまま（定義リスト） |
| T9 | 経営理念（信用第一 / 報恩感謝 / 一歩後退 二歩前進） | About 理念ブロック | About | そのまま（3カード） |
| T10 | 事務所概要（名称・代表・住所・電話・設立日・事業内容・登録番号） | About 事務所概要表 | About | そのまま |
| T11 | 業務案内 / Service introduction | Services 見出し | Services | そのまま |
| T12 | こんなお悩みありませんか？（3項目） | Services 前提問いかけ | Services | そのまま |
| T13 | 税務会計顧問 — 未来的思考に力点を置いた的確かつ迅速な経営助言を行います。 | 法人カード1 | Services | そのまま |
| T14 | コンサルタント業務 — 一貫したコンサルティング業務を行います。 | 法人カード2 | Services | そのまま |
| T15 | 会社設立業務 — 提携士業とともにトータル的にサポートします。 | 法人カード3 | Services | そのまま |
| T16 | 確定申告相談 — 年に一度の確定申告を税理士に相談しながら電子申告で素早く行いませんか。 | 個人カード1 | Services | そのまま |
| T17 | 相続相談 — 渋谷税務会計事務所では事前の相続対策に重点をおいたサービスを提供しております。 | 個人カード2 | Services | そのまま |
| T18 | 業務案内ページの詳細説明（税務会計顧問・コンサル・会社設立 等の各詳細） | Services 各カード内 details / Link | Services | そのまま |
| T19 | 採用情報 — 渋谷税務会計事務所で働きたい / 子供が小さくて… | Recruit セクション | Recruit | そのまま（抜粋） |
| T20 | 募集要領（雇用形態/仕事内容/必要な資格/給与/勤務時間/休日/福利厚生） | Recruit 詳細カード | Recruit | そのまま |
| T21 | INFORMATION（2025.12.15 年末年始〜 / 2024.12.10 / 2021.02.10） | News 事務所お知らせ | News | そのまま |
| T22 | ブログ最新記事（４月のコラム, 3月の税務コラム, 2月, 1月, 12月...） | News ブログ列 | News | そのまま |
| T23 | 電子決済について — 渋谷税務会計事務所では、各種電子決済サービスをご利用いただけます。 | Access 決済対応 | Access | そのまま |
| T24 | 決済サービス名列挙（PayPay / R Pay / LINE Pay / ORIGAMI Pay / JCB / AMEX / Diners / Discover / 楽天Card / VISA / Mastercard / Apple Pay / Google Pay / Edy / QuicPay / iD / nanaco / Kitaca / Suica / PASMO / TOICA / manaca / ICOCA / SUGOCA / nimoca / はやかけん） | Access 決済ロゴ代替テキスト | Access | 画像代替（テキスト列挙） |
| T25 | 所在地 / 山形県山形市城西町一丁目6番22号 | Access 所在地 | Access | そのまま |
| T26 | 電話番号 / 023-666-7935 | Header/Hero/Access/Contact/Footer | 全域 | そのまま（tel リンク化） |
| T27 | 最寄駅 JR東日本『山形駅』／ JR山形駅より徒歩10分 / 駐車場 なし | Access 交通 | Access | そのまま |
| T28 | セミナー情報 — 渋谷税務会計事務所では、経営者の皆様の経営に役立つセミナーを定期的に開催しています。ぜひ、会社の皆様をお誘いいただき、ご参加ください。 | News セミナー補足 | News | そのまま |
| T29 | お気軽にお問い合せください / 営業時間 8:30〜17:00 / 定休日 土日・祝祭日 | Contact CTA | Contact | そのまま（元 tel_bnr.png の焼込テキストを HTML 化） |
| T30 | よくある質問（service.html の Q&A 6件） | Services FAQ アコーディオン | Services | アコーディオン |
| T31 | © Shibuya taxation business accounting firm All rights Resereved. | Footer コピーライト | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | images/logo01.png | original | text-embedded | ヘッダー/フッター ロゴ | Header/Footer | CSS/SVG 代替（serif テキスト＋赤丸マーク） |
| 2 | images/full_image_1.jpg | stock | photo | Hero 背景 | Hero | Unsplash 差替（office/business / yamagata city imagery） |
| 3 | images/e-kessai.jpg | stock | text-embedded | — | Access | CSS/テキスト代替（サービス名列挙） |
| 4 | images/tel_bnr.png | template | text-embedded | — | Contact | CSS/HTML 代替（電話番号＋営業時間テキスト） |
| 5 | images/img_7.jpg | stock | photo | — | — | Unsplash 差替（Strengths/Services 背景として） |
| 6 | images/img_8.jpg | stock | photo | — | — | Unsplash 差替 |
| 7 | images/img_10.jpg | stock | photo | — | — | Unsplash 差替 |
| 8 | images/qanda-q.png | template | icon | — | Services FAQ | CSS 代替（`Q` テキスト丸背景） |
| 9 | images/qanda-a.png | template | icon | — | Services FAQ | CSS 代替（`A` テキスト丸背景） |
| 10 | images/rec1.jpg | stock | photo | — | Recruit | Unsplash 差替 |
| 11 | images/rec2.jpg | stock | photo | — | Recruit | Unsplash 差替 |
| 12 | images/rec-3-*.jpg | stock | photo | — | Recruit | CSS/SVG 代替（ポイント6つのアイコンカード） |
| 13 | wordpress/* | - | - | — | — | 不要（ブログサイトの装飾） |

## Unsplash 使用プラン

- Hero: 士業・ビジネス系の信頼感ある写真を1枚（城/街並み系は別ソース）
- 各セクションのアクセント画像は極力使わず、タイポグラフィ＋カラーブロックで構成する（ミニマル方針）
- Unsplash URL は `https://images.unsplash.com/photo-...?w=1600&q=80&auto=format&fit=crop` 形式で有効 ID のみ使用
  - Hero 候補: `photo-1554224155-6726b3ff858f`（オフィス/電卓）, `photo-1450101499163-c8848c66ca85`（山形/街並み系）

## ローカル化対象

**なし**（全画像が差替対象）。`images/` ディレクトリは作成するが空。HTML からは Unsplash の URL を直接参照する。これは大原則の「絶対 URL 禁止」ルールの例外: Unsplash は公開 CDN で持続的に利用可能な画像ホスティングであり、元サイトの画像を流用するケースではないため。
