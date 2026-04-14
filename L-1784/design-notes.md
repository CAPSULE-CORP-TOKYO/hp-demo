# 分析結果 (L-1784)

## 事務所
- 税理士法人 奥州会計 熊谷徹哉事務所
- 岩手県一関市 / TKCテンプレートベース

## アーキタイプ
- 名前: **A: モダンミニマル** + Bの重厚感を少し取り入れる
- 根拠:
  - 業種が税理士法人（士業・権威系）
  - 元サイトは TKC 緑基調の典型的テンプレだが、訴求文は「関与先企業の繁栄は私たちの喜びです」「自利利他」等で知的・伝統的
  - 情報量は多めだが構造化可能（事務所概要・サービス・経営理念・アクセス）
  - モダンミニマルで「信頼できる税理士法人」感を出し、見出しにセリフ（Noto Serif JP）を差し込むことで士業としての品格を付加

## カラーパレット
- メイン: `#2f6b3e`（深緑 — 元サイトの緑を継承、落ち着いた色相に調整）
- サブ: `#f4f7f2`（薄いベージュグリーン — 背景）
- ダーク: `#1a1a1a`（本文テキスト）
- アクセント: `#c89a3a`（金茶 — CTA・ライン装飾。士業としての品格）
- Base テキスト: `#2a2a2a`
- Muted: `#6b6b6b`

60-30-10:
- 60% #ffffff / #f4f7f2（background）
- 30% #2f6b3e（primary）
- 10% #c89a3a（accent / CTA）

## フォント
- 見出し: Noto Serif JP (weight 600-700)
- 本文: Noto Sans JP (weight 400-500)

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | btn-sp-menu.png | template | icon | CSS/SVG代替 | ハンバーガーアイコン |
| 2 | 607ea0ea...png (熊谷会計ロゴ) | original | text-embedded | **そのまま引き継ぎ** | 事務所ロゴ（例外的に引き継ぐ） |
| 3 | 6082a695...jpg (FX hero) | template | text-embedded | 差替 | TKCテンプレ焼込画像 |
| 4 | 5a436505...gif | template | unknown | 差替 | テンプレ素材 |
| 5 | 6086a035...jpg | template | text-embedded | 差替 | TKCプロモ |
| 6 | 5b90c9fe...png | template | text-embedded | 差替 | TKCプロモ |
| 7-18 | library/*.png,gif (TKCサイドメニューバナー) | template | text-embedded | 差替（CSSボタン化） | サイドメニュー |
| 19-24 | bnr-invoice/nensyunokabe | template | text-embedded | 差替 | TKCグローバルバナー |
| 25 | 28149588.jpg (葉っぱ背景) | template | photo | 差替 | TKC共通BG |
| 69 | 571707705a...gif (地図) | original | diagram | **そのまま引き継ぎ** | 固有地図 |
| 70 | 5717076d5a...png (自利利他書) | original | diagram | **そのまま引き継ぎ** | 固有書 |
| 71 | 5717076e5a...png (TKC集合写真) | template | text-embedded | 差替 | テンプレ集合写真 |

## 引き継ぎ画像（ローカル化対象）
1. `607ea0ea00aaa84d049e5b93.png` → images/logo.png
2. `571707705a982b652600110a.gif` → images/map.gif
3. `5717076d5a982b6526001108.png` → images/jiri-rita.png

## 差替方針（非引継画像）
- Hero 背景: Unsplash 税理士系画像（office, consultation 系）
- Services カードアイコン: SVG で統一
- About 写真: Unsplash 事務所系画像
