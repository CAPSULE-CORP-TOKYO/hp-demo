# 分析結果

## アーキタイプ
名前: A（モダンミニマル） + 一部 B（伝統重厚）の要素
根拠:
- 税理士事務所（士業・コンサル）。権威・信頼・専門性の訴求が主
- 原文は長文が多く情報量が豊富（経営理念・業務内容等）→ 読みやすさ重視
- 元サイトは TKC 標準テンプレで青系・角ばった無個性。現代的なミニマルに振る
- ロゴ代わりに「経営革新等支援機関 認定取得」を強調できるため、士業らしい落ち着いた青＋アクセントに深いネイビーで威厳を出す
- 見出しに Noto Serif JP、本文 Noto Sans JP のハイブリッドで信頼感と可読性を両立

## カラーパレット
元サイトのスクショから抽出:
- 元サイト基調: 明るい青（TKCテンプレ標準）。スカイブルー〜シアン系
- ヒーローには緑の葉っぱ写真→サブカラーの中間にアクセントとして触れる程度でOK

採用パレット:
- メイン（ネイビーブルー）: `#1E3A8A`（元サイトの青を深めて権威を出す）
- サブ（ライトブルー）: `#60A5FA`（元サイトのTKC青の明度版）
- アクセント（ディープゴールド）: `#C89B3C`（信頼・実績の強調。CTA・バッジに集中）
- ベース背景: `#F8FAFC`（off white）
- テキスト: `#0F172A` / サブテキスト `#475569`

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 2 | .../62da574cb5f1b9ec051e6925.png | original | text-embedded | 差替（HTMLテキスト化） | 「経営革新等支援機関 認定取得／三上貴也税理士事務所」の文字ロゴ |
| 3-5 | .../common/sample/slide/slideshow01,03,04.jpg | template | photo | Unsplash 差替 | TKC共通スライド素材 |
| 6-9 | .../bnr_increase-customer*.png | template | text-embedded | 差替 | TKCバナー素材 |
| 10-12 | .../TKCdesignDB_201704_*.png | template | photo | Unsplash 差替 | TKC素材DB |
| 13-17 | .../KFS_0*.png | template | photo | 差替 | TKC素材 |
| 18 | .../tkc_logo1.gif | template | photo | そのまま（相対化） | TKC全国会ロゴ（公式表記のため引き継ぎ） |
| 19-20, 23-24 | .../bnr-fixed/*.png | template | text-embedded | 差替 | TKC固定バナー |
| 21-22 | icon-close.png, icon-open.png | template | icon | CSS/SVG 代替 | |
| 25 | facebook tracking pixel | template | icon | 除外 | |
| 26 | page2 .../6239170bcd1b4f0a0673354d.png | original | photo (illustration) | そのまま引き継ぎ | **所長イラスト似顔絵（重要）** |
| 27 | page2 .../6625bb9f3d19938a4a654b88.png | template | icon | CSS/SVG 代替 | Instagram ロゴ |
| 28 | page2 .../6625bd43dda5ce2f06be601d.png | template | - | 除外 | 169バイト空ファイル |
| 29 | page2 .../62464f5571a0ee3606e05942.jpg | original | photo | そのまま引き継ぎ | **事務所外観（重要）** |
| 30 | page2 .../62425c4ac0e523f6053073e0.jpg | original | photo | そのまま引き継ぎ | **会議室（重要）** |
| 31-40 | page3/page4/page5 tempcommon, 1739424等 | template/stock | photo | 差替 | TKCテンプレ |
| 41-133 | その他全て | template | 各種 | 使わない（Unsplash/CSS代替） | サブページバナー等 |

**引き継ぎ確定画像（Phase 5-0 でローカル化）**:
1. `62da574cb5f1b9ec051e6925.png` (ロゴ文字画像) → 実は text-embedded なのでヘッダーにはテキスト表示を優先。ただしダウンロードはしておき、アクセント用フォールバックとして保管。→ **差替扱い**（ダウンロードしない）
2. `6239170bcd1b4f0a0673354d.png` → `chairman-illust.png` 所長イラスト
3. `62464f5571a0ee3606e05942.jpg` → `office-exterior.jpg` 事務所外観
4. `62425c4ac0e523f6053073e0.jpg` → `meeting-room.jpg` 会議室
5. `tkc_logo1.gif` → `tkc-logo.gif` TKC全国会ロゴ（フッター表記用）
