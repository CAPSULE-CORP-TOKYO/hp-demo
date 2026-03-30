# L-483 修正メモ

## 対象サイト
大楽会計事務所（https://www.dairaku-accfirm.com/）

---

## 修正1: CTA（問い合わせ導線）の改善

### 追加した要素

1. **デモバナー**（ページ最上部）
   - 「修正イメージデモ — 株式会社CAPSULE」のグレー帯
   - 控えめなデザインで元サイトの邪魔をしない

2. **CTAバー**（ヘッダー直上）
   - 青系グラデーション背景（元サイトの色調に合わせた `#1a3a6b` 〜 `#2563a8`）
   - 電話番号表示: `03-5797-9487`（電話アイコン付き）
   - モバイルではタップで発信可能（`tel:` リンク）
   - 「無料相談はこちら →」ボタン → お問い合わせフォームへリンク
   - 「✨ 改善ポイント」バッジ付き

---

## 修正2: フォント modernize + 余白改善

### 概要
TKCテンプレートのデフォルトフォント（明朝体+ゴシック混在）を Noto Sans JP に統一し、
見出し・本文の余白とフォントサイズを最適化してモダンな印象に刷新。

### 追加した要素

1. **Google Fonts リンク**（`<body>` 直前に挿入）
   - `Noto Sans JP` (weight: 300, 400, 500, 700)
   - preconnect 付きで読み込み高速化

2. **CSS オーバーライド**（`<style>` ブロック、`<body>` 直前に挿入）
   - フォント: 全要素を `Noto Sans JP, sans-serif` に `!important` で上書き
   - 見出し (h1/h2/h3): `font-weight: 700`, `letter-spacing: 0.02em`, サイズ・余白調整
   - 本文 (p): `line-height: 1.8`, `margin-bottom: 1rem`
   - リスト (li): `line-height: 1.7`
   - セクション間余白: `.row`, `[data-module-type]` に `margin-bottom` 追加
   - フッター: padding 調整

3. **デモバナー更新**
   - 固定表示 (position: fixed, top: 0) に変更
   - `body` に `padding-top: 30px` を追加してコンテンツが隠れないよう調整

### 変更しなかった要素
- 画像の width/height
- テーブルレイアウト
- ナビゲーション構造
- 配色（元サイトの青系を維持）
- HTML構造全般

### CSS セレクタ一覧

| セレクタ | 変更内容 |
|---------|---------|
| `body, html, div, span, p, a, li, td, th, ...` | font-family を Noto Sans JP に |
| `h1, h2, h3` | font-weight, letter-spacing, font-size, margin 調整 |
| `p` | line-height: 1.8, margin-bottom: 1rem |
| `.row` | margin-bottom: 1.5rem |
| `[data-module-type="container"]` | margin-bottom: 2rem |
| `[data-module-type="banner"]` | margin-bottom: 2rem |
| `.row.flex-box` | margin-bottom: 2rem |
| `.footer-link-005-blue` | padding-top/bottom: 1.5rem |

---

### 技術的な修正方法
- `<body>` タグの直前に Google Fonts `<link>` タグと `<style>` ブロックを追加
- `<body>` タグの直後にデモバナー要素を挿入
- 元サイトの既存要素は一切変更・削除していない
- CSS は全て `!important` 付きで確実に適用

### 修正日
2026-03-30
