# 分析結果 — L-1823 氏家公認会計士税理士事務所 / 中央綜合税理士法人 水沢事務所

## アーキタイプ
**A: モダンミニマル**（士業・コンサル）

根拠:
- 業種は公認会計士・税理士事務所（士業）
- 顧客層は地域の法人経営者（奥州市中心に170社強）
- 文体は論理的・解説的（CVP分析、PDCA、管理会計など専門性を訴求）
- 元サイトは茶系木目調の古典3カラムテンプレで情報過多。リデザインでは余白と階層を整え、プロフェッショナル感を強める
- 伝統色は弱く、むしろ「管理会計・データ駆動」の近代的な方向性が所長メッセージから読み取れる

## カラーパレット

元サイトは茶×クリームの木目調だが、主要ヘッダー/フッターはダークブラウン、アクセントに赤系。
ただし所長の専門領域（管理会計・データ志向）とモダンミニマル方針に合わせて、**青系を主軸としたプロフェッショナルパレット**に再整理する。元サイトのロゴ（logo.png / company_logo.png）は青系（#2E85C9 前後）であり、この色相を継承する根拠となる。

- メイン（primary）: `#0B3D66`（ダークネイビー、ロゴの青を深めたブランドカラー）
- サブ（secondary）: `#2E85C9`（ロゴ準拠のブライトブルー）
- アクセント（accent）: `#C9302C`（CTA、元サイトの赤系帯を継承）
- ベース: `#FFFFFF` / `#F5F7FA`
- テキスト: `#1A2230` / `#4A5568`

60-30-10: base 60 / primary 30 / accent 10。CTA ボタンは accent。

## フォント方針
- 見出し: Noto Serif JP（権威・信頼感）
- 本文: Noto Sans JP

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../common/logo.png | original | text-embedded | 差替 | 白背景＋「Ujiie Accountant Office」ロゴ＋青いマーク。ヘッダーでは company_logo.png を優先使用 |
| 2 | .../common/header_contact.png | template | text-embedded | 差替 | TELバナー。HTML テキストで代替 |
| 3 | .../common/btn_header_mail.png | template | text-embedded | 差替 | ボタン画像。CSS ボタンで代替 |
| 4 | .../common/feature01.png | template | text-embedded | 差替 | キャッチ焼込 |
| 5 | .../common/feature02.png | template | text-embedded | 差替 | 同上 |
| 6 | .../common/feature03.png | template | text-embedded | 差替 | 同上 |
| 7 | .../uploads/2016/10/btn_accounting.png | template | text-embedded | 差替 | ボタン画像 |
| 8-9 | .../title_facebook.png / title_twitter.png | template | text-embedded | 差替 | SVGアイコンで代替 |
| 10-15 | .../btn_directorsystem.png 等 バナー群 | template | text-embedded | 差替 | サイドバナー群。カード UI で代替 |
| 16 | .../bg_contact.png | template | text-embedded | 差替 | CTA 帯の背景 |
| 17 | .../btn_mail.png | template | text-embedded | 差替 | CSS ボタンで代替 |
| 18 | .../common/company_logo.png | original | text-embedded | **そのまま** | 「氏家公認会計士税理士事務所」シンボル＋社名ロゴ。ブランド identity なのでヘッダー/フッターロゴとして引き継ぎ |
| 19-20 | .../footer_tel.png / footer_fax.png | template | text-embedded | 差替 | HTML テキストで代替 |
| 21 | .../facebook v4 y2/.../onuUJj0tCqE.png | stock | icon | 差替 | Facebook SDK 残骸 |
| 22 | .../uploads/2016/08/概念図-300x278.jpg | original | diagram | そのまま | 業務分掌概念図。Overview の説明補強 |
| 23 | .../uploads/2016/08/photo_1.jpg | original | photo | **そのまま** | 事務所外観（固有写真） |
| 24 | .../uploads/2016/08/photo_2.jpg | original | photo | **そのまま** | 事務所看板（固有写真） |
| 25 | .../uploads/2016/08/photo_3.jpg | original | photo | **そのまま** | 執務室内観（固有写真） |
| 26 | .../uploads/2016/08/photo_4.jpg | original | photo | **そのまま** | 会議室（固有写真） |
| 27 | .../uploads/2016/08/photo_5.jpg | original | photo | **そのまま** | 第2会議室（固有写真） |
| 28 | .../uploads/2016/08/photo.jpg | original | photo | **そのまま** | 所長・氏家亮氏の顔写真（固有写真） |
| 29 | .../uploads/2024/10/中央綜合税理士法人_logo-300x87.jpg | original | text-embedded | **そのまま** | 経営統合先のロゴ。news-913 の文脈で引き継ぎ |

## ヒーロー画像方針
事務所外観（photo_1.jpg）をヒーロー背景として使用。オーバーレイ暗色を重ね、見出しの可読性を確保。

## 備考
- 元サイトは http → https リダイレクト、SSL 対応済（diagnosis notes 参照）
- 税理士事業は2024年10月に「中央綜合税理士法人 水沢事務所」として法人化済。公認会計士・中小企業診断士業務は個人事務所として継続。両組織の関係を冒頭で明示する
- ブログ更新は 2015 年で停止しているため、リデザインでは「news」（2017-2024の新着情報）のみ前面に出す。古いブログ記事は掲載しない
