# コンポーネント割当表: L-1387 株式会社ステップ

## サイト構造

1. **Header**（ロゴ + ナビ + TEL） 
2. **Hero**（大判外観写真 + キャッチ + CTA）
3. **About / Greeting**（代表挨拶 + 社名・代表名）
4. **Merit**（当社にご依頼いただくメリット — 3項目）
5. **Services**（クリニック向け 6 サービス）
6. **Fee**（料金案内）
7. **Staff**（スタッフ紹介 — 4名カード + その他メッセージ）
8. **Office**（アクセス・会社概要 + 沿革 + 外観/内観写真）
9. **Contact**（電話 + 問合せフォームリンク）
10. **Footer**
11. 768px 以下: モバイル追従 CTA バー

---

## テキストマッピング

| ID | 元テキスト（text-inventory 抜粋） | 新コンポーネント | セクション | 処理 |
|----|----------|----------------|-----------|------|
| T1 | 株式会社ステップ / 税理士法人ステップ | ヘッダーロゴ alt + 文字 | Header | そのまま |
| T2 | 0246-29-5600 | ヘッダー TEL / Contact CTA / Footer | Header/Contact | そのまま（tel: リンク） |
| T3 | ホーム / 会社案内 / サービス案内 / 料金案内 / セミナー情報 / 採用情報 | ナビ | Header | そのまま |
| T4 | 税理士による医業開業コンサル / 福島県の株式会社ステップ | ヒーロー見出し（Eyebrow + H1） | Hero | そのまま |
| T5 | 私たちの仕事の本質は、お客様の抱えるさまざまな不安を取り除き、前向きな気持ちで業務を進めていただくお手伝いをすることだと考えています。 | ヒーローリード文 | Hero | そのまま |
| T6 | お客様の悩みのポイントを見極め、解決策を見出し、「大丈夫ですよ」と背中を押して差し上げることのできる存在でありたい。その思いは、昭和60年の創業以来、片時も忘れたことはありません。 | About 本文 | About | そのまま |
| T7 | 大切なのは、お客様と共に、同じ方向を向いて歩んでいくこと。望まれた回答をご提供するだけの「for」ではなく、共に考え、共に成長する「with」の姿勢を信条に、今日も業務にあたっています。 | About 本文 | About | そのまま |
| T8 | 私たちは長きにわたり、医療に従事する方々のサポートを続けてまいりました。...（中略） | About 本文 | About | そのまま |
| T9 | 今後とも、お客様のニーズに応え、自信をもって「大丈夫です」とお声がけができるよう、所員一同研鑽を深め、成長を続けていく所存です。 | About 本文 | About | そのまま |
| T10 | 株式会社ステップ 代表取締役 坂本弥一 | About 署名 | About | そのまま（greeting ページから） |
| T11 | 当社にご依頼いただくメリット | Section title | Merit | そのまま |
| T12 | クリニック開業、医療法人設立、承継のサポートはお任せください | Merit カード1 見出し | Merit | そのまま |
| T13 | 医療に携わるみなさまに、その手腕を余すところなく発揮していただくための環境づくりを後押しいたします。...（中略） | Merit カード1 本文 | Merit | そのまま |
| T14 | クリニックの経営改善、医療法人化についてもご相談ください | Merit カード2 見出し | Merit | そのまま |
| T15 | 適切なサービスを提供しながら、...（中略）...準備を整えています。 | Merit カード2 本文 | Merit | そのまま |
| T16 | 「地域包括ケアシステム」構築のネットワークづくりをお手伝いします | Merit カード3 見出し | Merit | そのまま |
| T17 | 医療と介護を融合する形で、...（中略）...事業展開をご提案していきます。 | Merit カード3 本文 | Merit | そのまま |
| T18 | クリニックのための6つのサービス（ホームタイトル） | Section title | Services | そのまま |
| T19 | クリニック開業支援 | Service カード1 タイトル | Services | そのまま |
| T19b | これからクリニックを開業しようと準備を進めている方は、.../当社では、開業までに必要な一連の作業についてワンストップでご支援しています。 | Service カード1 本文 | Services | そのまま（冒頭 2 文に圧縮せず、リード文 2-3 行そのまま） |
| T20 | クリニック経営改善支援 | Service カード2 タイトル | Services | そのまま |
| T20b | クリニックを取り巻く経営環境は大きく変化しています。...絶え間ない「経営改善」の努力によって、経営の健全化、経営体質の強化を図ることが、クリニックの存続・発展と理想の医療の実現のためには不可欠であると言えます。 | Service カード2 本文 | Services | そのまま（リード要約でなく原文の最終段落） |
| T21 | 会計支援 | Service カード3 タイトル | Services | そのまま |
| T21b | 記帳指導・月次巡回監査／経営分析・相談業務／リスクマネジメント業務 | Service カード3 本文リスト | Services | そのまま |
| T22 | 事業承継支援 | Service カード4 タイトル | Services | そのまま |
| T22b | 事業承継の形は、時代とともに変化してきています。...当事務所は今後も積極的に支援に取り組んでまいります。 | Service カード4 本文 | Services | そのまま |
| T23 | 医療法人設立支援 | Service カード5 タイトル | Services | そのまま |
| T23b | 医療法人化をお考えの方へのサポートも充実しています。...確実な経営基盤づくりを支援いたします。 | Service カード5 本文 | Services | そのまま |
| T24 | 介護事業支援 | Service カード6 タイトル | Services | そのまま |
| T24b | 厚生労働省が提唱する「地域包括ケアシステム」の重要性が高まりを見せる中、...暮らしやすい環境づくりの実現を目指しています。 | Service カード6 本文 | Services | そのまま |
| T25 | 料金案内 | Section title | Fee | そのまま |
| T26 | 当社では、開業支援の料金については開業までに所要した年数に関わらず、一律で記載価格にてご支援しています。 | Fee リード | Fee | そのまま |
| T27 | 一般的な相場よりも安価であると言われることも多くありますが、それ以上に私どもが勉強になっていると感じることが多いためです。 | Fee リード | Fee | そのまま |
| T28 | 開業支援 / 一律330,000円（税込） | Fee カード1 | Fee | そのまま |
| T29 | 医業顧問料（開業後の経営支援）／月額 50,000円（税込）〜 ※売上高や業務量により増減することがあります。／別途決算料 月額の5ヶ月分／介護事業については別途ご相談ください | Fee カード2 | Fee | そのまま |
| T30 | スタッフ紹介 | Section title | Staff | そのまま |
| T31 | 草野 滋 / 副所長 税理士 / 元気に。わかりやすく。丁寧に。親身あるよき相談相手になれるようつとめてまいります。 | Staff カード1 | Staff | そのまま |
| T32 | 宮下 昌之 / 医業経営コンサルタント 診療放射線技師 / 幅広い視野でお客様を全力でサポート致します。 | Staff カード2 | Staff | そのまま |
| T33 | 矢代 あきこ / サブマネージャー / お客様の笑顔のため最善を尽くしてまいります。 | Staff カード3 | Staff | そのまま |
| T34 | 門馬 昭子 / サブマネージャー / お客様とのコミュニケーションを大切にしながらご満足いただける仕事ができるよう何事も全力で取り組みます。 | Staff カード4 | Staff | そのまま |
| T35 | その他のスタッフ / 巡回監査担当者 7名 / 総務・その他 4名 | Staff 補足 | Staff | そのまま |
| T36 | アクセス・会社概要 | Section title | Office | そのまま |
| T37 | 会社名: 株式会社ステップ（税理士法人ステップ） | Office 会社概要 | Office | そのまま |
| T38 | 住所: 〒970-8034 福島県いわき市平上荒川字長尾16番地 | Office 会社概要 | Office | そのまま |
| T39 | TEL: 0246-29-5600 / FAX: 0246-28-5361 | Office 会社概要 | Office | そのまま |
| T40 | 沿革: 昭和60年5月 坂本喜一税理士事務所 開業 / 昭和63年7月 有限会社坂本タックスプランニングセンター 設立 / 平成3年11月 組織変更により、株式会社ステップを設立 / 令和7年4月 先代の逝去に伴い、株式会社ステップ代表取締役変更 / 令和7年5月 税理士法人ステップを設立 | Office 沿革タイムライン | Office | そのまま |
| T41 | 業務内容: タックス＆コンサルの専門事務所として、...専門家（弁護士、司法書士、社会保険労務士）との連携により、迅速な対応を行います。 | Office 業務内容 | Office | そのまま |
| T42 | 所属団体: ＴＫＣ全国会 / ＴＫＣ医業会計システム研究会 / 全国Viewシステム会 / 日本医業経営コンサルタント協会 | Office 所属団体 | Office | そのまま |
| T43 | アクセス: いわき駅から車で7分 / 常磐交通・上荒川公園口で下車してすぐ / 駐車場あり | Office アクセス | Office | そのまま |
| T44 | お問合せ | Section title | Contact | そのまま |
| T45 | 〒970-8034 福島県いわき市平上荒川字長尾16番地 さかとみクリニックビル 2F | Contact 住所 | Contact | そのまま（leads.json address をベース、元サイトは 16番地までなので「さかとみクリニックビル 2F」はリード DB 由来、これは補足情報として別行で追加しない。Office セクションで原文16番地のみ使用） |
| T46 | Copyright (c) 2026 株式会社ステップ All Rights Reserved. | Footer | Footer | そのまま |

