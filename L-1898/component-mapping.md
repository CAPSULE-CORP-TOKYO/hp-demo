# コンポーネント割当表 — L-1898

## サイト構造
1. Header（ロゴ + ナビ + CTA）
2. Hero（オフィス写真 + 明朝キャッチコピー）
3. About / Greeting（代表挨拶）
4. Stats（保有資格数）
5. Practice / Services（5領域）
6. Specialties（専門業務 10領域）
7. Our Purpose（Vision / Value / Purpose）
8. Office / Access（つくばオフィス：地図・住所・電話）
9. News（お知らせ）
10. Contact（CTA + 電話）
11. Footer（拠点・コピーライト・ポリシーリンク）

モバイル追従 CTA バー: TEL + お問い合わせ

## テキストマッピング

| ID | 元テキスト（原文） | 出典ページ | 新コンポーネント | 処理 |
|----|-----------|----------|----------------|------|
| T1 | AKJ Partners | / Header | Header ロゴ右テキスト | そのまま |
| T2 | 税理士法人AKJパートナーズ つくばオフィス | leads.json | Header サブテキスト・タイトル | そのまま（leads.json正本） |
| T3 | 企業は、その取り巻く様々な利害関係者からの「信頼」を得て成り立ちます。 | / copy01.png 焼込 | Hero 見出し（明朝・1行） | そのまま（焼込画像をHTML化） |
| T4 | 企業を取り巻く環境は、その成長スピードに相乗し、めまぐるしく変化しております。この環境の変化に対応でき、初めて企業はその成長スピードを維持、次へのステージへと上っていくことができるものと、確信しております。私どもAKJ Partnersは、企業がこの環境変化にいかに迅速に対応できるか、職業的専門家の見地から助言・指導することを使命と考えております。事務所の基本理念であります、クライアントの成長を通じた健全な経済社会の発展への貢献を目指し、「柔軟性(Flexibility)」と「法令遵守(Compliance)」のもと、「信頼性(Confidence)」を勝ち取るべく、所員一人ひとりがより一層の専門知識を磨き、高度な専門家集団でありつづけます。 | corporateprofile/ Greeting | About / Greeting 本文 | そのまま（一字一句） |
| T5 | 公認会計士 9人 / 米国公認会計士 3人 / 税理士 16人 / CFP・AFP 4人 / 税理士科目合格・ACCA Level 2 12人 / 社会保険労務士（特定社会保険労務士含） 6人 / 医業経営コンサルタント 2人 / 公認不正検査士（CFE） 2人 / M&Aシニアエキスパート（金融財政事情研究会認定） 7人 | corporateprofile/tax/ 保有資格 | Stats カウンター（9項目） | そのまま |
| T6 | Audit 法定監査業務 / 任意監査業務・その他保証業務 / 監査対応支援業務 / 「合意された手続」業務 / 公認不正検査士による外部通報窓口業務 | practice/ | Services カード1 | そのまま |
| T7 | Tax & Account（Transaction Advisory Service: 資本政策の立案及び実行支援、企業組織再編、M&A、事業承継、税務デューディリジェンス、国税庁方式に基づく株価算定 / Corporate & Individual Business Service: 法人・個人における税務会計支援、プライベート・バンキング、グループ通算制度導入・申告支援、国際税務コンサルティング / Public Sector Service: 医療機関・介護福祉施設コンサルティング、学校法人コンサルティング / Accounting Resource Service: BPR支援、BPO支援、ディスクローズ支援、ストラクチャード・ファイナンス業務） | practice/ | Services カード2 | そのまま（要約しない） |
| T8 | Financial Advisory Service 株式公開コンサルティング / 企業再生コンサルティング / 各種評価業務 / 財務デューディリジェンス / FA業務 / コーポレートファイナンス業務 / IFRS導入支援 / 経営コンサルティング / 社会福祉法人内部統制支援 / 内部統制の高度化支援 / 決算体制の高度化支援 / 原価計算制度の設計支援 / 予算管理制度の設計支援 / グループ会社の財務調査支援 | practice/ | Services カード3 | そのまま |
| T9 | Human Resource 給与・賞与計算 / 年末調整 / 労務コンサルティング / 助成金コンサルティング / 給与明細ペーパーレス化サービス / 人事労務デューディリジェンス | practice/ | Services カード4 | そのまま |
| T10 | Others Publications / セミナー開催 | practice/ | Services カード5 | そのまま |
| T11 | IFRS関連支援業務 / ストック・オプションの報酬制度としての活用と設計・評価 / IPO支援業務 / 相続・事業承継 / 医療機関・介護福祉施設コンサルティング / シンガポールへの進出支援 / 移転価格コンサルティング業務 / 国際税務コンサルティング / 外資系企業支援 / 個人所得税確定申告 | / Footer + practice/ | Specialties リスト（10項目） | そのまま |
| T12 | Purpose（存在意義）「クライアントの成長を通じた健全な経済社会の発展への貢献」プロフェッショナルの見地から、クライアントの課題解決および成長による健全な経済社会の発展への貢献こそが私たちの使命。「柔軟性(Flexibility)」と「法令遵守(Compliance)」のもと、「信頼性(Confidence)」を勝ち取り、社会的に存在意義のあるプロフェッショナルファームを創りだします。 | our-purpose/ | Our Purpose - Purpose | そのまま |
| T13 | Vision（目指す姿）クライアントからの永続的に揺るがない信頼を勝ち取る。AKJ Partners に属する全てのメンバーが、自己実現の達成の場として生きがいを見出すことができる。 | our-purpose/ | Our Purpose - Vision | そのまま |
| T14 | Value（価値観）【組織】「高い品質と総合力」各プロフェッショナルが、有機的・機動的に連携し、高い品質と総合力を発揮する。「教育・育成」プロフェッショナルファームとしての高いプレゼンスの維持を図るべく、教育・育成に取り組む。【個人】「クライアントとのコミュニケーション」クライアントとの密接なコミュニケーションにより、潜在的な課題のみならず将来的なリスクをも把握した期待を超える知的専門ソリューションの提供を図る。「クロージング力」プロフェッショナルとしてのやり遂げる信念を持つ。「ポジティブな積極性」自ら当事者意識を持って、積極的に業務に取り組む。 | our-purpose/ | Our Purpose - Value | そのまま |
| T15 | つくばオフィス | leads + access/tsukuba-office/ | Access セクションタイトル | そのまま |
| T16 | 〒305-0032 茨城県つくば市竹園１丁目6−１ つくば三井ビルディング 18F | leads.json | Access 住所 | そのまま（leads.json 正本） |
| T17 | TEL.029-868-7033 / FAX.029-868-7034 | access/tsukuba-office/ | Access 連絡先 | そのまま（FAXは原文側） |
| T18 | つくばエクスプレス「つくば駅」A5番出口より徒歩5分 | access/tsukuba-office/ | Access 交通 | そのまま |
| T19 | 商号: 税理士法人 AKJパートナーズ / 設立: 平成22年8月 / 代表パートナー: 公認会計士・税理士 山本 成男, 公認会計士・税理士 吉村 史明 / パートナー: 仁田 順哉, 本田 淳介, 村田 洋子, 森 浩之, 脇屋 忠生, 百瀬 弘之, 沼岡 晴成 | corporateprofile/tax/ | About 法人概要テーブル | そのまま |
| T20 | 2026年4月1日【金融庁】【FAS】「企業内容等の開示に関する内閣府令の一部を改正する内閣府令」の公布等について / 2026年1月10日「会計検査院の指摘で実務の影響は？ストックオプション税務における再点検」旬刊経理情報No.1764（中央経済社）に執筆 / 2021年12月27日【3 minutes】「親族外承継の方法」を公開 | / | News リスト3件 | そのまま |
| T21 | 東京オフィス / つくばオフィス / 福岡オフィス / シンガポールオフィス / サテライトオフィス | / Footer | Footer 拠点リスト | そのまま |
| T22 | Copyright (c) AKJ Partners All Rights Reserved. | / | Footer コピーライト | そのまま |
| T23 | PRIVACY POLICY / SOCIAL MEDIA POLICY / 倫理綱領・行動規範 / 特定個人情報等の適正な取扱に関する基本方針 / 情報セキュリティ方針 | / Footer | Footer ポリシーリンク | そのまま |
| T24 | グループ: 社会保険労務士法人 AKJパートナーズ / 株式会社 AKJパートナーズ / 株式会社 AKJメディカルサービス / AKJ PARTNERS CONSULTANCY PTE. LTD. | corporateprofile/tax/ | Footer グループ会社 | そのまま |
| T25 | お問い合わせ | contact/ | CTA ボタン | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | 処理 |
|---|-------|------|------|----------------|------|
| 1 | header-logo.png | original | photo | Header ロゴ | ローカル化 (`images/header-logo.png`) |
| 8 | mainvisual01.png | original | photo | Hero メイン背景（エントランス） | ローカル化 (`images/mainvisual01.png`) |
| 10 | mainvisual02.png | original | photo | About / Office セクション写真 | ローカル化 (`images/mainvisual02.png`) |
| 12 | mainvisual03.png | original | photo | Services 背景 or Office 写真2 | ローカル化 (`images/mainvisual03.png`) |
| 14 | mainvisual04.png | original | photo | Office 写真3 | ローカル化 (`images/mainvisual04.png`) |
| 103 | map_tsukuba.png | original | diagram | Access 地図 | ローカル化 (`images/map_tsukuba.png`) |
| 54 | sign.gif | original | photo | About 代表署名 | ローカル化 (`images/sign.gif`) |
| 47 | mark-sgs.png | original | photo | Footer 認証マーク | ローカル化 (`images/mark-sgs.png`) |
| 9,11,13,15 | copy01-04.png | original | text-embedded | — | 不要（テキストはT3で再利用） |
| 2-7,19-46 | nav-*.png | template | icon | — | CSS/SVG 代替（テキストナビ） |
| 16-18 | title-*.png | original | text-embedded | — | HTML 見出しに置換 |
| 52,65,97,127等 | pagevisual-*.png | original | text-embedded | — | 不要（HTML 見出しに置換） |
| その他 (recruiting, books, ifrs, ipo 等の装飾画像) | mixed | various | — | 不要（デモではメインに含めない） |

合計引き継ぎ画像: **8枚**（mainvisual01-04 + logo + map + sign + sgs）

### 並列性ルール確認
- Hero: 単一画像（mainvisual01）→ OK
- About / Office: mainvisual02-04 を1セクション内で並列使用 → 全て original photo で統一OK
- Services カード5枚: アイコンは全てゴールドのSVG icon で統一 → 並列性OK
- Specialties: テキストのみのリスト → 画像なし
- Access: 地図1枚（map_tsukuba）

### 元サイトに直接 URL 参照しない
全ての引き継ぎ画像は `images/` ディレクトリにダウンロード後、相対パスで参照する。
