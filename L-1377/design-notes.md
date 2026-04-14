# 分析結果 — L-1377 岡﨑耕作税理士事務所

## アーキタイプ
名前: **A: モダンミニマル**

根拠:
- 業種が税理士（士業）であり、信頼・明瞭・権威を訴求する対象。
- 顧客層は法人経営者・個人事業主・相続相談者で、情報の見通しとプロフェッショナルさが重要。
- 元サイトはペライチ "accountingfirm" テンプレをベースにした 2010 年代後半の印象で、情報は整理されているが古さ・雑多さが残る。サンセリフ基調の高コントラスト・余白を活かしたモダンミニマルへ寄せる。
- 所長は国税専門官採用試験 / 関東信越国税局出身というキャリアを持ち、権威性の一部がある。主張は落ち着いたミニマルでまとめるのが最適。

## カラーパレット
元サイトは白背景＋ネイビー〜深いブルーの基調に、ヘッダーがダークネイビー〜ティール系のグラデーション、見出し帯が濃いネイビー、タブなど一部にティール/エメラルド。色相を継承し、明度・彩度を現代風に調整する。

- メイン: `#0B2E5B` (深いネイビー — ヘッダー・見出し)
- サブ: `#F5F7FB` (明るいブルーグレー — セクション背景の切り替え)
- テキスト: `#1F2937` (ダークグレー — 本文)
- ミューテッド: `#6B7280`
- アクセント: `#0EA5A4` (ティール — CTA ボタン、強調、区切り線)
- ボーダー: `#E5E7EB`

60-30-10 の法則:
- Base 60%: 白 `#FFFFFF` と `#F5F7FB`
- Primary 30%: `#0B2E5B`
- Accent 10%: `#0EA5A4` (CTA のみに集中)

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../ogp/151725.png | — | — | 不要 | OGP 専用（og:image）、DOM 参照なし |
| 2 | .../pixta/1491670539/0_original.jpg (css-bg) | stock | photo | **差替 (Unsplash)** | PIXTA ストック（背景） |
| 3 | .../img/1491380733/original.jpg | original ? | text-embedded | **差替 (Unsplash)** | peraichi userData 配下だがトップの大判画像で古い印象、保守的に差替 |
| 4 | .../img/1492303196/original.jpg | original ? | text-embedded | **差替 (Unsplash)** | 同上 |
| 5 | .../img/1491699069/original.jpg | original ? | text-embedded | **差替 (Unsplash)** | 同上 |
| 6 | .../accountingfirm/img/bar_bg.jpg | template | photo | **差替 (CSS グラデ)** | ペライチテンプレ共通背景 |
| 7 | .../accountingfirm/img/hojin_1.jpg | template | photo | **差替 (Unsplash)** | テンプレ付属（会議室） |
| 8 | .../accountingfirm/img/hojin_2.jpg | template | photo | **差替 (Unsplash)** | テンプレ付属 |
| 9 | .../accountingfirm/img/hojin_3.jpg | template | photo | **差替 (Unsplash)** | テンプレ付属 |
| 10 | .../img/655ea420c5629/original.png | original | text-embedded (brand badge) | **そのまま引き継ぎ (images/ にローカル化)** | freee 5つ星認定アドバイザーバッジ。事務所の保有資格を示す固有価値。小サイズで掲載。 |
| 11 | .../img/5c5f9c21c0404/original.png | original | text-embedded | **差替 (Unsplash)** | 相続相談バナー。テキスト焼込＋旧所在地マップ（移転前）、そのまま使うと情報が誤る。 |
| 12 | .../pixta/1491670539/0_original.jpg (重複) | stock | photo | **差替** | 2 と同一 |
| 13 | .../pakutaso/pakutaso_070/original.jpg | stock | photo | **差替 (Unsplash)** | ぱくたそストック |
| 14-17 | .../salon_nail/img/icon_*.png | template | icon | **CSS/SVG 代替** | SNS アイコン小さい素材 |
| 18-20 | `&quot;...&quot;` を含む URL | — | — | 不要 | HTML エスケープ残骸の誤検知 |
| 21-29 | googleads / facebook.com/tr / bing | — | tracking | 不要 | トラッキングピクセル |

## 画像引き継ぎ一覧 (Phase 5-0 でローカル化する対象)

| ローカルパス | 元 URL | 用途 |
|---|---|---|
| `images/freee-5star.png` | http://cdn.peraichi.com/userData/58e35bea-7a6c-4664-a641-1f650a0000c2/img/655ea420c5629/original.png | freee 5つ星認定バッジ（事務所の特徴セクション） |

それ以外は Unsplash 差替 or CSS 代替。

## フォント方針
- 士業で信頼・権威・モダン感を出すため、本文は **Noto Sans JP**、見出しは **Noto Serif JP** を一部で併用しない（A: モダンミニマルは基本サンセリフ）。
- 見出しはウェイト 700、本文 400、行間広めに取る。