注: T45 の「さかとみクリニックビル 2F」は leads.json 側の情報で、元サイト側には記載なし → 原文優先で Office セクションは「福島県いわき市平上荒川字長尾16番地」とする。

---

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| img01 | .../6842a91efaa7c712354a1ebd.jpg (step ロゴ) | original | photo | ヘッダーロゴ | Header | **そのまま**（ローカル化: `logo.jpg`） |
| img02 | .../61947e0317e3c02c06de29f5.png (外観) | original | photo | Hero 背景/右カラム | Hero | **そのまま**（ローカル化: `office_exterior.png`） |
| img03 | .../61947a4cf107221c069af511.png (外観帯合成) | original | photo | About セクション帯 or Office | Office | そのまま（ローカル化: `office_hero.png`） |
| img04 | .../619701ac029a3c0706ecf4a4.png (草野) | original | photo | Staff カード1 | Staff | **そのまま**（ローカル化: `staff_kusano.png`） |
| img05 | .../636b347f7d86678636a742a7.jpg (宮下) | original | photo | Staff カード2 | Staff | **そのまま**（ローカル化: `staff_miyashita.jpg`） |
| img06 | .../623a652ab2d85e5b272cd416.png (矢代) | original | photo | Staff カード3 | Staff | **そのまま**（ローカル化: `staff_yashiro.png`） |
| img07 | .../619701ac029a3c0706ecf4a3.png (門馬) | original | photo | Staff カード4 | Staff | **そのまま**（ローカル化: `staff_momma.png`） |
| img08 | .../61948eaec529b13b062035b9.png (会議室) | original | photo | Office ギャラリー | Office | **そのまま**（ローカル化: `office_in_meeting.png`） |
| img09 | .../61948eadf107221c069af8bf.png (執務デスク) | original | photo | Office ギャラリー | Office | **そのまま**（ローカル化: `office_in_desk.png`） |
| img10 | .../6194919fa89ea4270682667c.png (受付) | original | photo | Office ギャラリー | Office | **そのまま**（ローカル化: `office_reception.png`） |
| — | .../68467e7fc1c02c0fbc768766.jpg (Medical Consulting) | original | text-embedded | — | Hero | 差替（img02 を使う） |
| — | .../611c68ffd2fba5515b7fbc7c.png (TEL バナー) | template | text-embedded | — | — | 差替（HTML で tel:） |
| — | .../617762bd*.png 他サービス6枚 | template | text-embedded | — | Services | 差替（SVG アイコン + HTML） |
| — | .../611ca62fd2fba5515b7fc5d3.png / 6842ad04*.png / 619718330b... 等 | template | text-embedded | — | — | 差替（HTML 見出し） |
| — | material/lib01/*.jpg | stock | photo | — | — | 不要 |
| — | bnr-invoice-*.png / bnr-nensyunokabe-*.png | template | text-embedded | — | — | 不要 |
| — | icon-close.png / icon-open.png / btn-sp-menu.png | template | icon | — | — | **CSS/SVG 代替** |

### 統一性チェック

- Staff カード 4 枚 → 全て original×photo で統一 ✓
- Service カード 6 枚 → 全て「HTML + SVG アイコン」で統一（元画像はテキスト焼込のため）✓
- Office ギャラリー → original×photo 3 枚で統一 ✓

### ダウンロード対象（Phase 5-0 で取得）

1. logo.jpg — https://www.tkcnf.com/library/575526a0d00dee027371eabf/6842a91efaa7c712354a1ebd.jpg
2. office_exterior.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/61947e0317e3c02c06de29f5.png
3. office_hero.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/61947a4cf107221c069af511.png
4. staff_kusano.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/619701ac029a3c0706ecf4a4.png
5. staff_miyashita.jpg — https://www.tkcnf.com/library/575526a0d00dee027371eabf/636b347f7d86678636a742a7.jpg
6. staff_yashiro.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/623a652ab2d85e5b272cd416.png
7. staff_momma.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/619701ac029a3c0706ecf4a3.png
8. office_meeting.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/61948eaec529b13b062035b9.png
9. office_desk.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/61948eadf107221c069af8bf.png
10. office_reception.png — https://www.tkcnf.com/library/575526a0d00dee027371eabf/6194919fa89ea4270682667c.png
