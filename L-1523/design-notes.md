# 分析結果 — 佐藤登美子税理士事務所 (L-1523)

## アーキタイプ
名前: **B: 伝統重厚** + **A: モダンミニマル** のハイブリッド（メインは B 寄り）
根拠:
- 山形県山形市の創業昭和58年（1983年）の老舗税理士事務所。40周年を迎えた実績。
- 所長は女性税理士・佐藤登美子氏。経歴・役職の権威性が強い（顧問・理事・総代等多数）。
- TKC 全国会会員。「租税正義の実現」「自利利他」等、仏教哲学に根ざした経営理念。
- クライアントは地域企業（医業・農業・社会福祉法人含む）。保守的でトラストの必要な層。
- 一方で「女性税理士」「親しみやすさ」「創立40周年」等の個性もある。
- よって、明朝体主体の伝統重厚をベースにしつつ、ミニマルな余白設計と現代的レイアウトを組み合わせる。

## カラーパレット
元サイトは青の看板・青のリボン系配色（TKC テンプレート由来）。色相を継承する。
- メイン: `#0d3b66`（深い紺紺青 — 元サイトの青看板ベース）
- サブ: `#f5f6f8`（オフホワイト）
- アクセント: `#c9a35b`（落ち着いたゴールド — 権威と品格の演出、ボタン専用）
- テキスト主色: `#1a1a1a`
- テキスト補助: `#555b66`
- 区切り線: `#e6e8ec`

60-30-10:
- base 60% = #f5f6f8 / white
- primary 30% = #0d3b66
- accent 10% = #c9a35b

## 画像分類

| # | URL（短縮） | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | library/.../571f2b51...121f.gif | original | text-embedded | **そのまま（logomark）** | 佐藤登美子税理士事務所 横書きロゴ。小さく使用 |
| 2 | library/.../6122ed43...dae4.jpg (top2) | original | photo | **そのまま** | 事務所の青い看板（地図目印） |
| 3 | library/.../5f2c9bc4...25fb.png (t4) | original | photo | **そのまま（メインヒーロー）** | 事務所外観＋山形の山々（1280px 広角）★ |
| 4 | library/.../6840d937...d6ea.jpg (t5) | original | photo | **そのまま** | 事務所正面ファサード（白い柱） |
| 5 | library/.../5b1e2257...8923.jpg (office) | original | photo | **そのまま** | 所長 佐藤登美子氏の顔写真 ★ |
| 6 | library/.../576796d8...7056.jpg (map) | original | photo | **そのまま** | 事務所外観（俯瞰、赤屋根） |
| 7 | material/lib02/tkc_logo1.gif | original | icon | **そのまま** | TKC 全国会ロゴ（小） |
| 8 | library/.../5bfe1154...e39a.jpg (seminar1) | original | text-embedded | 差替 | 旧社名横断幕入り、画質低 |
| 9 | library/.../5bfe1183...132f.jpg (seminar2) | original | text-embedded | 差替 | 旧社名横断幕入り |
| 10 | library/.../5bfe11b3...2886.jpg (seminar3) | original | text-embedded | 差替 | 旧社名横断幕、プロジェクター写り込み |
| 11 | library/.../571f2b68...122e.jpg (service) | stock | photo | 差替 | 古いキーボード＋電卓 |
| 12 | library/.../571f2b63...122b.jpg (philosophy) | stock | photo | 差替 | TOKYO STOCKS 新聞＋電卓 |
| 13 | material/lib03/bnr_*.png (多数) | template | text-embedded | 不要 | TKC 共通テンプレバナー |
| 14 | design/images/bnr-fixed/bnr-invoice-pc1.png 等 | template | text-embedded | 不要 | テンプレ固定バナー |
| 15 | design/images/common/btn-sp-menu.png 等 | template | icon | CSS/SVG 代替 | ナビアイコン |

### 引き継ぐ画像（Phase 5-0 でローカル化する対象）

1. `tomiko-logo.gif` ← 571f2b51e2e8177f7b00121f.gif
2. `office-sign.jpg` ← 6122ed43ca85b1a305e1dae4.jpg（青看板）
3. `office-hero.png` ← 5f2c9bc4477c7729594725fb.png（広角ヒーロー）
4. `office-facade.jpg` ← 6840d93745a63d0fb50bd6ea.jpg（正面ファサード）
5. `tomiko-portrait.jpg` ← 5b1e2257ee98ccfb2eee8923.jpg（所長顔写真）
6. `office-aerial.jpg` ← 576796d876f6213f536e7056.jpg（俯瞰）
7. `tkc-logo.gif` ← material/lib02/tkc_logo1.gif

### 引き継がない画像 → 新規リソースで置き換え

- セミナーセクションは **削除**（画質低＋旧社名入り＋情報的価値低）
- 業務案内の視覚補強は CSS/SVG アイコンで代替（電卓・建物等 Unicode 絵文字は使わない。SVG インライン）
