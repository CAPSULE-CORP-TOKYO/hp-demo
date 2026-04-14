# 分析結果 — L-1659 タカハシ会計 高橋竹夫税理士・行政書士事務所

## アーキタイプ
名前: **A: モダンミニマル**（補助として B: 伝統重厚 の要素をわずかに採用）

根拠:
- 業種は山形県酒田市の税理士・行政書士事務所。顧客層は中小企業経営者・医療機関・社会福祉法人・公益法人と幅広く、信頼感・権威性・清潔感を重視する BtoB 士業サイト。
- 既存サイトは TKC 系の古いテンプレート（2010年代前半、Nivo Slider、固定幅）で、余白が極端に少なく情報過多。リデザインでは大胆な余白・抑制された色数・サンセリフの読みやすさを重視する。
- 文体は硬めの説明調（業務案内・経営理念共に格式あり）で、流行の「ポップ・親しみやすい」系（C ウォームフレンドリー）は不適。
- 信頼感・格式を少し添えるため、見出しに Noto Serif JP をサブ使用する。

## カラーパレット

screenshot.png から抽出。ヘッダー・サイドナビの濃い紺色と白のコントラストが特徴。
- **メイン（濃紺）**: `#1F3C5A` — ヘッダー・見出し・ロゴ周辺
- **サブ（ライトグレー系）**: `#F4F6F9` — 背景、セクション区切り
- **アクセント（オレンジ寄りのゴールド）**: `#C98A3A` — CTA / 強調下線

ルール: 色相は元サイトの紺 (#1F3C5A 近傍) を継承。アクセントはオリジナルの右下に配置された「バナー色（赤橙系）」の印象を受けて節度あるゴールドに置換。別配色への変更ではなく明度・彩度の調整の範疇。

## 画像分類

トップページ掲載の画像を中心に判定。サブページの TKC テンプレ・バナー類は全て差替または非採用。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | http://www.tkcnf.com/library/57173b500e0f21c90b6634fe/5fe5715f4cd50f00233cecc2.png | original | photo（ロゴ） | そのまま（ローカル化） | タカハシ会計ロゴ |
| 2 | http://www.tkcnf.com/library/57173b500e0f21c90b6634fe/6119ed71d36f73345c1c25a2.jpg | original | photo | そのまま（ローカル化） | 事務所外観（看板寄り） |
| 3 | http://www.tkcnf.com/library/57173b500e0f21c90b6634fe/6119ed7559ff892460b3076f.jpg | original | photo | そのまま（ローカル化） | 事務所外観（別角度） |
| 4 | http://www.tkcnf.com/library/57173b500e0f21c90b6634fe/62c3b976ba805df00565a921.jpg | original | photo | そのまま（ローカル化） | 酒田市 山居倉庫（地元象徴、サイト運営側採用） |
| 5 | http://www.tkcnf.com/library/57173b500e0f21c90b6634fe/62c666aba2c88ec2063250c3.jpg | original | photo | そのまま（ローカル化） | 酒田市 山居倉庫裏手（同上） |
| 6 | http://www.tkcnf.com/material/lib02/tkc_logo1.gif | template | icon | CSS/SVG 代替または除外 | TKC全国会ロゴ（テンプレ共通素材）→ テキストで「TKC全国会会員」と明示 |
| 7 | http://www.tkcnf.com/material/lib03/bnr_menu011_a.png | template | text-embedded | 差替 / 不要 | TKC 共通バナー |
| 8 | http://www.tkcnf.com/design/images/bnr-fixed/bnr-invoice-pc1.png | template | text-embedded | 不要 | 電帳法・インボイス固定バナー |
| 9 | http://www.tkcnf.com/design/images/bnr-fixed/bnr-nensyunokabe-pc.png | template | text-embedded | 不要 | 年収の壁 固定バナー |
| 10 | http://www.tkcnf.com/design/images/common/btn-sp-menu.png | template | icon | CSS 代替 | SP メニューアイコン |
| 11 | http://www.tkcnf.com/design/images/bg/bg-pat-A011.png | template | bg-pattern | 不要 | 背景パターン |
| 12+ | その他サブページの各種バナー・イラスト（TKC全国会素材 / material/lib01 / material/lib03 配下） | template/stock | text-embedded/diagram | 不要 | 全て TKC 共通テンプレ素材のため非採用 |

**引き継ぐ画像は 1〜5 のみ**（ロゴ + 事務所外観2枚 + 山居倉庫2枚）。それ以外は全て TKC 共通テンプレ素材で引き継ぐ価値なし。セクションに追加のビジュアルが必要な場合は CSS グラデ・幾何パターン、または統一性が取れる場合のみ Unsplash から業種的に適した写真を使う。

## デザイン方針まとめ

- ヘッダー: 白背景 + 濃紺ロゴ + シンプルなナビ。モバイルはハンバーガー
- ヒーロー: 事務所外観写真（p1）を背景に overlay、キャッチコピー「Your success is our business / 貴社の発展・繁栄のお手伝いが私たちの仕事です」を配置
- 営業日・最新のお知らせ・業務案内・経営理念抜粋・事務所概要・所長挨拶・アクセス・お問合せの順で構成
- 余白は playbook 通りの 24px / 64-100px
- フォント: Noto Sans JP メイン、見出しのみ Noto Serif JP
- フッター: 事務所名・住所・TEL・TKC全国会会員表記・東北税理士会所属・コピーライト
