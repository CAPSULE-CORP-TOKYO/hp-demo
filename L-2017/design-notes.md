# 分析結果 — L-2017 加藤一彦税理士事務所

## アーキタイプ

名前: **A: モダンミニマル**（B 伝統重厚を軽く融合）

根拠:
- 業種が税理士・会計事務所で、信頼性と権威を訴求する必要がある
- 所長歴の長さ（創業48年、昭和49年税理士登録）・各種役職歴・「自利利他」という理念的キーワードがあり、権威感も重要
- 一方、主な顧客は会津地方の中小企業・個人商店で、スマホ対応・読みやすさ・すっきりした導線が求められる
- 情報量は多めだが「事務所紹介・業務案内・料金・交通案内」と構造化しやすい
- 現行サイト（TKC テンプレ）は古いテンプレ感が強く、ストック合成画像（木々＋地球＋鶴ヶ城）でオリジナル要素が弱い
- → モダンミニマルをベースに、Noto Serif JP を見出しに使い権威感を出すハイブリッド方針

## カラーパレット

現行サイトは TKC テンプレの薄いブルー/グリーン系。色相を継承しつつ、コーポレートブルーに寄せる。

- メイン: `#1e3a5f`（ネイビーブルー — 信頼・税務の権威感）
- サブ: `#eff3f8`（薄いブルーグレー — 背景）
- アクセント: `#c8a35a`（ゴールド — 会津の伝統・格式感、CTA に集中）
- テキスト: `#1a1a1a` / `#555`
- ボーダー: `#d8dde5`

## フォント

- 見出し: Noto Serif JP（700）— 権威・信頼感
- 本文: Noto Sans JP（400 / 500 / 700）— 可読性

## 画像分類

元サイトの画像は **TKC 共通テンプレート素材が大半**、かつ「ストック合成背景（hero）+ テキスト焼込バナー（services）+ ロゴ（テキストのみ）」という構成。オリジナル写真（代表写真、事務所外観、スタッフ写真等）はゼロ。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /library/.../5744188481913ec72e001ff9.png | template | text-embedded | 差替 | 社名のみのテキストロゴ。HTML テキストで代替 |
| 2 | /library/.../575916197d10be6a6732d629.jpg | template | photo (stock合成) | 差替 | 木々＋地球儀＋鶴ヶ城のストック合成画像。Unsplash の会津/鶴ヶ城写真 or 業務関連写真で差替 |
| 3 | /library/.../5744188681913ec72e001ffa.gif | template | text-embedded | 差替 | ニュース用テキスト焼込バナー |
| 4 | /material/lib03/bnr_management-innovation007_a.png | template | text-embedded | 差替 | TKC 経営革新バナー |
| 5 | /material/lib03/bnr_aointroduce015_a.png | template | text-embedded | 差替 | TKC セミナーバナー |
| 6 | /library/.../5744188981913ec72e001ffc.jpg | template | text-embedded | 差替 | セミナー案内バナー |
| 7 | /library/.../5744188a81913ec72e001ffd.jpg | template | text-embedded | 差替 | 経営革新等支援機関バナー |
| 8 | /library/.../5744188c81913ec72e001ffe.jpg | template | text-embedded | 差替 | 「貴社を毎月来訪します」バナー |
| 9 | /library/.../5744188d81913ec72e001fff.jpg | template | text-embedded | 差替 | 「創業の夢をお手伝い」バナー |
| 10 | /library/.../5744188e81913ec72e002000.jpg | template | text-embedded | 差替 | 「同業者比較で貴社を診断」バナー |
| 11 | /library/.../5744189081913ec72e002001.jpg | template | text-embedded | 差替 | 「経営計画の策定支援」バナー |
| 12 | /library/.../5744189181913ec72e002002.jpg | template | text-embedded | 差替 | 「部門別の業績管理をサポート」バナー |
| 13 | /library/.../5744189281913ec72e002003.jpg | template | text-embedded | 差替 | 「会計ソフトで経営をサポート」バナー |
| 14 | /material/lib03/bnr_increase-customer021_a.png | template | text-embedded | 差替 | 建設業バナー |
| 15 | /library/.../5744189581913ec72e002005.jpg | template | text-embedded | 差替 | 相続対策バナー |
| 16 | /library/.../5744189681913ec72e002006.jpg | template | text-embedded | 差替 | 相続税・贈与税バナー |
| 17 | /material/lib02/KFS_01〜05.png | template | diagram/icon | CSS/SVG 代替 | TKC KFS 概念図。不要 |
| 18 | /material/lib02/tkc_logo1.gif | template | icon | CSS/SVG 代替 | TKC ロゴ小アイコン。フッターにテキスト表示 |
| 19 | /design/images/bnr-fixed/bnr-nensyunokabe-pc.png 等 | template | text-embedded | 差替 | 年収の壁バナー |
| 20 | /design/images/bnr-fixed/bnr-invoice-pc1.png | template | text-embedded | 差替 | 電帳法・インボイスバナー |
| 21 | /design/images/common/btn-sp-menu.png 他 | template | icon | CSS/SVG 代替 | メニューアイコン |
| 22 | /material/lib01/*.jpg/png（サブページ大量） | template | stock | 差替 | サブページの汎用ストック素材 |
| 23 | connect.facebook.net/... | template | css-bg | 不要 | FB トラッキング |

**結論**: 元サイトから引き継ぎ可能な「original × photo/diagram」画像は **ゼロ**。引き継ぐ画像はなく、全て差替（Unsplash）または CSS/SVG 代替となる。

**images/ ローカル化対象**: なし

**差替戦略（Unsplash）**:
- ヒーロー背景: 会津若松のシンボル（鶴ヶ城・街並み）または静かな書類/万年筆の士業ムード → `photo-1551434678-e076c223a692`（ノートと万年筆、ビジネス系）または `photo-1450101499163-c8848c66ca85`（会計書類）を候補
- サービスカード: 使わない（アイコン SVG + テキストのみで構成してすっきり見せる）
- Office セクション: 事務所情報カードにマップ等を使う
