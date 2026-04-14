# 分析結果 — L-1864 税理士法人イカワ会計

## 基本情報
- 会社名（正式）: 税理士法人イカワ会計
- 代表者: 居川 孝男
- 所属税理士: 居川 孝男 / 居川 陽明 / 熊谷 光明 / 滝田 賢治
- 本社: 〒961-8056 福島県西白河郡西郷村字下前田西24-2 / TEL 0248-24-3056 / FAX 0248-24-4817
- 郡山事務所: 〒963-8871 福島県郡山市本町1丁目8-11 Villa MotomatiⅡ203号室 / TEL 024-953-8260 / FAX 024-953-8270
- メール: ikawa@tkcnf.or.jp
- 平成4年開業、平成29年4月法人化
- キャッチコピー（元サイト由来）: 「ビジネスを支える、信頼の良きパートナー」

## アーキタイプ
**A: モダンミニマル**（士業・コンサル系）

根拠:
- 士業（税理士法人）で権威性・信頼性の訴求が重要
- 元サイトは TKC テンプレで情報が縦に延々続く構造。情報整理とコントラスト回復が一番の改善点
- 顧客は中小企業経営者。過度な装飾よりクリアで読みやすいレイアウトが好まれる
- 見出しに Noto Serif JP を補助的に使うことで権威性を保ちつつ、本文は Noto Sans JP で可読性を確保

## カラーパレット
元サイトの青系を継承しつつ、落ち着きと信頼感のあるトーンに整える。

- メインカラー: `#1a4b8c`（濃紺 — TKC ブルーをベースに落ち着きのある深い青に調整）
- サブカラー: `#5b8fc7`（ライトブルー — アクセント補助）
- ベース（背景）: `#ffffff` / `#f5f7fa`（やや青みがかった白）
- テキスト: `#1a1a1a` / `#555555`（見出し / 本文）
- アクセント（CTA）: `#d97706`（オレンジゴールド — 青の補色系で CTA を目立たせる）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 2 | .../6551a085.../logo.png | original | photo | そのまま | 「税理士法人 イカワ会計」ロゴ（横長） |
| 3 | .../6576a5b4.../ (本社TEL 0248-24-3056) | template | text-embedded | 差替 | TKCテンプレボタン。HTML tel: リンクで代替 |
| 4 | .../6551a2d5.../ (郡山TEL 024-953-8260) | template | text-embedded | 差替 | 同上 |
| 5 | .../65603c41.../ (ごあいさつ) | template | text-embedded | 差替 | HTML 見出しで代替 |
| 6 | .../656040b0.../office1.jpg | original | photo | そのまま | 事務所外観（建物）|
| 7 | .../656040b3.../office2.png | original | photo | そのまま | 事務所看板（税理士法人イカワ会計）|
| 8 | .../656040b0.../office3.png | original | photo | そのまま | 応接室1 |
| 9 | .../656040b0.../office4.png | original | photo | そのまま | 応接室2 |
| 10 | .../6551b563.../ (PAGE TOP) | template | text-embedded | 差替 | CSS で代替 |
| 11 | .../6551b6ec.../logo | original | photo | 重複 | 2番と同じロゴ |
| 12 | .../6551b8dc.../ (お問い合わせ) | template | text-embedded | 差替 | ボタンテキストで代替 |
| 13 | .../65769fd7.../ (本社TEL) | template | text-embedded | 差替 | 重複 |
| 14 | .../6551b7ef.../ (郡山TEL) | template | text-embedded | 差替 | 重複 |
| 15 | .../6551b675.../ (TKC全国会) | template | icon | そのまま（Footer小さく）or CSS代替 | 差替で統一 |
| 16 | connect.facebook.net/... | tracking | icon | 不要 | Facebook tracking |
| 17-18 | .../6552f9ba.../ (ビジネスを支える、信頼の良きパートナー) | original | text-embedded | 差替 | テキストは Hero 見出しで使用 |
| 19-21 | .../material/lib01/65482648.jpg etc | stock | photo | 差替 | CSS背景のストック画像 |
| 22 | .../6551c8bd.../ (経営革新等支援機関とは) | template | text-embedded | 差替 | ボタン代替 |
| 23 | .../6551c8c0.../ (金融機関の皆様へ) | template | text-embedded | 差替 | ボタン代替 |
| 24 | .../6551c8c3.../ (料金について) | template | text-embedded | 差替 | ボタン代替 |
| 25 | .../6551c8c6.../ (セミナー案内) | template | text-embedded | 差替 | ボタン代替 |
| 26-31 | .../design/images/bnr-fixed/... | template | text-embedded | 差替 | バナー類 |
| 32 | .../6551c08d.../ (alt: 事務所の経営理念について / 実体: 羅針盤) | stock | photo | 差替 | ストック画像（注意: alt と実体不一致）|
| 33 | .../jiririta2012_02.jpg (自利利他の書) | template | text-embedded | 差替 | TKC テンプレ素材 |
| 34 | .../56fb41e3.../omakase.jpg | template | photo | 差替 | TKC 全国会大会写真 |
| 35 | .../material/lib01/64321844.jpg | stock | photo | 差替 | CSS背景 |
| 36-47 | .../6552d.../ (サービスアイコン群) | template | text-embedded / icon | CSS/SVG 代替 | 全て文字焼込みアイコン |
| 48-53 | .../material/lib01/*.jpg | stock | photo | 差替 | CSS背景のストック |
| 54-55 | .../570cbf.../ (経営革新セミナー2006) | original | photo | 差替（古すぎ） | 2006年撮影、古く差替推奨 |

## 引き継ぎ画像（ローカル化対象）

| ファイル名 | URL | 用途 |
|---|---|---|
| logo.png | https://www.tkcnf.com/library/570b87d949122c4d04b43c52/6551a085dd9183574cb1d7e8.png | ヘッダー / フッターロゴ |
| office-exterior.jpg | https://www.tkcnf.com/library/570b87d949122c4d04b43c52/656040b07f67feec41f7367b.jpg | 本社外観（about セクション） |
| office-sign.png | https://www.tkcnf.com/library/570b87d949122c4d04b43c52/656040b3a4de923506fc17fd.png | 看板（about セクション） |
| office-room1.png | https://www.tkcnf.com/library/570b87d949122c4d04b43c52/656040b04beb4578612a24a6.png | 応接室（about セクション） |
| office-room2.png | https://www.tkcnf.com/library/570b87d949122c4d04b43c52/656040b0cdffef3606f04ddb.png | 応接室別アングル（about セクション） |

## 判定サマリ
- **純写真で価値があるのは 5 枚**（ロゴ + 事務所外観/看板/応接室×2）
- **TKC テンプレ素材は全て差替**
- 「自利利他」の書は TKC 共通素材のため引き継がない → 経営理念セクションは HTML テキストで表現
- Hero 背景は Unsplash（ビジネス/オフィス系）で差替
- サービスアイコンは Unicode / SVG で代替
