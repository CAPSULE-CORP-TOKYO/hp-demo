# 分析結果 — L-2069 税理士法人テルス

## 元サイト概要
- 対象 URL: https://gaiaproject.jp/tellus （ガイアグループ傘下の税理士法人テルス）
- 元スクショ: 緑基調・2015年頃のテンプレ、テーブルレイアウト中心、写真は小さなサムネイル、CTA 弱い
- 業種: 税理士法人（会計・税務コンサル）
- 本社: 福島県須賀川市大町442-3（須賀川オフィス）
- 住所・電話一致確認済み: `0248-75-2207`、須賀川本社 DEC-026 OK
- 妥当性: /tellus サブサイト（税理士法人テルス専用ページ）が website。companyName と完全一致

## アーキタイプ
**名前**: A: モダンミニマル（権威系スパイス）
**根拠**:
- 顧客層は中小企業経営者・事業承継ニーズがある層。信頼・権威・誠実さが必須
- 士業（税理士・公認会計士）なのでコンサル感のあるモダンミニマル
- 元サイトの緑基調（ガイアグループ CI）を継承しつつ、余白・サンセリフで現代化
- 伝統重厚（B）ほどの重みは不要だが、見出しに Serif を効かせて信頼感を補強

## カラーパレット
元スクショから抽出（GAIA GROUP の緑を継承）:
- メイン: `#7CB342`（ガイアグリーン — 元サイトのヘッダー緑を継承）
- ダークメイン: `#33691E`（濃い緑、見出し/ヘッダー強調用）
- サブ: `#F5F7F2`（オフホワイト、セクション背景）
- テキスト: `#1F2A24`（ほぼ黒、読みやすさ重視）
- ミュート: `#5A6B62`
- アクセント（CTA）: `#F59E0B`（ウォームオレンジ、CTA 集中）
- ボーダー: `#E4E8DF`

配色方針: 60-30-10（ベース白系 60% / グリーン 30% / オレンジ 10%）

## フォント
- 見出し: Noto Serif JP 600-700（権威と信頼感）
- 本文: Noto Sans JP 400-500
- 数字/英字: Noto Sans JP

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /img/common/tellus_logo.png | original | text-embedded | そのまま引き継ぎ | ブランドロゴ画像、Header に使用 |
| 2 | /img/page/tellus_top.jpg | original | text-embedded | 差替（Unsplash or CSS） | "会計・税務の力で地域経済を支える。" 焼込。HTML の見出しと重複 |
| 3 | /img/page/img_tellus.jpg | stock | photo | 差替 | 四つ葉クローバー＋都市のストック素材、汎用 |
| 4 | /wp-content/.../sukagawaoffice.jpg | original | photo | **そのまま引き継ぎ** | 須賀川本社外観（GAIA GROUP 看板）— 最重要 |
| 5 | /wp-content/.../tokyooffice2-3.jpg | original | photo | そのまま引き継ぎ | 東京オフィス |
| 6 | /wp-content/.../koriyamaoffice4.jpg | original | photo | そのまま引き継ぎ | 郡山オフィス |
| 7 | /img/page/info.png | original | text-embedded | CSS/SVG 代替 | 「業務案内」タイトル画像 |
| 8 | /img/page/info2.png | original | text-embedded | CSS/SVG 代替 | 「企業情報」タイトル画像 |
| その他 | facebook_logo、zeimu_banner 等 | template/icon | 各種 | 不要 | |

## Hero 戦略
- Hero 背景は Unsplash 差替（抽象的な「数字・ビジネス・信頼」系）
- Hero 見出しは原文「会計・税務の力で地域経済を支える。」をそのまま（`<br>` で分断しない）
- サブ見出しは「経営･財務コンサルのガイア･テルスグループ｜福島須賀川」

## セクション構成
1. Header (ロゴ + ナビ + 問い合わせ CTA)
2. Hero (キャッチ + 須賀川本社の示唆 + CTA)
3. About (冒頭の代表挨拶原文)
4. Services (業務案内 + サービス詳細 9項目)
5. Results (実績紹介 A-O 15社)
6. Company (沿革 + 代表社員 + 須賀川オフィス写真)
7. Access (3拠点 + 主要オフィス一覧)
8. Contact (CTA カード + TEL + フォーム誘導)
9. Footer
