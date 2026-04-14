# 分析結果

## アーキタイプ
名前: A（モダンミニマル）+ 伝統系のサブ要素
根拠:
- 税理士（士業）で権威性・信頼性が求められる業種
- 元サイトは「自利利他」「お客様第一主義」など落ち着いた文体だが、顧客層は中小企業経営者・個人・創業者と広い
- 情報量は豊富（料金表、ご相談の流れ、サービス解説、採用情報）
- モダンミニマルを基軸に、見出しに Noto Serif JP を使い権威性を出す
- 所長経歴・実績は文字情報として強く訴求

## カラーパレット
（元サイトのスクリーンショットから抽出）
- メイン: `#2f7a47`（深緑 / 信頼・士業系）
- サブ: `#eaf5ec`（淡い緑 / 背景・セクション区切り）
- アクセント: `#c49a3a`（金 / 権威・CTA用）
- ニュートラル: `#1f2937`（濃グレー / 本文）, `#6b7280`（グレー / サブテキスト）, `#ffffff`（白 / base）

元サイトの色相（緑系）は必ず継承。CTA ボタンにメイングリーンを使用し、ホバー・アクセントに金を使う（60-30-10）。

## 画像分類

元サイトの画像を「出自 × 適性」で分類し、処理方針を決定する。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | library/.../693775e96fde3063454b51d3.jpg | original | photo | そのまま | 所長（上村文明）ポートレート。本物の代表写真 |
| 2 | library/.../69377fcbab946449801163e5.jpg | original | photo | そのまま | 事務所建物全景（2階建ての白い建物、交差点角から） |
| 3 | library/.../69378caf5c59fc6a72f8d382.jpg | original | photo | そのまま | 事務所付近交差点（南青山入口） |
| 4 | library/.../69377fc08ac5224979ba142d.jpg | original | photo | そのまま | JR天王台駅北口前からの通り（アクセス案内用） |
| 5 | library/.../69377fb26fde3063454b5452.jpg | original | photo | そのまま | 上村会計事務所の看板が見える通り |
| 6 | library/.../695dec4de9fa8629b21eac7b.jpg | original | photo | そのまま | 税務・会計サービスカード用 |
| 7 | library/.../695dec4d70374e0d319f64ed.jpg | original | photo | そのまま | 自計化・デジタル化支援カード用 |
| 8 | library/.../695dec4de9c4070be708ef8c.jpg | original | photo | そのまま | 創業支援カード用 |
| 9 | library/.../695dec4da201043a964e414e.jpg | original | photo | そのまま | 経営支援カード用 |
| 10 | library/.../69117e16a5baf9525077627f.png | original | photo | そのまま | ロゴマーク画像 |
| 11 | library/.../Feature01-03 各種 | original | text-embedded | 差替 | 「Feature01/半世紀の歩み」等のテキスト焼込バナー → HTML 文字で再現 |
| 12 | library/.../ごあいさつ.png / サービス案内.png 等 | original | text-embedded | 差替 | セクションタイトル画像 → HTML 文字で再現 |
| 13 | library/.../お気軽にお問合せください系 | original | text-embedded | 差替 | 電話番号焼込バナー → HTML で再現 |
| 14 | library/.../自利利他の書 | original | text-embedded | 差替 | 書画だが HTML テキスト + 装飾で再現（テキストは text-inventory にある） |
| 15 | design/images/bnr-fixed/bnr-invoice-* | template | text-embedded | 差替 | TKC テンプレのインボイスバナー → 掲載しない |
| 16 | design/images/bnr-fixed/bnr-nensyunokabe-* | template | text-embedded | 差替 | TKC テンプレの年収の壁バナー → 掲載しない |
| 17 | design/images/common/icon-* | template | icon | CSS/SVG 代替 | 小アイコン |
| 18 | material/lib07/... service02 bnr 群 | template | text-embedded | 差替 | TKC 提供のサービス説明画像 → 使わない（HTML テキストで完結） |
| 19 | 経営革新等支援機関認定 | original | text-embedded | 差替 | HTML バッジで再現 |
| 20 | 駐車場地図 (69785194f36cde4795b89a72.png) | original | diagram | そのまま | 駐車場地図（固有図表） |

## 採用する固有写真（Phase 5-0 でローカル化）

1. 所長ポートレート（#1）→ About セクション
2. 事務所建物全景（#2）→ Hero 背景 / Office セクション
3. 税務・会計イメージ（#6）→ Services カード
4. 自計化・デジタル化イメージ（#7）→ Services カード
5. 創業支援イメージ（#8）→ Services カード
6. 経営支援イメージ（#9）→ Services カード
7. ロゴマーク（#10）→ Header ロゴ

事務所周辺写真（#3-5）、駐車場地図（#20）は Access セクションに配置可能だが、一貫性のため Access は Google Maps 埋め込みか、シンプルな住所テキストで代替する方針も検討。今回は文字情報メイン＋建物写真1枚で Office セクションを構成する。

## 差替方針

- テキスト焼込画像（Feature01-03、ごあいさつ等）は HTML テキストで再現
- テンプレバナーは掲載しない（サービス詳細は HTML テキストで十分）
- アイコンは SVG / Unicode で代替
