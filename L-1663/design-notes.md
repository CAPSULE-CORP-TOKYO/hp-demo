# 分析結果 L-1663

## リード情報
- leadId: L-1663
- companyName: 税理士法人 大坪・阿部会計事務所 酒田事務所
- 住所（酒田支店）: 〒998-0054 山形県酒田市宮野浦3-6-36
- TEL（酒田支店）: 0234-25-5320
- website: https://www.otsubo-office.com/
- industry: 税理士
- proposalType: renewal

## 重要な構造上のポイント
- 元サイトは本店（千葉県市川市）メイン。酒田事務所は支店。
- 会社全体名称: 税理士法人 大坪・阿部会計事務所
- リードは「酒田事務所」なので、リデザインでは「山形県酒田市の税理士事務所」としての入口を強化しつつ、会社全体（市川本店＋酒田支店）の実態も原文どおり保持。
- 電話番号: リードの phone（酒田 0234-25-5320）を Hero/CTA に掲出。市川本店の TEL はフッターの本支店情報ブロックにそのまま保持。
- 代表社員税理士: 大坪 恭也

## アーキタイプ
名前: A: モダンミニマル（士業向け）+ 控えめにエグゼクティブ感
根拠:
- 税理士法人。法人設立・相続・資金繰りなど B2B/資産家向けの堅い業種
- 元サイトは紺色基調で権威的トーン
- モダン士業サイトの定番（大胆な余白、サンセリフ、高コントラスト、控えめなアクセント）が最適
- Noto Sans JP メイン、見出しに Noto Serif JP を併用して落ち着きを出す

## カラーパレット
元サイト screenshot から抽出:
- メイン（primary navy）: #1b3c6f（紺色基調、元サイトのヘッダー・サイドバー色の継承）
- サブ（deep navy）: #0f2547
- ベース: #ffffff / #f5f7fa（やや温かみのあるオフホワイト）
- アクセント: #c8a24b（落ち着いたゴールド、士業・権威系で常套。紺との相性◎）
- テキスト: #1a1a1a / #4a5568（本文） / #6b7280（補助）

60-30-10:
- base 60% = 白 + オフホワイト
- primary 30% = navy 系
- accent 10% = gold（CTA ボタン、下線、アイコン）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../header_name2.png | original | text-embedded | CSS代替 | 社名ロゴ（テキスト焼込）→ HTML テキストで代替 |
| 2 | .../top.jpg (hero) | original | text-embedded | Unsplash差替 | 「税務・会計相談...」大きな焼込あり。但し背景のスタッフ写真は staff.jpg で代替可 |
| 3 | .../support.png | original | text-embedded | 差替 | 「会社設立・独立開業のサポートを致します」焼込 |
| 4 | .../notary.png | original | text-embedded | 差替 | 「大坪恭也行政書士事務所のWebサイト」焼込 |
| 5 | .../top_s01.jpg | stock | photo | Unsplash差替 | 握手の汎用ストック |
| 6 | .../top_s02.jpg | stock | photo | Unsplash差替 | 手書きの汎用ストック |
| 7 | .../top_s03.jpg | stock | photo | Unsplash差替 | 札束の汎用ストック |
| 8 | .../top_s04.jpg | stock | photo | Unsplash差替 | PC操作の汎用ストック |
| 49 | .../shocho.jpg | original | photo | そのまま引き継ぎ | **所長・大坪恭也の顔写真**（About セクションで使用） |
| 50 | .../staff.jpg | original | photo | そのまま引き継ぎ | **スタッフ集合写真**（Hero 背景 / About で使用） |
| 39/51 | .../seturitu.png | original | diagram | そのまま引き継ぎ | 法人設立までの流れ図 |
| 52 | .../sozoku.png | original | diagram | そのまま引き継ぎ | 相続税申告の流れ図 |
| 54 | .../kakutei.png | original | diagram | そのまま引き継ぎ | 法人確定申告までの流れ図 |
| 10-37 | topics/*.jpg | original | photo | 不要 | ニュース個別記事内の写真。index に載せない |
| 9/40/41 | mfp_must.gif / mail-to.png | template | icon | CSS/SVG代替 | アイコン類 |

## 引き継ぐ画像（Phase 5-0 でローカル化）

- shocho.jpg（代表写真）
- staff.jpg（スタッフ集合写真）— Hero 背景として使用
- seturitu.png（法人設立フロー図）
- sozoku.png（相続税申告フロー図）
- kakutei.png（法人確定申告フロー図）

## フォント方針
- Noto Sans JP（本文・ナビ・見出し基本）
- Noto Serif JP（Hero 見出し・セクション見出しの一部でアクセント）

## ナビ構成
- Home / サービス・料金 / 会社設立の流れ / 相続相談 / 所長・スタッフ / アクセス / お問い合わせ
