# 分析結果 — L-1881 福島県相続相談センター

## アーキタイプ
名前: **E: テキストヘビー**（士業解説系）＋ A のミニマル要素を補助的に混ぜる

根拠:
- 相続という重いテーマを、ガイドブック配布という文脈で丁寧に解説する情報量の多い LP
- 代表者メッセージ・FAQ・目次・プロフィール・事務所概要など、読み物要素が中核
- 顧客層は高齢者〜その子世代（40〜60代）で、可読性と信頼感が最優先
- 元サイトは緑系で親しみやすさを出しているため、伝統重厚（B）ではなく読みやすさ重視のテキストヘビー＋モダンミニマルの折衷
- 本文は Noto Sans JP 主体、見出しは Noto Serif JP で格式を少し加える

## カラーパレット
元サイトは緑基調（ガイドブックの木／葉のモチーフ）。色相継承。

- メイン: `#3E7C4F`（深緑、見出し・ヘッダー）
- サブ: `#E8F4EA`（薄緑、セクション背景）
- テキスト: `#1F2A24`（ほぼ黒、本文）
- アクセント: `#D98E2B`（山吹、CTA ボタン — ガイドブック本体の山吹色を拾う）
- 背景ベース: `#FFFFFF`

60-30-10 法則:
- Base (white) 60%
- Primary (deep green + pale green) 30%
- Accent (山吹) 10% — CTA に集中

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../LPtop.jpg | template | text-embedded | 差替 | 「無料プレゼント実施中」のキャッチコピー焼込バナー。Hero で使わず CSS ビジュアルで構成 |
| 2 | .../img-nayami-e1630775726426.png | stock | photo | 差替 | 悩むビジネスマンのストック画像 |
| 3 | .../booksample001.jpg | template | text-embedded | 差替 | ガイドブック内部サンプル（他事務所向けテンプレ） |
| 4 | .../booksample002.jpg | template | text-embedded | 差替 | 同上 |
| 5 | .../2705.svg (✅ emoji) | stock | icon | CSS/SVG 代替 | Unicode ✓ で代替 |
| 6 | .../booksample003.jpg | template | text-embedded | 差替 | 同上 |
| 7 | .../booksample004.jpg | template | text-embedded | 差替 | 同上 |
| 8 | .../booksample005.jpg | template | text-embedded | 差替 | 同上 |
| 9 | .../unnamed-file.jpg | template | photo | 差替 | ガイドブック本体モック。表紙に「司法書士 相続一郎事務所」と他事務所名が焼き込まれている完全テンプレ素材 |
| 10 | .../moisjikomi-300x200.jpg | stock | photo | 差替 | キーボード打鍵のストック画像 |
| 11 | .../kakuninmail-300x200.jpg | stock | photo | 差替 | スマホとメール封筒のストック画像 |
| 12 | .../yuusou-300x216.jpg | stock | photo | 差替 | ポストと封筒のストック画像 |
| 13 | .../6969c6...-300x200.jpg | stock | photo | 差替 | 女性相談員のストック画像 |
| 14 | .../mr-aoki.jpg | **original** | **photo** | **そのまま** | 代表社員・青木大氏の本物写真（スーツ姿・正面）。唯一の固有資産 |
| 15 | .../icon-QA.png | stock | icon | CSS/SVG 代替 | FAQ アイコンは SVG で代替 |

### 引き継ぐ画像（ローカル化対象）
- `mr-aoki.jpg` のみ

### ビジュアル構成方針
- Hero: テキスト中心＋深緑グラデーション＋抽象的な葉モチーフ SVG で「ガイドブック無料プレゼント」を訴求（LPtop の焼込を使わず再構成）
- 悩みセクション: アイコン（SVG）＋テキストカード
- ガイドブック特徴紹介: アイコン＋テキストで統一
- プロフィール: mr-aoki.jpg（丸型クロップ）＋ メッセージ本文
- お届けの流れ: 番号付きステップ UI（CSS）
- FAQ: アコーディオン（details/summary）
- お問い合わせ: フォームモック＋事務所概要
