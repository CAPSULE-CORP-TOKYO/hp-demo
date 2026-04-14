# コンポーネント割当表（L-1959）

## サイト構造
Header → Hero → Pain（こんな方は早めに） → Merit（税理士に依頼するメリット） → Plans（料金プラン2種） → Flow（ご利用の流れ） → Necessary（必要書類） → Staff（税理士・スタッフ紹介） → FAQ → Contact → Footer

## テキストマッピング（主要項目）

| ID | 元テキスト | 新コンポーネント | セクション |
|----|----|----|----|
| T1 | 決算申告サポートセンター郡山 / 運営 郡司総合会計事務所 | ロゴ + サブ | Header / Footer |
| T2 | 決算書作成・法人税申告はおまかせください！ | サブ見出し | Hero |
| T3 | かけこみ決算申告では、損をする!? | メインキャッチ | Hero |
| T4 | 少しでも節税をと考えるなら、決算書の作成は決算日の翌日から２ヶ月以内より前のご相談が望ましく、申告前に、余裕を持ってしっかりとした準備を行えることが節税対策へとつながります。 | リード文 | Hero下 |
| T5 | こんな方は、ぜひ"早め"にご相談ください。 | セクションタイトル | Pain |
| T6 | 決算がわからない / これから起業する / 会社設立1年目 / 節税したい / 急いでお願いしたい | カードラベル | Pain |
| T7 | （各カードのチェック箇条書き） | カード本文 | Pain |
| T8 | 税理士に依頼するメリット | セクションタイトル | Merit |
| T9 | ①〜④ メリット説明 | カード | Merit |
| T10 | 料金プラン / 決算シンプルプラン 9.9 万円〜 / 決算丸投げプラン 16.5 万円〜 | プランカード | Plans |
| T11 | ご利用の流れ（1〜5） | ステップ | Flow |
| T12 | 決算に必要な書類（通帳、領収書...） | リスト | Necessary |
| T13 | 税理士・スタッフ紹介（郡司洋一プロフィール + 8スタッフ） | プロフィール + カード | Staff |
| T14 | よくあるご質問（10問前後） | アコーディオン | FAQ |
| T15 | 〒963-8005 福島県郡山市清水台１－３－８ 郡山商工会議所会館４０１ | 住所 | Contact / Footer |
| T16 | TEL 0120-070-306 / FAX 024-983-8383 / MAIL support@tax-sp.jp | 連絡先 | Contact / Footer |
| T17 | サイトのご利用について / プライバシーポリシー | リンク | Footer |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|---|---|---|---|---|---|
| 1 | header-1.jpg | original | photo | Hero 背景写真 | Hero | そのまま（ローカル化） |
| 2 | photo_gunji.jpg | original | photo | 代表プロフィール写真 | Staff | そのまま（ローカル化） |
| 3 | staff_.png | original | photo | スタッフ集合 | Staff | そのまま（ローカル化） |
| 4 | photo_gunji_n.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 5 | photo_akimoto.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 6 | photo_bannai.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 7 | photo_takahashi.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 8 | photo_shiraiwa.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 9 | photo_konno.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 10 | photo_senzaki.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| 11 | photo_sasagawa.jpg | original | photo | スタッフ個別 | Staff | そのまま（ローカル化） |
| - | logo.png / TOP1〜4 / TEL_header.png / TEL.png / hissu.png | text-embedded | - | - | - | 差替（HTMLテキスト） |
| - | TOP_image.jpg / muryousoudan.jpg / mitsumori.jpg / inkan.jpg / nouzei.jpg / afterfollow.png | stock | photo | - | - | 差替（CSS/SVG または不使用） |
| - | check.png / ppr_*.png / denkyu.png / menu-icon*.png / spmenu_*.png | template | icon | - | - | CSS/SVG 代替 |

## 注意
- スタッフ写真は staff/ ページから取得。Hero とプロフィール写真は事務所固有なのでローカル化必須
- ストック画像（電卓・印鑑等）は引き継がず、CSS/SVG アイコンに置き換える
- 全テキストブロックを原文のまま配置すること
