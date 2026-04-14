# 分析結果

## アーキタイプ

名前: A: モダンミニマル（一部 E: テキストヘビー要素）
根拠:
- 業種: 税理士事務所（士業・権威系）
- 顧客層: 中小企業経営者（白河市周辺）
- 文体: 「自利利他」「租税正義の実現」「自己研鑽」等、理念を語るトーン
- 情報量: 経営理念・行動指針など中程度に情報量あり。所長挨拶は簡潔
- 現状: TKC 全国会の統一テンプレで個性ゼロ、差別化課題
- 方針: 余白・高コントラスト・サンセリフ主体の信頼感ある現代的レイアウト。見出しは控えめに Noto Serif JP を使い権威感を残す

## カラーパレット

元サイトの色相（TKC テンプレの濃紺 + 水色）を継承しつつ、現代化。

- メイン: `#0B3D62`（濃紺: 信頼・税務の堅実さ）— 元 TKC ヘッダ色に近い
- サブ: `#E8EEF3`（淡いブルーグレー: 余白とカード背景）
- アクセント: `#C8A14B`（金/琥珀: CTA・帯要素。士業の権威感）
- テキスト: `#1A1A1A` / `#555555`

## 画像分類

実体確認済み（alt と中身の乖離があるため、全て curl + Read で検証）。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | library/.../63a2b6cb92211f966b73d84e.png（alt: 菊地宏幸税理士事務所） | original | text-embedded | 差替 | 社名＋住所＋TELが焼き込まれたテキスト画像。HTML 側でタイポグラフィ化 |
| 2 | library/.../201206161435_RNE4R.JPG（alt: 空） | **original** | **photo** | **そのまま引き継ぎ** | 3階建てビルに「菊地会計」看板が写る事務所外観の実写真。唯一の固有写真 |
| 3 | library/.../57567a0f860b29695c00171f.png | template | text-embedded | 差替 | TKC「自利利他」書画シンボル |
| 4 | library/.../57567a10860b29695c001720.png | template | text-embedded | 差替 | TKC 全国会集合写真＋「わたしたちにお任せください！」焼込 |
| 5 | material/lib02/temp02_main03.jpg | template/stock | photo | 差替 | TKC テンプレの会議手元ストック画像 |
| 6-x | material/lib02/KFS_*.png | template | text-embedded/diagram | 差替 | TKC KFS 図 |
| 7-x | material/lib03/bnr_*.png | template | text-embedded | 差替 | TKC 共通バナー群（IT導入補助金等）全て焼込テキスト |
| 8-x | design/images/bnr-fixed/*.png | template | text-embedded | 差替 | TKC 固定バナー（インボイス・年収の壁） |
| 9-x | design/images/common/*.png | template | icon | CSS/SVG 代替 | MENU・icon-close・icon-open |
| 10-x | library/.../5656ef25.../*（tkc-monitoring 他） | template | diagram/text-embedded | 差替 | TKC システム解説図 |
| 11-x | library/.../5fe591577ae7d61e74e3e4d0.png | template | text-embedded | 差替 | TKC モニタリング情報サービスバナー |

**結論**:
- 引き継ぎ対象の original 画像: **事務所外観写真 1 枚のみ**（#2）
- 全ての TKC バナー・ロゴテキスト画像は HTML タイポグラフィ + Unsplash で差替
- 他の Unsplash 差替は業種「office / tax / accounting / business consulting / documents」系に統一

## フォント方針

- 見出し: Noto Serif JP（権威感・信頼感）
- 本文: Noto Sans JP（可読性）

## レイアウト方針

- Header: ロゴ（テキスト）+ デスクトップナビ / モバイルハンバーガー
- Hero: 白河の中小企業を支える税理士という立ち位置を全面に。事務所外観写真 or Unsplash（accounting）をビジュアルに
- About（所長挨拶・所属団体）: カード型
- Philosophy（経営理念 3 つ）: 3 カラム縦型カード
- Services（業務案内）: 4 カテゴリのカード
- Office（事務所概要 + 外観写真）: テーブル + 写真ペア
- Access（交通案内 + 住所・TEL）
- News（最新情報）: リスト型
- Footer: 住所 + TEL + コピーライト
- Mobile sticky CTA: TEL + 問合せフォーム
