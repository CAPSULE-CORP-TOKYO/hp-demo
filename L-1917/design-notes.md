# 分析結果 — L-1917 大橋税理士事務所

## 主体一致確認（DEC-026 関連）
- leads.json companyName: 大橋税理士事務所
- 元サイト `<title>`: 郡山｜大橋税理士事務所　相続,会計,税務,経営
- 元サイト プロフィール表: 大橋税理士事務所 / 所長 大橋 健二 / 福島県郡山市虎丸町5-8 / 024-935-7633 / ohhashi-kenji@tkcnf.or.jp
- leads.json 住所: 〒963-8014 福島県郡山市虎丸町5-8 日宝郡山第一ビル4f
- ⚠️ ビル名揺れ: index/事務所概要では「さくらＮＴビル4F」、map（交通案内）ページでは「日宝郡山第一ビル4F」。同じビルの新旧名称（または通称/正式名称）と思われる。leads.json の住所は map ページと一致しているため、leads.json 値をそのまま採用する
- ⇒ 判定: **同一事務所**。DEC-026 のような別会社サイトではない。Phase 3 以降を続行する

## アーキタイプ
名前: **A: モダンミニマル**（士業向け、信頼感を保ちつつ刷新）
根拠:
- 業種は税理士事務所（権威・信頼）。ただし元サイトのトーンは「明るく元気」がモットーで親しみやすさも含む
- 顧客層は中小企業経営者・個人事業主・相続案件。情報量はそれなりに多いが、現代的に整理して導線を明快にする必要
- 元サイトのグリーン基調を継承しつつ、PC幅固定/バナー乱立/情報過多の旧来型を捨てて余白主体のミニマル構造に再設計
- 見出しに Noto Serif JP（士業の落ち着き）を一部使い、本文は Noto Sans JP

## カラーパレット
元サイトのグリーン（TKC テンプレ）を継承。色相は変えない。

- メイン: `#3F6B2A`（深みのあるフォレストグリーン。元サイトの帯色 #76923c をやや落ち着いた方向に調整）
- サブ: `#76923C`（元サイトの帯色そのまま。アクセント帯・ホバー）
- アクセント: `#C99700`（伝統的な金茶。CTA・強調）
- 背景: `#FFFFFF` / `#F7F8F4`（白＋ごく淡いグリーンウォーム）
- テキスト: `#1F2A1A`（ほぼ黒、わずかにグリーン寄り）

## 画像分類

| # | URL（短縮） | 内容 | 出自 | 適性 | 処理 |
|---|---|---|---|---|---|
| 1 | library/.../58af99f4...png | テキストロゴ「大橋税理士事務所」 | original | photo(logo) | **そのまま**（ロゴ） |
| 2 | library/.../58b384b8...png | TEL 電話番号画像 | original | text-embedded | CSS/HTML 代替 |
| 3 | library/.../58afa246_55fe...png | ヒーロー「相続についてお困り…」会議室背景 | original | text-embedded | 差替（Unsplash） |
| 4 | library/.../58afa245_0155...png | ヒーロー「相続…」グラフ会議背景 | original | text-embedded | 差替（Unsplash） |
| 5 | library/.../58afa246_e2a0...png | ヒーロー「相続…」握手背景 | original | text-embedded | 差替（Unsplash） |
| 6 | library/.../58dcd69e...jpg | **スタッフ集合写真（4名）** | original | photo | **そのまま** |
| 7 | library/.../5b975b92...jpg | TKCモニタリング棒グラフ | template | diagram | 不要（差替なし） |
| 8 | material/lib03/bnr_*（多数） | TKC共通バナー（マイナンバー、年収の壁、電帳法、各種システム紹介、関連サイト誘導） | template | text-embedded | 不要 |
| 9 | library/.../58dcd776...jpg | 所長 電話対応中 | original | photo | **そのまま**（所長挨拶セクション） |
| 10 | library/.../58dcd92a...jpg | 事務所内 オフィス風景 | original | photo | **そのまま** |
| 11 | library/.../58dcd932...jpg | 応接室 本棚 | original | photo | **そのまま** |
| 12 | library/.../58dcd940...jpg | 男性スタッフ 笑顔 | original | photo | **そのまま** |
| 13 | library/.../58dcd92e...jpg | 「魂」木彫オブジェ | original | photo | そのまま（装飾） |
| 14 | library/.../58dcd939...jpg | 銅鉱物オブジェ | original | photo | 不要（雰囲気写真、優先度低） |
| 15 | library/.../58dcd943...jpg | 男性スタッフ 作業中 | original | photo | **そのまま** |
| 16 | library/.../58dcd93c...jpg | 蘭の花 | original | photo | 不要（装飾、優先度低） |
| 17 | library/.../58dcd946...jpg | 女性スタッフ 電話対応 | original | photo | **そのまま** |
| 18 | library/.../58dcda5c...jpg | **事務所外観（ビル）** | original | photo | **そのまま**（アクセスセクション） |
| 19 | library/.../58afb210...png | 「相続お悩み相談サイト」バナー | original | text-embedded | 不要 |
| 20 | material/lib02/tkc_logo1.gif | TKC 全国会ロゴ | template | logo | そのまま（フッターの所属表示用、SVG/img どちらでも可） |
| その他 | design/images/、material/lib03/ | TKC 共通テンプレの装飾・バナー類 | template | various | 不要 |

**引き継ぎ画像（local images/ 配下にダウンロード）**:
1. ロゴ: 58af99f40155a55e28ffd7b3.png → `images/logo.png`
2. スタッフ集合: 58dcd69e0953317255053582.jpg → `images/staff-team.jpg`
3. 所長電話: 58dcd776095331725505359d.jpg → `images/director-phone.jpg`
4. オフィス風景: 58dcd92afc6a04c74eb0ade5.jpg → `images/office-room.jpg`
5. 応接室: 58dcd93209533172550535e9.jpg → `images/office-lounge.jpg`
6. スタッフ男性笑顔: 58dcd94009533172550535ec.jpg → `images/staff-male1.jpg`
7. 魂オブジェ: 58dcd92eb0b521c94ed879d4.jpg → `images/desk-symbol.jpg`
8. スタッフ男性作業: 58dcd943fc6a04c74eb0ade7.jpg → `images/staff-male2.jpg`
9. スタッフ女性電話: 58dcd94609533172550535ee.jpg → `images/staff-female.jpg`
10. 事務所外観: 58dcda5cb0b521c94ed879f0.jpg → `images/office-exterior.jpg`

## デザイン方針メモ
- ヒーローはテキスト焼込画像を捨て、HTML テキスト + Unsplash の士業/オフィス系の落ち着いた写真背景。原文の「大橋税理士事務所のホームページにようこそ！」と「明るく元気」のキャッチを HTML 文字で表示
- 業務案内は元サイトの 5 つの柱（巡回監査 / 業績管理体制 / 自計化指導 / 書面添付 / 記帳適時性証明書）をカード化
- 所長挨拶は所長電話写真をビジュアルに、原文をそのまま
- 経歴は時系列リスト（原文そのまま、創作禁止）
- スタッフ写真ギャラリー（4枚 + 集合写真1枚）で職場の空気感を訴求
- 事務所概要表 → 元サイトの dl 型を踏襲しつつモダンに
- 交通案内 → 事務所外観写真 + テキスト案内（所在地は leads.json と一致する map ページ表記の「日宝郡山第一ビル4F」を採用）
- TKC全国会会員 / 東北税理士会所属の表記はフッターに残す
