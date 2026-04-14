# 分析結果

## アーキタイプ
名前: A（モダンミニマル）＋ 一部 B（伝統重厚）要素
根拠:
- 税理士事務所（昭和45年設立、東北税理士会所属）であり信頼・権威が要件
- ただし diagnosis に「モバイル非対応/2012年頃のTKCテンプレート/画像ボタン多用/CTA不明瞭」とあるため、モダンで余白の効いたミニマル構成にリデザインする
- 見出しに Noto Serif JP（和の重厚感）、本文に Noto Sans JP（可読性）の二枚使い

## カラーパレット
元サイト screenshot.png より:
- メイン: #1e5aa8（ネイビーブルー、TKC系の青をやや深めた信頼色）
- サブ: #f5f7fa（薄グレーブルー、背景）
- アクセント: #e88a2a（オレンジ、CTA / 見出しアクセント）
- テキスト: #1a2433（濃紺） / #4a5568（薄テキスト）

## 画像分類

141枚の画像を確認したが、**寺山会計センター固有の original 画像は存在しない**。
全て TKC 共通テンプレート素材か、ストック写真、外部記事サムネイルである。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガーアイコン |
| 2 | library/.../571f2f93...gif | template | text-embedded | 差替 | タイトル焼き込み画像 |
| 3 | library/.../571f2f96...jpg (940x372 空・草原・菜の花) | stock | photo | 差替 | 汎用ストック風景 |
| 4 | library/.../571f2f94...gif (140x80) | template | text-embedded | 差替 | 「当事務所が研究 実績機関です」焼き込み小バナー |
| 5 | material/lib02/tkc_logo1.gif | template | text-embedded | CSS/SVG 代替 | TKC全国会ロゴ小バナー |
| 6 | library/.../571f2f98...jpg "経営革新等支援機関" | template | text-embedded | CSS/SVG 代替 | 認定マーク焼き込み |
| 7-11 | material/lib02/KFS_0{1-5}.png | template | text-embedded | 差替 | KFSとは? バナー連続 |
| 12-17 | design/images/bnr-fixed/bnr-* | template | text-embedded | 差替 | 電帳法・年収の壁 固定バナー |
| 18 | facebook.net/.../onuUJj0tCqE.png | template | icon | 不要 | Facebook埋め込みトラッキング |
| 19-24 | library/.../571f2f{99,9a,9c,9d,9f,a2}.* | stock | photo | 差替 | サブページの汎用アイキャッチ（純粋なストック） |
| 25-27 | library/.../689ecf16* (日本政策金融公庫バナー3枚) | template | text-embedded | 差替 | TKC融資紹介共通バナー |
| 28-37 | material/lib03/bnr_useful*.png | template | text-embedded | 差替 | TKC共通の業務メニューバナー |
| 38-70 | library/.../tkc-management-qa/* 記事サムネ多数 | template | photo | 差替 | Q&A 記事サムネ（寺山会計固有でない）|
| 71-141 | その他 TKC 共通素材・spacer.gif・btn_pagetop.gif 等 | template | icon/diagram | CSS/SVG 代替 or 不要 | 全てテンプレ素材 |

**結論**: 引き継ぎ対象の original 画像はゼロ。images/ ディレクトリへのダウンロード対象ファイルなし。
代替方針:
- ヒーローの背景: Unsplash の「office / business / accounting」系高品質写真
- About セクションの印象画像: Unsplash の「いわき/海岸/福島」風景 or 事務所イメージ
- サービスカードのアイコン: SVG / Unicode
- 「ＴＫＣ全国会会員」「経営革新等支援機関」は CSS の装飾ピルで再現（テキストのみ）

## 業種・トーン
- 業種: 税理士（company registration 1945系、所長寺山隆三）
- 客層: 地元いわき市の中小企業、法人・個人事業主、創業者
- 文体: 格式のある丁寧文（「当事務所は〜」「〜いたします」）
- 強み: TKC全国会会員、東北税理士会所属、昭和45年創業（開業は昭和42年）、自利利他の経営理念、PC会計・自計化支援、経営革新等支援機関
