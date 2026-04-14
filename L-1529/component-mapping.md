# コンポーネント割当表

## サイト構造
- Header（ロゴ + ナビ + 電話 + お問合せ CTA）
- Hero（事務所名 + キャッチコピー）
- News（新着情報 3件）
- About（事務所紹介・50年の歴史）
- Leaders（所長 髙梨英吉 + 税理士 髙梨徹也の紹介）
- Services（業務案内 8項目）
- TargetClient（個人事業者・法人・相続）
- Office（事務所概要・所在地・電話）
- Event（事務所の行事 簡易）
- Contact CTA
- Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 山形県の税理士　髙梨徹也税理士事務所　㈱高梨税務会計事務所 | ヘッダー社名 + title | Header / head | そのまま |
| T2 | 会社発展の全てをサポートし、経営者の皆様の悩みを解決する （株）高梨税務会計事務所のHPへようこそ | ヒーロー見出し | Hero | そのまま |
| T3 | この出会いは一期一会！ ここから始まります。 | ヒーローサブコピー | Hero | そのまま |
| T4 | 関与先企業の繁栄は私たちの喜びです。 | ヒーロー補足 | Hero | そのまま |
| T5 | 株式会社高梨税務会計事務所は ＴＫＣ全国会会員です / ＴＫＣ全国会は、租税正義の実現をめざし関与先企業の永続的繁栄に奉仕するわが国最大級の職業会計人集団です。/ 東北税理士会所属 | 信頼バッジセクション | About 内 | そのまま |
| T6 | 新着情報 2020.3.13 〜 2018.07.30 計4項目 | News カードリスト | News | そのまま |
| T7 | 事務所紹介 / 50年にわたる信頼とノウハウ / 私たちは、お客様に満足していただけるよう挑戦を続けます！ | About セクション見出し | About | そのまま |
| T8 | 税理士 髙梨英吉 あいさつ全文 + 経歴 | Leaders カード1 | Leaders | そのまま |
| T9 | 税理士 髙梨徹也 あいさつ全文 | Leaders カード2 | Leaders | そのまま |
| T10 | 事務所概要 一式（事務所名・所在地・電話・FAX・業務内容） | Office 情報テーブル | Office | そのまま |
| T11 | 業務案内 リード文 + 税務・会計 8項目（巡回監査〜記帳代行） | Services グリッド | Services | そのまま |
| T12 | 個人事業者の方 / 法人 / 相続及び贈与でお悩みの方（各リード文 + 詳細） | TargetClient 3カード（アコーディオン） | TargetClient | カード + アコーディオン |
| T13 | 企業防衛 / 開業及び法人設立をお考えの方（各リード文 + 詳細） | Services 補足アコーディオン | Services | アコーディオン |
| T14 | 事務所の行事 / 経栄会 / 婦人部会 / 高梨杯 ゴルフコンペ / 所内イベント | Event セクション 4カード | Event | そのまま |
| T15 | 所在地 山形県山形市五日町6-10 / TEL 023-643-7155 / FAX 023-644-9756 | Office 連絡先 + Footer | Office / Footer | そのまま |
| T16 | 職員紹介 導入文 + 各職員コメント | Staff セクション（要約カード） | Staff | そのまま（抜粋）※メインには入れず概要のみ |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 29 | .../5b22270877ccb21768acee41.jpg | original | photo | 所長顔写真 | Leaders カード1 | **そのまま（ローカル化）** |
| 30 | .../5b51429178ca01e97be0e2c0.jpg | original | photo | 税理士顔写真 | Leaders カード2 | **そのまま（ローカル化）** |
| 31 | .../5b513f26f83d62b07b4376ec.jpg | original | photo | 事務所外観 | Office セクション | **そのまま（ローカル化）** |
| — | Unsplash yamagata/mountain | stock | photo | Hero背景 | Hero | Unsplash 差替 |
| — | Unsplash office/meeting | stock | photo | About ビジュアル | About | Unsplash 差替 |
| — | CSS/SVG | — | icon | 各 Service アイコン | Services | SVG 代替 |
| — | Unsplash business/tokyo | stock | photo | Services ビジュアル | Services | Unsplash 差替 |

## ダウンロード対象（Phase 5-0 実行予定）

| ファイル名 | 元URL |
|---|---|
| leader-eikichi.jpg | https://takanashizeimukaikei.tkcnf.com/library/574be103dec07e302b658df4/5b22270877ccb21768acee41.jpg |
| leader-tetsuya.jpg | https://takanashizeimukaikei.tkcnf.com/library/574be103dec07e302b658df4/5b51429178ca01e97be0e2c0.jpg |
| office-exterior.jpg | https://takanashizeimukaikei.tkcnf.com/library/574be103dec07e302b658df4/5b513f26f83d62b07b4376ec.jpg |

## 差替画像（Unsplash 直接参照）

- Hero 背景: 山形の自然 / 信頼感のある風景
- About / Services: オフィス・業務シーン
