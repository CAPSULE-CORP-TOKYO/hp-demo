# 分析結果

## アーキタイプ

**名前**: A（モダンミニマル） + 一部 E（テキストヘビー）寄り
**根拠**:
- 業種: 税理士 + 行政書士（士業／権威＋信頼が求められる）
- 顧客層: つくば市近隣の中小企業・個人事業主・クリニック・社会福祉法人
- 文体: 丁寧語中心、業務内容と所信の説明が主。感情系の装飾少なめ
- 情報量: 業務案内・事務所紹介・経営理念・料金・お知らせ・交通案内。典型的な士業サイト
- 所長略歴・所属団体等の読み物要素あり（E寄り）
- 強み訴求: 「ここに相談すれば、だいたいの事は片づく」「総合的サービス」「司法書士・社労士・弁護士と連携」
→ 権威感を失わない落ち着いたモダンミニマル。大判ヒーロー + 余白 + 読みやすいカード型で情報を整理する。

## カラーパレット

元サイトは紺（TKC テンプレ定番）を基調にした古典的士業配色。色相を継承しつつ現代化:

- メイン: `#0F2B5C`（ディープネイビー。元サイトのヘッダー紺を踏襲）
- サブ: `#F5F7FA`（薄いブルーグレー、背景用）
- アクセント: `#C9A15B`（落ち着いたゴールド。士業の信頼感・権威感を補強。CTA ボタンに集中）
- テキスト: `#1A202C`（ほぼ黒）
- 罫線/微細: `#E2E8F0`

60-30-10: white/grey 60% / navy 30% / gold 10%。

## 画像分類

| # | URL / ファイル | 出自 | 適性 | 処理 | 備考 |
|---|---|---|---|---|---|
| 1 | library/.../5717104c...jpg (hero.jpg) | stock | photo | **差替** | スーツ＋電卓＋ノートの典型テンプレストック。TKC 系テンプレ素材 |
| 2 | library/.../571710575a...png (philosophy.png) | original | text-embedded | **差替** | 「わたしたちにお任せください！」文字焼込＋集合写真。HTML 見出しで再構成 |
| 3 | library/.../pic0.jpg (office.jpg) | original | photo | **そのまま引き継ぎ** | 筑波山を望む地域風景写真（つくば市固有性あり）。About/Access セクションで使用 |
| 4 | library/.../571710555a...gif (office_extra.gif) | template | illustration | **差替** | イラストキャラ（大工・医師・シェフ等）。業態紹介のテンプレイラスト |
| 5 | material/lib03/bnr_aointroduce015_a.png | template | text-embedded | **差替** | TKC 経営支援セミナー2018 バナー |
| 6 | material/lib02/KFS_0x.png (x5) | template | text-embedded | **差替** | KFS 説明スライド |
| 7 | library/.../571710585a...jpg (free1.jpg) | original | text-embedded | **差替** | 出張後継者塾案内（チラシ画像。テキストはHTMLで掲載済） |
| 8 | library/.../5717105a...gif (free1b.gif) | original | text-embedded | **差替** | 後継者塾カリキュラム表 |
| 9 | library/.../5717105c...jpg (free2a.jpg) | original | document | **差替** | NPO 法人論文の1ページ目画像 |
| 10 | library/.../5717105d...jpg (free2b.jpg) | original | document | **差替** | 論文の表紙 |
| 11+ | bnr_fixed/*.png, tkc-menu7/8/2 バナー群, icon-*.png, btn-sp-menu.png, etc. | template | text-embedded/icon | **差替 / CSS代替** | TKC テンプレバナー・アイコン群。引き継ぐ価値なし |
| N | connect.facebook.net/... | tracking | pixel | **除外** | FB トラッキングピクセル |
| N | images/bg-pat-A001.png | template | pattern | **差替** | 背景パターン、現代風 CSS グラデに置換 |

### ローカル化対象（Phase 5-0 でダウンロード）

- `office.jpg`（既にダウンロード済み: `images/office.jpg`） — About / Access セクションの視覚要素として利用

**他はすべて差替または不要**。TKC 固有画像（menu2, menu7, menu8, bnr_useful 等）は引き継がない。

### 差替先方針

- ヒーロー: Unsplash の士業/ビジネス系の落ち着いた写真（office desk, pen, documents などの 1 枚）
- About/Access: `images/office.jpg`（筑波山風景） + Unsplash 補助画像
- サービス / 経営理念 / 料金 / 交通 / お知らせ: 画像は使わずアイコン (Unicode/SVG) + カード型 UI
