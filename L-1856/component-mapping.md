# コンポーネント割当表 — L-1856 大手門会計

## サイト構造（single page）
Header → Hero → Notice（リニューアル告知）→ About（事務所について）→ Policy（事務所方針・社是）→ Services（業務内容）→ Advisors（税理士紹介）→ Resources（税務ニュース・旬の特集・書式集）→ Access → Contact → Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 税理士法人　大手門会計 | ヘッダーロゴ（テキスト） | Header | そのまま |
| T2 | 福島県白河市 | サブライン | Header | そのまま |
| T3 | PAX INTRANTIBVS SALVS EXEVNTIBVS / （ﾊﾟｸｽ ｲﾝﾄﾗﾝﾃｨﾌﾞｽ ｻﾙﾌﾞｽ ｴｸｾｳﾝﾃｨﾌﾞｽ） | Hero サブ見出し（原文まま） | Hero | そのまま（分断禁止） |
| T4 | これは、ドイツのローテンブルグ市の門に刻まれている言葉で、東山魁夷画伯は「歩み入るものにやすらぎを、去り行く人にしあわせを」と日本語に訳されています。 | Hero リード文 | Hero | そのまま |
| T5 | 【ホームページリニューアルのお知らせ】令和８年４月よりホームページをリニューアルしております。このホームページは４月末をもって配信を停止いたしますが、新ホームページ（https://ohtemon.tkcnf.com）より情報を発信しておりますので、今後とも変わらぬご愛顧のほど、何卒よろしくお願い申し上げます。 | お知らせ告知ブロック | Notice | そのまま |
| T6 | 事務所方針 ◆事務所について 全文（佐藤雄一郎創設〜プラス・ワン〜） | About 本文 | About | そのまま（段落保持） |
| T7 | 事務所方針：誠実で親切な仕事 / 専門家としての権威ある仕事 / 誇りと喜びのある仕事 + 下文 | Policy 社是カード 3 枚 + リード | Policy | そのまま |
| T8 | 月次の試算表は…／経営戦略…／新知識や情報…（具体 1〜3） | Policy 具体例 3 項目 | Policy | そのまま |
| T9 | 業務内容 + 税理士独占業務の説明 + 1.巡回監査〜8.業務に対するコンサル | Services カード/リスト | Services | そのまま（8 項目） |
| T10 | 司法書士、不動産鑑定士とのネットワーク〜 | Services フッター補足 | Services | そのまま |
| T11 | 税理士・中小企業診断士 佐藤 俊彦 （画像内コメント） | Advisors カード 1 | Advisors | 画像そのまま + 氏名キャプション |
| T12 | 弁護士・税理士 浦木 厚利 （画像内） | Advisors カード 2 | Advisors | 画像 2 枚並べる + キャプション |
| T13 | 税理士 遠藤 徳 （画像内） | Advisors カード 3 | Advisors | 画像そのまま + キャプション |
| T14 | 税理士 須田 茂 （画像内） | Advisors カード 4 | Advisors | 画像そのまま + キャプション |
| T15 | やさしい税務会計ニュース（最新 5 件の見出し + 日付） | Resources ニュース列 | Resources | そのまま（リンクは # 固定） |
| T16 | 会話形式で楽しく学ぶ税務基礎講座 / 話題となっている「食料品消費税ゼロ」の“ゼロ”とは、どういう意味でしょうか？ | Resources カード | Resources | そのまま |
| T17 | 旬の特集 / 社会人としての基本である、電話応対についてのマナーをチェックしてみましょう。 | Resources カード | Resources | そのまま |
| T18 | WORD、EXCELでそのまま使える経理総務書式集 / ダウンロードしてそのままお使いいただける書式をご提供しております。／以下のボタンからご利用ください。 | Resources 書式集ブロック + 3 ボタン（経理向け/総務向け/契約書） | Resources | そのまま |
| T19 | アクセス本文（東北への入口…小峰城の大手門…玄関のひさしアーチ…） | Access 本文 | Access | そのまま |
| T20 | 〒961-0908 福島県白河市大手町11-15 / TEL 0248-22-5656 / FAX 0248-22-5655 / メールでのお問合せ | Contact + Footer | Contact/Footer | そのまま |
| T21 | 財務局・経済産業局認定 経営革新等支援機関 | Footer バッジ | Footer | そのまま |

## 画像マッピング

| # | 元URL（filename） | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | files/会社前01.jpg | original | photo | Hero 背景 | Hero | **そのまま**（ローカル化）|
| 2 | files/会社前02.jpg | original | photo | About 本文横画像 | About | **そのまま**（ローカル化）|
| 3 | files/所長コメント付き３.jpg | original | photo+text | Advisors カード 1 | Advisors | **そのまま**（ローカル化）|
| 4 | files/浦木先生コメント付きトリミング.jpg | original | photo+text | Advisors カード 2 上段 | Advisors | **そのまま**（ローカル化）|
| 5 | files/浦木先生著書等2025.5.27#4.jpg | original | text | Advisors カード 2 下段 | Advisors | **そのまま**（ローカル化）|
| 6 | files/遠藤先生コメント付き2025.5.27.jpg | original | photo+text | Advisors カード 3 | Advisors | **そのまま**（ローカル化）|
| 7 | files/須田先生コメント付き３.jpg | original | photo+text | Advisors カード 4 | Advisors | **そのまま**（ローカル化）|
| — | design/menu_*.png（8 枚） | original | text-embedded | HTML テキストナビに置換 | Nav | 差替 |
| — | design/caption_*.png（11 枚） | original | text-embedded | HTML 見出しに置換 | 各セクション | 差替 |
| — | design/top_caption_*.png（4 枚） | original | text-embedded | HTML 見出しに置換 | Resources | 差替 |
| — | files/会社ﾛｺﾞ*.jpg（2 枚） | original | text-embedded | HTML ロゴテキストに置換 | Header | 差替 |
| — | gazou-data.com/* 全て（TKC 外部） | template | text-embedded/icon/sashie | 削除・差替 | — | 差替 |
| — | to-pagetop.png 等 icon | template | icon | SVG 代替 | — | CSS/SVG |

## 画像ソース統一
- Advisors セクション: 全 4 カードが原則 **files/*.jpg のオリジナル composite 画像**。混在なし。画像内に氏名・資格・経歴が焼込まれているため、HTML 側は最小限のキャプション（氏名・肩書のみ）のみ付ける。
- Hero / About: 事務所外観原写真のみ。Unsplash・テンプレ一切不要。

## 非掲載（別ページ相当）
- 税務ニュース各記事の長文本文 → Resources で見出しのみ（元記事リンク無効化のため `#` または外部新サイト `https://ohtemon.tkcnf.com` への誘導）
- 今月のお仕事カレンダー本文 → 見出しリンクのみ
- 税務基礎講座の Q&A 本文 → 見出しリード + 「続きを読む」固定リンク
- 書式集のファイル個別（30 件以上）→ 経理/総務/契約書の 3 カテゴリ入口のみ
- 問合せフォーム項目 → 連絡先情報と tel: リンクに集約
