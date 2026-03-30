# 修正内容メモ — L-494（いさやま税理士法人）

対象ファイル: `index.html`
元サイト: https://www.isasystems.co.jp/
作成日: 2026-03-30

---

## デモバナー

`<body>` 直後に非固定のデモバナーを追加。
背景色 `#555`、白文字、高さ28px。「修正イメージデモ — 株式会社CAPSULE」を表示。

---

## 修正1: 固定お問い合わせバー（CTA改善）✨

- **種別**: CTA改善
- **場所**: ページ最下部に固定表示（`position: fixed; bottom: 0`）
- **内容**:
  - 電話ボタン: `tel:044-953-2386`
  - お問い合わせボタン: `https://www.isasystems.co.jp/お問合せ/`
- **デザイン**: 元サイトのヘッダーカラー `#1e73be` を使用したグラデーション背景。お問い合わせボタンはオレンジ `#ff6b00` で目立たせる。
- **バッジ**: 「✨ 改善1」をバー内に表示
- **body**: `padding-bottom: 56px` を追加し、コンテンツがバーに隠れないようにした

---

## 修正2: 3カラムカードのデザイン改善（デザイン改善）✨

- **種別**: デザイン改善
- **対象**: `#topPr .topPrOuter`（会社概要・業務案内・トピックスの3カラム）
- **追加CSS**:
  - `box-shadow: 0 2px 8px rgba(0,0,0,0.12)` — カード風の影
  - `border-radius: 8px` — 角丸
  - `transition: transform 0.3s ease, box-shadow 0.3s ease` — ホバーアニメーション
  - ホバー時: `transform: scale(1.03)` + 影を強調
- **バッジ**: JSで最初のカード右上に「✨ 改善2」を表示

---

## 修正3: トピックス欄の見やすさ改善（UX改善）✨

- **種別**: UX改善
- **対象**: `#topBlog .infoListBox`（Topics & Information セクション内の記事リスト）
- **追加CSS**:
  - `border: 1px solid #e0e0e0` — 枠線
  - `border-radius: 8px` — 角丸
  - `padding: 18px 20px` — 内側余白
  - `background: #fff` — 白背景
  - `margin-bottom: 16px` — 記事間の余白
  - ホバー時に軽い影 (`box-shadow`) を追加
- **バッジ**: JSでトピックスの見出し `<h2>` 横に「✨ 改善3」を表示

---

## 技術的メモ

- CSS変更は全て `</head>` 直前に `<style>` ブロックとして追加（既存CSSは未変更）
- 新規HTML要素はファイル末尾に追加
- 既存HTML要素の削除・変更なし
- バッジはインラインスクリプトで動的に追加
