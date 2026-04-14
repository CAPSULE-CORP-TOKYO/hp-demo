# 分析結果: L-1387 株式会社ステップ（税理士法人ステップ）

## アーキタイプ
名前: **A: モダンミニマル**（ややリッチビジュアル寄り）
根拠:
- 業種: 税理士法人（医業専門コンサル）。権威性と信頼感、かつ専門性の訴求が必要
- 顧客層: クリニック開業医・医療法人経営者。高所得・意思決定者。清潔感と品質の両立を重視
- 文体: 「大丈夫ですよ」「共に考え、共に成長する」など伴走型・人間味のあるトーン
- 情報量: サービス6カテゴリ、スタッフ4名+その他、沿革、料金、採用まで掲載されており、情報量は多め
- オリジナル写真が豊富（代表/副所長/スタッフ/外観/内観/受付）→ ビジュアル主体のレイアウトが可能
- 方針: 余白をしっかり取ったミニマル構成＋大判ヒーロー写真＋ファクトカードで、信頼感・清潔感・伴走型の柔らかさを両立
- フォント: Noto Sans JP をメイン、見出しにやや Noto Serif JP 混在も可（硬すぎない権威性）

## カラーパレット

元サイトから抽出:
- メインカラー（ブランドカラー）: **#A6175E**（ステップのロゴ中央「斜線 p」のマゼンタ系ピンク）
- ダークニュートラル: **#3A4651**（ロゴ「st」のチャコールグレー）
- ベース: **#FFFFFF**（白）/ **#F8F5F7**（ほんのりピンクがかったオフホワイト）
- サブアクセント: **#7A0E43**（濃いマゼンタ、ホバー/強調用）

60-30-10:
- ベース 60%: #FFFFFF / #F8F5F7
- プライマリ 30%: #3A4651（テキスト・ヘッダー）
- アクセント 10%: #A6175E（CTA、見出し装飾、ライン）

## 画像分類

（代表的なもの。全101枚のうち引き継ぎ候補になる original×photo のみ Pick。残りはテンプレート/テキスト焼込等で差替対象）

| # | URL（末尾） | 出自 | 適性 | 処理 | 備考 |
|---|-------------|------|------|------|------|
| logo | 6842a91e...STEP.jpg | original | photo(ロゴ) | **そのまま** | 社名ロゴ。スタンドアローンで完成 |
| hero | 68467e7f...medical-consulting.jpg | original | text-embedded | 差替 | 「Medical Practice Consulting」キャッチ焼込。差替 |
| kusano | 619701ac...kusano.png | original | photo | **そのまま** | 副所長 草野滋 人物写真 |
| miyashita | 636b347f...miyashita.jpg | original | photo | **そのまま** | 宮下昌之 人物写真 |
| yashiro | 623a652a...yashiro.png | original | photo | **そのまま** | 矢代あきこ 人物写真 |
| momma | 619701ac...momma.png | original | photo | **そのまま** | 門馬昭子 人物写真 |
| gaikan_top | 61947a4c...gaikan.png | original | photo | **そのまま** | トップ帯用外観合成（ロゴプレート+建物） |
| office_ext | 61947e03...exterior.png | original | photo | **そのまま** | 事務所外観（ピンクライン入り三階建て） |
| office_in1 | 61948eae...meeting-room.png | original | photo | **そのまま** | 会議室（内観） |
| office_in2 | 61948ead...desk.png | original | photo | **そのまま** | 個別デスク（内観） |
| office_in3-6 | 61948eae〜 | original | photo | そのまま（任意） | 内観追加 |
| reception | 6194919f...reception.png | original | photo | **そのまま** | 受付（料金ページのもの） |
| gyomu1 | 62318c6c...work_scene.png | original | photo | そのまま（任意） | 業務風景 |
| greeting_img | 699ea2da...greeting.png | original | text-embedded | 差替 | 「代表挨拶」見出し焼込 |
| service_titles | 617762bd〜 | template/original | text-embedded | 差替 | サービス6カード（テキスト焼込）→ HTML カード化 |
| section_title_* | 611ca62f/617773...etc | template | text-embedded | 差替 | 各セクション日本語タイトル焼込（H2 に置換） |
| greeting_logo | 6842ad04...greeting_logo.png | template | text-embedded | 差替 | 「Greeting Message」ロゴ |
| btn_contact | 68462e4e...tel.png | template | text-embedded | 差替 | 電話番号焼込 → tel: + HTML |
| btn_mail | 61947b56...mail.png | template | text-embedded | 差替 | 問合せ焼込 → HTML CTA |
| bnr_invoice | bnr-invoice-*.png | template | text-embedded | 不要 | TKC 共通バナー |
| bnr_nensyu | bnr-nensyunokabe-*.png | template | text-embedded | 不要 | TKC 共通バナー |
| merit_illust1-3 | 619715ad... | template | text-embedded/illust | 差替 | メリット用汎用イラスト（SVG アイコンで代替） |
| step_arrows | 61971024〜 | template | text-embedded | 差替 | STEP番号入り画像 → HTML 番号付きボックスに |
| 材料系 lib01/lib03 | .../material/lib01/*.jpg | stock/template | photo | 不要 | TKC 汎用素材 |
| 年収の壁/電帳法 | .../5656ef25.../*.png | template | text-embedded | 不要 | TKC 全国共通コンテンツ（リンク先） |

### 画像差替方針
- ヒーローには外観写真（office_ext）を大判で使用
- サービスセクションは SVG/Unicode アイコン + HTML テキストでカード化（元画像はテキスト焼込のため）
- スタッフセクションは 4 名の original×photo をそのまま配置
- アクセス/会社概要セクションに office_ext + 内観 2 枚を組み合わせ
- 元ロゴを header に配置（social proof として強い）

## 全体方針

- 医業専門コンサルという強みを明確に打ち出す
- 代表挨拶・メリット・サービス6カテゴリ・料金・スタッフ・アクセス・会社概要（沿革含む）を主要セクションとしてそのまま掲載
- 伴走型の文体（原文そのまま）を活かすため、挨拶文と meritセクションの本文は原文流用
- 余白を広く、上品に。Material 風のカードシャドウは控えめ
- CTA は「電話 0246-29-5600」と「問合せフォーム（https://cms.tkcnf.com/step/form/inquiries）」を併設
