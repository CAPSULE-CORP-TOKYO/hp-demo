# 分析結果 — L-1864 税理士法人イカワ会計

## アーキタイプ
名前: **A: モダンミニマル**（B: 伝統重厚のニュアンスを一部取り入れる）
根拠:
- 業種は税理士法人（士業・権威系）。TKC 系テンプレートの青ベース、キャラクターイラスト、縦長一本レイアウトは「古臭い・情報設計未整理」と診断済み
- 創業平成4年、所長は TKC 東北会会長経験等の権威系経歴。法的信頼を訴求
- 情報量が多め（所属団体、経歴、TKC 行動指針、サービス詳細）→ ミニマルに整理しつつ、権威性のためセリフ系見出しをワンポイントで採用
- 福島県の地方士業。過度にモダンすぎると地元中小企業に敷居が高いので、ウォーム要素（事務所写真）も活用

## カラーパレット
- メインカラー: `#1b3a6b` (TKC 系の青を継承、深く引き締める)
- サブカラー: `#f4f6fa` (クールライトグレー — 背景)
- アクセントカラー: `#c9a45c` (権威感のあるゴールド — CTA/見出しライン)
- 補助テキスト: `#4a5568` / `#1a202c`

**根拠**: 元サイトのメインカラーは TKC 系の青系（#1c3f7c 近辺）。色相を維持しながら、彩度を落としてモダン感を出す。ゴールドアクセントで「伝統的な士業の信頼感」を補完。

## フォント
- 見出し: Noto Serif JP (700) — 権威性
- 本文: Noto Sans JP (400, 500)
- 英字小見出し: Inter (500)

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | btn-sp-menu.png | template | icon | CSS/SVG 代替 | テンプレのハンバーガー |
| 2 | 6551a085... png (税理士法人イカワ会計) | original | text-embedded | そのまま | 会社ロゴ（社名文字入り）。企業固有ロゴなので採用 |
| 3 | 6576a5b4... png (本社 TEL) | template | text-embedded | 差替 | テキスト焼込 |
| 4 | 6551a2d5... png (郡山 TEL) | template | text-embedded | 差替 | テキスト焼込 |
| 5 | 65603c41... png (ごあいさつキャラ) | original | diagram | **差替** | 所長キャラクターイラスト。診断で「古臭い」と指摘。Unsplash 差替 |
| 6 | 656040b07f67feec41f7367b.jpg (事務所外観) | original | photo | **そのまま** | 事務所の白い建物外観。採用 |
| 7 | 656040b3a4de923506fc17fd.png (看板) | original | photo | **そのまま** | 黄色い「税理士法人イカワ会計」看板 |
| 8 | 656040b04beb4578612a24a6.png (応接室) | original | photo | **そのまま** | 会議テーブル（アクリル板あり） |
| 9 | 656040b0cdffef3606f04ddb.png (会議室) | original | photo | **そのまま** | 会議テーブル別アングル |
| 10 | 6551b563... PAGE TOP | template | icon | CSS/SVG 代替 | トップへ戻る |
| 11 | 6551b6ec... ロゴ2 | original | text-embedded | 重複 | ロゴ #2 と同一内容、フッターで使う |
| 12 | 6551b8dc... お問い合わせ | template | text-embedded | 差替 | |
| 13-14 | 6576...65 / 6551b7ef... TEL | template | text-embedded | 差替 | |
| 15 | 6551b675... ＴＫＣ全国会 | template | text-embedded | 差替/不要 | TKC 認定表記は HTML テキストで代替 |
| 16 | connect.facebook.net | template | tracker | 不要 | トラッキング |
| 17-18 | 6552f9ba... (ビジネスを支える、信頼の良きパートナー) | template | text-embedded | 差替 | キャッチ焼込み、Hero は HTML テキスト |
| 19 | 65482648.jpg | template | photo | 差替 | bg |
| 20 | 40655040.jpg | template | photo | 差替 | bg |
| 21 | 79587859.jpg | template | photo | 差替 | bg |
| 22-25 | 6551c8... 経営革新/金融/料金/セミナー | template | text-embedded | 差替 | |
| 26-31 | bnr-invoice/bnr-nensyunokabe | template | text-embedded | 不要 | TKC バナー |
| 32 | 6551c08d... コンパス | stock | photo | 不要 | 汎用ストック |
| 33 | jiririta2012_02.jpg (自利利他書) | original | diagram | **そのまま** | 書道作品、唯一の固有コンテンツ |
| 34 | 56fb41e3... セミナー集合 | original | photo | 不要 | 古いセミナー写真、使わない |
| 35 | 64321844.jpg | template | photo | 差替 | bg |
| 36-47 | service/ 内のアイコン | template | icon | CSS/SVG 代替 | 全て |
| 48-53 | inheritance/fee の bg | template | photo | 差替 | bg |
| 54-55 | seminar 写真 | original | photo | 不要 | 古い・低品質 |

## 差替方針（Unsplash/CSS 代替）

- Hero 背景: Unsplash の office/accounting 系（高品質横長）
- About 付近: 事務所外観（#6）を採用
- Philosophy 付近: 自利利他書（#33）＋ 事務所内観（#8 or #9）
- サービスアイコン: 全て SVG/Unicode で代替
- ロゴ: #2 をそのまま採用

## 差別化ポイント（テキスト由来）

1. **平成4年開業の実績**（30年以上）
2. **TKC 全国会所属、経営革新等認定支援機関**
3. **本社（西白河）＋郡山事務所**の2拠点
4. **「自利利他」の経営理念**
5. **巡回監査**による毎月訪問
6. **創業・相続・事業承継**に強い
7. **書面添付実践**（税理士法第33条の2）
