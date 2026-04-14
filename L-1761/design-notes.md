# 分析結果 — L-1761 こずかた税理士法人

## アーキタイプ
名前: **A: モダンミニマル**（見出しに明朝体のアクセントを許容）
根拠:
- 業種は税理士法人（士業）で、信頼性・権威性の訴求が重要
- 元サイトは TKC テンプレ、青紫基調の 2 カラム旧レイアウト（2010s-mid）
- コンテンツは硬めの書き言葉（経営理念、行動指針等）
- 写真は一切 original がなく、全て TKC テンプレのストック画像
- モダンに再構築する際は、大胆な余白・サンセリフ主体・高コントラスト・写真差替えが妥当
- 見出し（所長挨拶、経営理念）には Noto Serif JP を部分的に用いて士業らしい格を出す

## カラーパレット
元サイトは青紫（#4B3F99 系）基調。現代的に調整。
- メイン: `#1E3A8A`（濃紺）— 信頼感、士業定番。元の青紫を色相寄せ
- サブ: `#475569`（スレート）— 本文・補助
- アクセント: `#D97706`（琥珀色）— CTA・ハイライト（10%）
- 背景: `#FFFFFF` / `#F8FAFC`（薄グレー）
- テキスト: `#0F172A`（ほぼ黒）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガーは SVG |
| 2 | tkc_logo1.gif | template | text-embedded | 差替 | TKC 全国会ロゴ画像 → テキストで「ＴＫＣ全国会会員」表記 |
| 3 | bannerContact01.png | template | text-embedded | 差替 | お問合せバナー → CSS ボタン |
| 4 | temp02_main01.jpg（手帳とペン） | template | photo | 差替 | TKC テンプレのストック、原文に紐付かない汎用写真 |
| 5 | temp02_main02.jpg（ビジネスマン集合） | template | photo | 差替 | TKC テンプレのストック写真 |
| 6 | temp02_main03.jpg（手元で書類） | template | photo | 差替 | TKC テンプレのストック写真 |
| 7 | temp02_pic01.jpg（ガッツポーズの男女） | template | photo | 差替 | TKC テンプレのストック写真 |
| 8 | temp02_pic02.jpg | template | photo | 差替 | TKC テンプレのストック写真 |
| 9 | KFS_01.png - KFS_05.png | template | text-embedded | 差替 | 「KFSでお手伝い」等テキスト焼込バナー |
| 10 | bnr-invoice-pc1.png / bnr-nensyunokabe-pc.png | template | text-embedded | 差替 | 固定バナー（電帳法・年収の壁） |
| 11 | icon-open/close.png | template | icon | CSS/SVG 代替 | アコーディオンアイコン |
| 12 | bg-pat-A008.png | template | diagram | 差替 | 背景パターン |

**結論**: オリジナル写真ゼロ。全画像を Unsplash の「tax / accounting / office / consulting」系の高品質画像に差替。ローカルダウンロード対象は **なし**（`images/` ディレクトリは空で OK）。
