# コンポーネント割当表（L-1966）

## サイト構造

1. **Header**（ロゴ + ナビ + TEL）
2. **Hero**（ヒーロー：見出し・サブ・CTA）
3. **About**（事務所紹介 — いわき中央事務所）
4. **Strengths**（法人としての4つの強み）
5. **Services**（提供サービス）
6. **Flow**（ご相談の流れ 4 ステップ）
7. **Representative**（いわき中央事務所 代表税理士 木幡仁一）
8. **Firm**（さくら中央税理士法人 支店一覧）
9. **Contact**（電話・フォーム・住所）
10. **Footer**
11. **Mobile CTA bar**

## テキストマッピング

全て text-inventory.txt の原文そのまま使用。原文の該当行番号は text-inventory.txt の行番号。

| ID | 元テキスト（原文） | 出典 | 新コンポーネント | セクション | 処理 |
|----|-----|------|------|-----|------|
| T1 | さくら中央税理士法人 | logo alt / 法人名 | ヘッダーロゴ画像 | Header | そのまま |
| T2 | さくら中央税理士法人いわき中央事務所 | leads.json companyName / text-inventory 709 / branch ページ | ヘッダー法人名テキスト（サブ） / About / Contact / Footer | 複数 | そのまま |
| T3 | 報告だけでなく、相談できる税理士法人に。 | top1.jpg 焼込（元サイトのヒーローコピー。実在） | ヒーロー見出し | Hero | そのまま（br/span で分断しない） |
| T4 | 年数回でなく、毎月毎週相談できる税務サービスを。お客様との成長と繁栄を目指し、「一期一会」を大切に、常に新鮮な気持ちでお客様に接することを目指しています。 | top1.jpg 焼込（実在コピー） | ヒーローサブコピー | Hero | そのまま |
| T5 | 【ICTに強い会計事務所】 | text-inventory 12 | Strengths カード1 見出し | Strengths | そのまま |
| T6 | さくら中央税理士法人はITに強い会計事務所です。セカンドオピニオンとしてご相談に来られる経営者も多くいらっしゃいます。税務だけでなく、パソコンや複合機の選定から導入までお気軽にご相談ください。 | text-inventory 13-15 | Strengths カード1 本文 | Strengths | そのまま（句点連結） |
| T7 | 【マイナンバーに強い会計事務所】 | text-inventory 16 | Strengths カード2 見出し | Strengths | そのまま |
| T8 | マイナンバーを安全に収集・保管・管理しています。弊社で従業員様のマイナンバーを登録する場合には、初回のみ従業員様お一人につき500円頂戴しております。それ以外には一切費用はかかりません。マイナンバーの保管に不安をお持ちの方はぜひ弊社にお問合せください。 | text-inventory 17-20 | Strengths カード2 本文 | Strengths | そのまま |
| T9 | 電子帳簿保存法に対応. | top3.jpg 焼込 | Strengths カード3 見出し | Strengths | そのまま |
| T10 | スキャナーを利用して領収書、請求書を送っていただきます。私たちはお客様の総務となり経理となり毎日お客様のことを見ています。 | top3.jpg 焼込 | Strengths カード3 本文 | Strengths | そのまま |
| T11 | コストに見合った税理士サービスを。 | top2.jpg 焼込 | Strengths カード4 見出し | Strengths | そのまま |
| T12 | いくら顧問料を安くしたとしても、社内のコストにお金を使ってしまっていては意味がありません。私たちは質とコスト兼ね備えたサービスをご提供いたします。 | top2.jpg 焼込 | Strengths カード4 本文 | Strengths | そのまま |
| T13 | さくら中央税理士法人のサービス特徴 | text-inventory 22 | Services セクション見出し | Services | そのまま |
| T14 | サービス | text-inventory ナビ | Services セクションラベル | Services | そのまま |
| T15 | 料金 / ご相談の流れ / 税理士紹介 / 会社案内 / 採用情報 / Contact / Blog | text-inventory 4-10 ナビ | ナビゲーション項目 | Header | そのまま（内部アンカー化） |
| T16 | ご相談の流れ | text-inventory 525 | Flow セクション見出し | Flow | そのまま |
| T17 | STEP 1 お問い合わせ／お問い合わせフォーム、または Tel、 Fax にてお問い合わせください。（内容を確認後、弊社より折り返しご連絡いたします。） | ご相談の流れ ページ screenshot 焼込 donyu_01 の相当箇所 | Flow ステップ1 | Flow | そのまま（Step 文言のみ） |
| T18 | STEP 2 個別相談 | screenshot donyu_02 | Flow ステップ2 | Flow | そのまま |
| T19 | STEP 3 お見積り | screenshot donyu_03 | Flow ステップ3 | Flow | そのまま |
| T20 | STEP 4 顧問契約 | screenshot donyu_04 | Flow ステップ4 | Flow | そのまま |
| T21 | ■さくら中央税理士法人いわき中央事務所 代表税理士 木幡 仁一 〒970-8044 福島県いわき市中央台飯野４丁目２−４ 電話：0246-28-9767 | text-inventory 1803-1808（branch ページ） | About / Representative / Contact | 複数 | そのまま |
| T22 | さくら中央税理士法人 支店一覧 | text-inventory 708 / 1802 | Firm セクション見出し | Firm | そのまま |
| T23 | ■さくら中央税理士法人中野中央事務所 税理士 草地 久由美 〒164-0011 東京都中野区中央４丁目６０−５ 自然村ビル ３階 電話：03-3384-1989 | text-inventory 1809-1812 | Firm カード | Firm | そのまま |
| T24 | ■さくら中央税理士法人佐藤真事務所 税理士 佐藤 真 〒277-0813 千葉県柏市 大室３丁目６番地１８ 電話：04-7189-8521 | text-inventory 1813-1816 | Firm カード | Firm | そのまま |
| T25 | ■さくら中央税理士法人練馬中央事務所 税理士 丸山 恭子 税理士 宇田 一大 〒176-0012 東京都練馬区豊玉北5-16-12サンライズ豊玉3D 電話：03-5999-7017 | text-inventory 1817-1822 | Firm カード | Firm | そのまま |
| T26 | 法人名：さくら中央税理士法人 / 所在地：〒103-0013 東京都中央区日本橋人形町2-15-15 新扇堂ビル3階 / 開業日：平成25年12月（前：安田会計事務所）/ 代表：安田 信彦 / 従業員：11名（令和5年4月現在） / 電話：03-3667-1016 / FAX：03-3666-7019 | text-inventory 700-707 | Firm 概要ブロック | Firm | そのまま |
| T27 | お問い合わせ | contact2 ページ | Contact セクション見出し | Contact | そのまま |
| T28 | TEL 0246-28-9767 | branch ページ | Contact TEL / Header TEL / Mobile CTA | 複数 | そのまま |
| T29 | コピーライト © さくら中央税理士法人 | 慣習 | Footer | Footer | そのまま（原文にある表記が乏しいので minimal ©️ 表記のみ） |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | http://ysd21.com/wp-content/uploads/2015/03/SClogo1_300.png | original | photo（ロゴ） | ヘッダー / フッター ロゴ | Header / Footer | **そのまま（images/SClogo1_300.png）** |
| 2 | https://ysd21.com/wp-content/uploads/2016/07/b1364fce1bb7e7a4134ebd65718e269f-e1514345943332.jpg | original | photo | 代表税理士セクション（木幡仁一） | Representative | **そのまま（images/kohata-jinichi.jpg）** |
| 3 | .../2014/09/top1.jpg / top2.jpg / 2016/03/top3.jpg | original | text-embedded | — | Hero | **Unsplash 差替**（落ち着いたオフィス・書類系） |
| 4 | .../2014/09/m.yasuda.jpg | original | photo | — | — | **不使用**（本店代表。iwaki demo には不適） |
| 5 | .../2014/09/i.mori_.jpg / s.takagi.jpg | original | photo | — | — | **不使用**（本店税理士） |
| 6 | .../sakuracyuo_1〜6.jpg | original | photo | — | — | **不使用**（本店の雑多なグリッドバナー） |
| 7 | .../contents_1/2/3.jpg | template | diagram | — | — | **差替**（CSS アイコン or Unsplash） |
| 8 | .../price_*, .../scan_*, .../mynum_*, .../souzoku_*, .../donyu_* | original | text-embedded | — | — | **不使用**（テキスト化した内容を HTML で再構築） |
| 9 | ブログ各種画像（2025-2026 のニュース画像） | original | photo | — | — | **不使用**（iwaki branch demo の主要訴求に不要） |
| 10 | RPA/RDA カテゴリ画像 | template | text-embedded | — | — | **不使用** |
| 11 | Hero 背景 | — | — | Hero 背景 | Hero | **Unsplash URL**（例: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40 — 書類・デスク系） |
| 12 | About セクション装飾 | — | — | About 背景 | About | **CSS グラデーション**（画像不要） |

## 統一性チェック

- スタッフ写真: 木幡仁一のみ引き継ぎ。並列 3 枚など並べる構成にはせず「いわき中央事務所 代表税理士」の 1 枚専用セクションとして配置 → 混在禁止ルールに抵触しない
- サービスカード: Unsplash 画像を使わず、CSS アイコン（SVG または emoji-free の CSS）で統一 → 画像ソースの混在回避
- Hero のみ Unsplash 背景画像を使用

## Hero 画像の確定 URL（Unsplash）

- `https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1920&q=80&fit=crop` — 書類・ペン・電卓（税理士業務の雰囲気）

（Unsplash public URLs は直接参照可。ローカル化不要。HTTPS。）
