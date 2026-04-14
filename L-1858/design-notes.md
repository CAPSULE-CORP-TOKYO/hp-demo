# 分析結果 — L-1858 田代行孝税理士事務所

## アーキタイプ
名前: **A: モダンミニマル**（士業・コンサル）
根拠:
- 税理士事務所（白河市、TKC 全国会会員）で、信頼性と清潔感が重要
- 元サイトは TKC 標準テンプレで情報量が多いが、中身は会計/税務の堅実な内容
- 伝統寺院系ではなく、白を基調に Noto Sans JP + 見出しに Noto Serif JP を使う現代的ミニマル構成が最適
- B（伝統重厚・明朝体）は過剰、C/D（写真主体）は固有写真ゼロのため不適

## カラーパレット
元サイトのメインはオレンジ（TKC 標準カラー）。以下で継承:
- **メイン（ベース）**: `#FFFFFF`（白）
- **サブ（テキスト）**: `#1F2937`（ほぼ黒、Noto Sans JP の可読性重視）
- **プライマリ**: `#D94E1F`（元のオレンジを彩度やや落として現代的に）
- **プライマリ-dark（ホバー）**: `#B33E15`
- **アクセント（細部）**: `#F5B16C`（淡いオレンジ、区切り線/背景強調）
- **背景（セクション）**: `#F7F5F2`（温かみのあるオフホワイト）
- **ボーダー**: `#E5E1DB`

60-30-10:
- 60% 白/オフホワイト（base）
- 30% 黒系テキスト + 軽いニュートラル
- 10% オレンジ（CTA・見出しアクセント・アイコン）

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../57566ded...gif (logo.gif) | original | text-embedded | CSS/SVG 代替 | 「田代行孝税理士事務所」の黒テキスト画像。HTML テキストで再現 |
| 2 | .../57566df5...jpg | stock | photo | 差替 | 本棚のストック写真 |
| 3 | .../57566df7...jpg | stock | photo | 差替 | キーボード＋文房具のストック |
| 4 | .../57566df9...jpg | stock | photo | 差替 | 都会のビル群夕景ストック |
| 5 | .../57566def...gif | template | text-embedded | 差替 | TKC 全国会オンデマンド講座バナー |
| 6 | material/lib02/KFS_01〜05.png | template | text-embedded | 差替 | TKC KPS 紹介バナー |
| 7 | bnr-invoice-pc1.png / bnr-nensyunokabe-pc.png | template | text-embedded | 差替 | 電帳法・年収の壁バナー（TKC 標準） |
| 8 | design/images/bg/bg-pat-A002.png | template | - | 差替 | 背景パターン（CSS グラデで代替） |
| 9 | library/.../57566dfe...jpg (office) | stock | photo | 差替 | 古いキーボード＋電卓ストック |
| 10 | library/.../57566e00...jpg (philosophy1) | stock | photo | 差替 | 雑誌ストック |
| 11-141 | その他全て | template/stock | mixed | 差替/不要 | TKC コンテンツ系バナーは全てサブコンテンツ扱いで本文ページには載せない |

**結論**: 固有の写真はゼロ。ロゴもテキストのみで再現可能。**Phase 5-0 でダウンロードする画像は無し。** Hero 以降の装飾写真は Unsplash（office / business / accounting 系）で統一。
