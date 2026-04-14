# 分析結果

## アーキタイプ

**名前: A: モダンミニマル**（長文コンテンツがあるため E: テキストヘビー 要素も加味）

**根拠:**
- 業種: 公認会計士・税理士事務所（士業・権威系）
- 客層: 中小企業経営者・公益法人・個人事業主
- 文体: 真面目で抑制的。経営理念ページに「お客様の事業継続」「長期的視点」「不況期に強い体質」といった本質志向の長文あり
- 情報量: 業務案内・公益法人支援に詳細なサービス記述あり
- 元サイトは 2013 年頃の TKC NF テンプレ（Bootstrap 2、nivo slider）で、モバイル実質非対応

→ 士業らしい落ち着きと信頼感を前面に、大胆な余白・サンセリフ見出し・高コントラスト・オリジナル写真活用のモダンミニマルで構成する。経営理念の長文は読みやすいカード/記事レイアウトに配置する。

## カラーパレット

元サイト screenshot から目視抽出:
- ヘッダー / ナビ: 白 + グレー、青系ボタン
- 背景グラデ: 明るい水色 (#9ecbea 相当)
- CTA 電話ボタン: 青
- バナー: 紺色

色相を継承しつつ彩度を抑え、士業らしい落ち着いた紺・コバルト系にする:
- **メイン**: `#1e3a66`（紺青。ヘッダー・見出し・フッター）
- **サブ**: `#4a78b8`（コバルト。リンク・ホバー・装飾ライン）
- **アクセント**: `#e8a340`（暖色アンバー。CTA ボタンに集中）
- **ベース**: `#f7f8fa`（ほぼ白）
- **本文テキスト**: `#2b2f36`

60-30-10 = ベース #f7f8fa 60% / メイン #1e3a66 30% / アクセント #e8a340 10%

## 画像分類（実画像を Read で確認済み）

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガーアイコン |
| **2** | /library/.../5768f3de...gif (240x60) | **original** | **photo** | **そのまま** | **坂東事務所ロゴ（筆文字「Bando」+ 漢字） → logo.gif** |
| 3 | /library/.../5768f3e0...jpg (898x360) | stock | photo | 差替 | 書架のスライダー画像・テンプレ向けストック |
| 4 | /library/.../5768f3e2...jpg (898x360) | stock | photo | 差替 | デスク＋植木＋ノート＋眼鏡のストック写真 |
| 5 | /library/.../5768f3e4...jpg (898x360) | stock | photo | 差替 | 都市夕景のストック写真 |
| 6 | /library/.../5768f3e5...gif (370x83) | original | text-embedded | 差替 | 「あまりにも暇なときに押すボタン」焼込 |
| 7 | /library/.../5768f3e7...jpg (480x97) | original | text-embedded | 差替 | 「公益法人制度改革、新会計基準への対応をご支援します」焼込バナー |
| 8-16 | /material/lib03/*, /design/images/bnr-fixed/* | template | text-embedded | 差替 | TKC 共通 PC/SP バナー（インボイス・年収の壁・経営革新等支援機関） |
| 17 | /design/images/bg/bg-pat-A002.png | template | pattern | 不要 | 背景パターン |
| 18 | /library/.../59bb423c...jpg (CSS bg) | template | photo | 不要 | テンプレ CSS 背景 |
| 19 | facebook pixel | — | — | 不要 | トラッキング |
| 20 | /material/lib04/bg-img-A005.jpg | template | photo | 不要 | テンプレ背景 |
| **21** | /library/.../5768f3ea...jpg (320x240) | **original** | **photo** | **そのまま** | **代表・坂東氏の顔写真 → representative.jpg** |
| **22** | /library/.../5768f3eb...jpg (500x375) | **original** | **photo** | **そのまま** | **「税理士 坂東祐治事務所」銘板・関東信越税理士会会員プレート → nameplate.jpg** |
| **23** | /library/.../5768f3ed...jpg (500x375) | **original** | **photo** | **そのまま** | **事務所外観（平屋・白壁・赤瓦屋根の玄関） → exterior1.jpg** |
| **24** | /library/.../5768f3ee...jpg (500x375) | **original** | **photo** | **そのまま** | **事務所外観（「坂東公認会計士事務所」縦看板入り駐車場アングル） → exterior2.jpg** |
| 25 | /material/lib04/bg-illu-B003.jpg | template | diagram | 不要 | テンプレ背景 |
| 26 | /library/.../5768f3f3...gif (470x8) | template | icon | 不要 | 装飾ライン（8px 高） |
| 27 | /material/lib04/bg-img-A001.jpg | template | photo | 不要 | テンプレ背景 |
| 28 | /library/.../5768f3f7...jpg (450x91) | original | text-embedded | 差替 | 「TKC全国会 公益法人経営研究会 Click!」焼込バナー |
| 29 | /library/.../5768f3f8...jpg (199x280) | template | text-embedded | 差替 | TKC 経営革新セミナー 2009 ポスター（TKC 全国共通） |
| 30-39 | /material/lib03/bnr_useful*.png | template | text-embedded | 差替 | TKC 共通「経営者お役立ち情報」バナー群 |
| 40-147 | tkc-management-qa 等のサムネ | template | text-embedded | 不要 | 他ページ配信記事サムネ（全 TKC 共通、デモでは未使用） |

### 引き継ぎ画像サマリ（5 枚）

以下のみ `images/` にローカル化し HTML から相対パスで参照:

1. **logo.gif** ← #2 (5768f3de1084a56918000139.gif)
2. **representative.jpg** ← #21 (5768f3ea1084a56918000140.jpg) — 代表坂東氏
3. **nameplate.jpg** ← #22 (5768f3eb1084a56918000141.jpg) — 事務所銘板
4. **exterior1.jpg** ← #23 (5768f3ed1084a56918000142.jpg) — 外観正面
5. **exterior2.jpg** ← #24 (5768f3ee1084a56918000143.jpg) — 外観看板付き

### Unsplash 差替画像（業務案内カード用、業種: office/tax/business で統一）

- tax-card: `https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1200&q=80` — 電卓・書類
- public-card: `https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80` — ビル・公共感
- kaizen-card: `https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80` — グラフ・分析

（Services セクションのカード 3 枚は Unsplash で統一。オリジナル写真と混在させない。）
