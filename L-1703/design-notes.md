# 分析結果 — L-1703 高山孝治税理士事務所

## アーキタイプ
名前: **B: 伝統重厚** をベースに、**A: モダンミニマル** の余白感を組み合わせる

根拠:
- 業種: 税理士（士業）、所長は元国税局・税務署勤務の定年退職者、東北税理士会新庄支部所属
- 文体: 丁寧・一人称・「ふるさと新庄」への想い・わび・さび、国内旅行、ぐい呑みコレクション等の趣味 → 落ち着きと人柄を伝える必要
- 客層: 地元山形県新庄市の中小事業者・個人事業主・相続相談者
- 現状: 2005年デザインで極めて古い → 士業にふさわしい信頼感・権威感を表現しつつ、現代的な余白・可読性を確保
- 情報量: 挨拶・事務所案内・業務内容が中心。ニュースや頻繁更新なし
- 写真: 代表（所長）の顔写真 1 枚のみがオリジナル純写真。他はテンプレボタン画像

方針: Noto Serif JP 主体（見出し）、Noto Sans JP（本文）。深緑 + アイボリー + 金アクセントで士業らしい信頼感。大判ヒーローにストック画像（山形・新庄の自然 or 書斎／事務所感）を使い、代表写真は About セクションで主役にする。

## カラーパレット

元サイトは黒背景 + マゼンタ/青/緑/黄/オレンジのボタンという配色で、一貫したブランドカラーは存在しない（テンプレ寄せ集め）。そのため「元サイトの色相を継承」という原則はほぼ適用不可。士業として最も違和感のない深緑＋生成りベースを採用する（業種継承ルールに寄せる）。

- メイン（primary）: `#1f3b2d`（深緑 — 信頼・落ち着き・東北の森）
- サブ（base）: `#f6f2e7`（生成り・和紙調）
- アクセント: `#b8862b`（燻金 — 士業らしい格式）
- テキスト: `#2b2b2b`
- ミュート: `#6b6b6b`
- 罫線: `#d9d3c2`

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../20061108105001_a_ilst146.gif | template | icon | CSS/SVG 代替 | テンプレイラスト |
| 2 | .../space.gif | template | icon | 不要 | スペーサー |
| 3-8 | rays-counter.com/* | template | icon | 不要 | アクセスカウンター |
| 9 | .../bana-takayama02.gif | original | text-embedded | 差替 | 社名焼込バナー |
| 10 | .../ani_mail.gif | template | icon | CSS/SVG 代替 | アニメメールアイコン |
| 11 | media.fc2.com/counter_img.php?id=50 | template | icon | 不要 | FC2 トラッキング |
| 12 | .../back_a4.gif | template | icon | 不要 | 背景画像 |
| 13-17 | b-home.jpg / b-jimusyoannai.jpg / b-zeirisitoha.jpg / b-gyally.jpg / b-01.gif | original | text-embedded | 差替 | ナビボタン（テキスト焼込） |
| 18 | .../c_yellow.gif | template | icon | 不要 | カラーバー |
| **19** | .../takayama1.jpg | **original** | **photo** | **そのまま** | **代表（所長）の顔写真 — 唯一のオリジナル純写真** |
| 20 | .../toti2011small.jpg | original | photo | 不要 | 貸土地写真（成約済のため本文から除外） |
| 21 | .../b03_top.gif | original | text-embedded | 差替 | TOP ボタン |
| 22-23 | .../b-goaisatu.jpg / b-kobaikeibaijoho.jpg | original | text-embedded | 差替 | ナビボタン |
| 24-42 | clip_a30.gif, bana-rinkuheya.gif, clip_a7.gif, b_lis002.gif, bana-tohokuzeirisikai.gif, mapionlogo_admi.gif, logo_tell.gif, goo.gif, h1_39.gif, phonebook.gif, header_msn_green.gif, bana-furusatosyokuhin6.jpg, syououken.jpg, rink-takayamajimusyo*.gif, ani-jimusyo*.gif | template | icon/text-embedded | 不要 | リンク用バナー・外部サイトロゴ（自社ページには不要） |
| 43-49 | static.fc2.com/* / media.fc2.com/* | template | icon | 不要 | FC2 システム画像（404ページ由来） |
| 50-52 | b-rink.jpg / b-02.gif / b-03.gif | original | text-embedded | 差替 | ナビボタン |
| 53-58 | guinomiten01〜06.jpg | original | photo | 不要 | ぐい呑み展示会写真（2012年開催済のため本文から除外） |

**結論**: メインで使えるオリジナル純写真は takayama1.jpg（代表写真） **1 枚のみ**。

ヒーロー背景・事務所イメージ・サービス画像は全て Unsplash ストックで補う。
