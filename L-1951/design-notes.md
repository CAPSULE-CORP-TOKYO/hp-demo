# 分析結果

## アーキタイプ

名前: **A: モダンミニマル（信頼感寄り）**

根拠:
- 業種: 税理士（士業 / 専門職）
- 客層: 福島県郡山市とその近隣の中小企業経営者・個人事業主
- 文体: 実直・説明的・専門用語（巡回監査、自計化、書面添付、記帳適時性証明書 等）
- 情報量: 非常に多い（経営理念・行動指針・業務内容・料金・契約の流れ）
- 元サイト: TKCNF 共通テンプレート（左サイドバーに詰め込み、2013年頃の印象）
- 強み訴求: TKC 全国会会員、巡回監査、黒字決算支援、書面添付
- 所長が平成30年開業、税理士＋FP2級＋農業簿記1級、明確なプロフィール

よって、「A: モダンミニマル」で余白と階層を整え、見出しは Noto Serif JP の重みで権威を出し、本文は Noto Sans JP で可読性を担保する構成にする。

## カラーパレット

元サイトはコーポレートブルー基調（TKC テンプレ標準）。色相を継承し明度・彩度を整える。

- メイン: `#1E3A8A`（深い紺：見出し・主要UI・信頼感）
- サブ: `#2563EB`（ブルー：リンク・アクセント縁取り）
- アクセント: `#F59E0B`（琥珀：CTA ボタンに集中）
- 背景: `#F8FAFC`（ほぼ白のブルーグレー）
- カード背景: `#FFFFFF`
- 罫線: `#E2E8F0`
- 本文: `#0F172A`
- 補助テキスト: `#475569`

60-30-10: `#F8FAFC`/`#FFFFFF` 60% / `#1E3A8A`/`#2563EB` 30% / `#F59E0B` 10%

## 画像分類

全 87 画像を走査したところ、純粋なオリジナル写真・ロゴは **存在しない**。全て TKC 共通テンプレのバナー・イラスト・解説図・ストック画像。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 2 | .../material/lib01/bannerContact01.png | template | text-embedded | 差替 | TKC 共通「お問合せはこちら」バナー |
| 3 | .../material/lib02/tkc_logo1.gif | template | photo | 差替 | TKC 全国会ロゴ（事務所固有ではない） |
| 4-6 | .../material/lib03/bnr_useful001_b.png 他 | template | text-embedded | 差替 | TKC 共通お役立ちバナー |
| 7 | .../material/lib01/1469218.jpg | template/stock | photo | 差替 | TKC 共通の一般風景画像 |
| 8 | .../material/lib01/management_advice_blue03_07.png | template | text-embedded | 差替 | 経営助言解説イラスト |
| 9 | .../material/lib01/59e71711e6bfda3b01a2bebc.jpg | template/stock | photo | 差替 | TKC 共通ストック |
| 10 | .../material/lib02/temp09_pic02.jpg | template | photo | 差替 | TKC テンプレ写真 |
| 11 | .../material/lib03/bnr_menu011_a.png | template | text-embedded | 差替 | TKC 共通バナー |
| 12-17 | .../design/images/bnr-fixed/* | template | text-embedded | 差替 | TKC 固定バナー（年収の壁・インボイス等） |
| 18 | connect.facebook.net/... | tracking | — | 不要 | トラッキング |
| 19-87 | /page3-5 以降および tkc-* ページ | template/stock | 全て | 差替 or 不要 | TKCコラム/ガイド/解説図。事務所固有ではない |

**結論: 引き継ぐ画像はゼロ**。`images/` ディレクトリは作るが中身は空でよい。ヒーローと About セクションの背景は Unsplash の高品質画像（office / business / japan-countryside / accounting）で補う。装飾アイコンは SVG/Unicode で代替。

## 方針

- ヒーローは大判画像 + 半透明オーバーレイ、原文キャッチ「貴社を毎月訪問し、自計化システムの活用と経営改善計画策定により黒字決算を支援します」をそのまま表示（`<br>` や装飾 span で分断しない）
- About / 所長挨拶 / 経営理念 / 業務内容 / 料金 / 契約の流れ / アクセス・事務所概要 / お問合せ CTA を単一ページに縦に流す
- 左サイドバー詰め込みの旧構成を廃し、中央寄せの読み物レイアウトに転換
- モバイルは 768px 以下でハンバーガーナビと下部追従 CTA バー（TEL + お問合せ）
