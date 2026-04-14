# 分析結果 — L-1898 税理士法人AKJパートナーズ つくばオフィス

## アーキタイプ
名前: A（モダンミニマル）+ B（伝統重厚）のハイブリッド — エグゼクティブ向け権威系モダン

根拠:
- 顧客層: IPO 支援・IFRS 導入支援・シンガポール進出支援を扱う、上場準備中〜上場企業・M&A 案件を持つ成長企業
- 既存サイトのトーン: ダークネイビー × ゴールドの落ち着いたエグゼクティブ感、エントランス写真がヒーロー、品のあるコーポレート印象
- 文体: フォーマル・専門的（「企業は…『信頼』を得て成り立ちます」のような格調の高い言い回し）
- 写真素材: 高品質なオフィス内観写真（エントランス・図書室・会議室）が複数ある
- 旧サイトの問題: モバイル非対応、アイコン+テキストリストの2015-2018年型、ヒーロー以外に視覚的見せ場なし

→ ダークトーンの威厳・落ち着き（B）を保ちつつ、大判ヒーロー・余白・サンセリフ系日本語で現代化（A 寄り）。装飾過剰にせず、写真と空白で語らせる。

## カラーパレット
- メイン (Primary): `#1C2C42`（ダークネイビー、既存ヘッダー色を継承）
- ベース (Base): `#FAF8F4`（オフホワイト、品のあるベージュ寄り）
- アクセント (Accent): `#B68A4A`（ゴールド、既存サイトのゴールドアクセントを継承）
- テキスト: `#1C2C42`（本文）/ `#5A6271`（サブ）
- ボーダー: `#E5E0D6`

60-30-10:
- ベース（オフホワイト）60% — 背景全般
- プライマリ（ダークネイビー）30% — ヘッダー、フッター、見出し、ヒーローオーバーレイ
- アクセント（ゴールド）10% — CTA ボタン、リンクホバー、見出しアンダーライン

## フォント
- 見出し: Noto Serif JP（明朝、権威感）
- 本文: Noto Sans JP（読みやすさ）
- 数字・英字: 同上

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | header-logo.png | original | photo | そのまま | AKJ Partners ロゴ（透過 PNG、テキストロゴ＋カラーマーク） |
| 8 | mainvisual01.png | original | photo | そのまま | エントランスホール写真（高品質） |
| 10 | mainvisual02.png | original | photo | そのまま | 図書室・打合せスペース |
| 12 | mainvisual03.png | original | photo | そのまま | 会議室（大型ボードルーム） |
| 14 | mainvisual04.png | original | photo | そのまま | 図書室・読書スペース |
| 9,11,13,15 | copy01-04.png | original | text-embedded | 差替（HTML テキスト化） | キャッチコピー焼込画像 |
| 2-7 | nav-*_off.png | template | icon | CSS/SVG 代替 | グローバルナビアイコン |
| 16-18 | title-whatsnew/info/seminar.png | original | text-embedded | 差替（HTML テキスト化） | お知らせセクション見出し |
| 19-46 | nav-practice/*, nav-footer/* | template | icon | CSS/SVG 代替 | 業務内容アイコン |
| 47 | mark-sgs.png | original | photo | そのまま | ISO/SGS 認証マーク |
| 52,65,97,127 | pagevisual-*.png | original | text-embedded | 差替 | ページタイトルバナー（テキスト焼込） |
| 54 | sign.gif | original | photo | そのまま | 代表 山本成男 署名 |
| 57 | sgs.png | original | photo | そのまま | ISO 認証ロゴ |
| 58 | fts_logo.jpg | original | photo | そのまま | fon to share ロゴ |
| 59 | 2024女性活躍-1.png | original | photo | そのまま | 女性活躍推進企業データベース |
| 60 | bnr-tokyo.jpg | original | text-embedded | 不要 | TOKYO 働き方改革宣言（つくばオフィスでは無関係） |
| 102 | pagevisual-access-tsukuba.png | original | text-embedded | 差替 | アクセスページタイトル |
| 103 | map_tsukuba.png | original | diagram | そのまま | つくばオフィス周辺地図 |
| 134-140 | title-mainvisual-*.png | original | text-embedded | 差替 | ページタイトル画像 |
| その他 (62-96, 100-133, 135-140 等) | template/original mix | various | 多くは差替 or 不要 | サブページの装飾画像、タイトル画像 |

### 引き継ぎ確定リスト（Phase 5-0 でローカル化）
1. `header-logo.png` → `images/header-logo.png`
2. `mainvisual01.png` → `images/mainvisual01.png`（ヒーロー）
3. `mainvisual02.png` → `images/mainvisual02.png`（About / オフィス紹介）
4. `mainvisual03.png` → `images/mainvisual03.png`（Services 背景 or About 補助）
5. `mainvisual04.png` → `images/mainvisual04.png`（補助 or 不要）
6. `map_tsukuba.png` → `images/map_tsukuba.png`（Access 地図）
7. `sign.gif` → `images/sign.gif`（代表署名 — 法人概要）
8. `sgs.png` → `images/sgs.png`（ISO 認証）

合計 8 枚。テンプレ icon・テキスト焼込・ページ装飾・本店他拠点固有画像は引き継がない。

## つくばオフィス特化方針
- リードは「税理士法人AKJパートナーズ つくばオフィス」。本店サイトは法人全体だが、デモはつくばオフィス向けに構成する
- ヘッダー・タイトルは「税理士法人AKJパートナーズ つくばオフィス」
- 連絡先（電話・住所）はつくばオフィスを採用（029-868-7033 / 茨城県つくば市竹園1-6-1 つくば三井ビルディング 18F）
- 注: 既存サイト表記は「つくばビルディング」だが leads.json は「つくば三井ビルディング」。両者をどちらも正本扱いし、HTML には leads.json の正式名を採用しつつ、既存サイトの言い回しも併存させない
- 業務内容・法人概要・代表挨拶・パーパスは本店サイトの原文を使用（AKJ Partners 全体の理念は支店共通として正当）
- アクセス情報はつくばオフィス専用ページ (access/tsukuba-office/) の原文を使用
- ニュース・採用は AKJ Partners 全体のものを表示

## 余白・コンポーネント方針
- ヒーロー: 全幅、暗いオーバーレイ + 中央に明朝見出し（焼込画像 copy01 のテキストを HTML 化）
- 数字訴求: 公認会計士9人/税理士16人/...の保有資格を 6カラムカウンターで視覚化
- Services: 5サービス（Audit / Tax & Account / FAS / Human Resource / Others）をカード型で並列
- Specialties: IFRS / SO / IPO / 相続 / 医療 / シンガポール / 移転価格 / 国際税務 / 外資 / 個人 を 2カラムリスト
- Access: 地図画像 + 住所・電話・最寄駅
- News: 直近3件
- フッター: 拠点一覧（東京/つくば/福岡/シンガポール/サテライト）
