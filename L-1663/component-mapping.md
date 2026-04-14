# コンポーネント割当表 L-1663

## サイト構造
Header → Hero → About（所長挨拶） → Services（業務内容＋料金） → Kigyou Flow（会社設立の流れ） → Sozoku（相続相談） → News → Access（本店＋酒田支店） → Contact CTA → Footer

## テキストマッピング（原文忠実）

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 税理士法人 大坪・阿部会計事務所 | ヘッダー ロゴテキスト | Header | そのまま |
| T2 | 千葉県市川市の税理士事務所 | ヘッダー サブ | Header | そのまま |
| T3 | 税務・会計相談 会社設立・独立開業は、市川・本八幡の税理士 大坪恭也にお任せください。 | Hero 見出し | Hero | そのまま（焼込画像の文言を HTML テキスト化） |
| T4 | 0234-25-5320（酒田支店） | Hero/CTA 電話番号 | Hero/Fixed CTA | そのまま（リードの phone） |
| T5 | 自信の会社設立～法人設立フルサポート ――― 何でも聞いてください | 会社設立セクション見出し | Kigyou Flow | そのまま |
| T6 | 法人を設立すると、個人事業で税金を納めるより税額を低く抑えられることがあります。また、個人事業と比べ社会的信頼が向上し、業種によっては受ける業務の幅も広がります。併設の行政書士事務所で、法人設立の書類を作成し、その後の税務署への各種届出作成、会計税務業務を支援いたします。 | 会社設立 本文 | Kigyou Flow | そのまま |
| T7 | サービス・料金のご案内 | Services セクション見出し | Services | そのまま |
| T8 | 併設の大坪恭也行政書士事務所「office Otsubo」提携の弁護士事務所、その他士業との連携により、企業経営、資産運用を行う上で発生する手続きや問題を包括的に解決する（ワンストップサービス）お手伝いをさせていただきます。 | Services リード文 | Services | そのまま |
| T9-12 | 開業が初めての方 / 相続でお困りの方 / 資金繰りでご相談したい方 / 会社の現状を分析してほしい方（各見出し＋本文） | 「こんな方向け」カード4枚 | Purpose Cards | そのまま（カード化） |
| T13 | 法人設立～法人顧問契約 / 所得税の申告 / 相続税の申告 / 贈与税の申告 / 資金繰りのご相談 / 財務分析・経営計画書類の作成（各説明含む） | Services カード6枚 | Services | そのまま（カード化） |
| T14 | 料金表（例）（消費税込）＋各料金 | 料金表テーブル | Services | そのまま（テーブル化） |
| T15 | 所長あいさつ（代表社員税理士 大坪 恭也 挨拶文全文） | About セクション | About | そのまま |
| T16 | 監査部 / 開発部 の説明 | About サブブロック | About | そのまま |
| T17 | ニュース・トピックス（各日付＋タイトル） | News リスト | News | そのまま（4件） |
| T18 | 相続相談について（各ページの概要文） | Sozoku セクション | Sozoku | そのまま（代表文のみ原文） |
| T19 | 【本店】〒272-0023 千葉県市川市南八幡2-16-16-3F / TEL 047-712-5671 / FAX 047-712-5672 | Access カード（本店） | Access | そのまま |
| T20 | 【支店（酒田事務所）】〒998-0054 山形県酒田市宮野浦3-6-36 / TEL 0234-25-5320 | Access カード（酒田） | Access | そのまま ※リードの phone |
| T21 | サービス対応地域（千葉県全域、東京都23区、埼玉県、神奈川県、山形県...） | Access 下部 対応地域 | Access | そのまま（アコーディオン） |
| T22 | Copyright(c) Otsubo Abe TAC ACCOUNTANT CORPORATION. All rights reserved. | Footer copyright | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 | ローカルパス |
|---|-------|------|------|----------------|-----------|------|--------------|
| 1 | header_name2.png | original | text-embedded | — | Header | CSS代替（HTMLテキスト） | — |
| 2 | top.jpg | original | text-embedded | — | — | 不使用 | — |
| 3 | staff.jpg | original | photo | Hero 背景 + About | Hero/About | そのまま | images/staff.jpg |
| 4 | shocho.jpg | original | photo | About 所長写真 | About | そのまま | images/shocho.jpg |
| 5 | top_s01-04.jpg | stock | photo | Purpose カード4枚 | Purpose Cards | Unsplash 統一差替 | — |
| 6 | seturitu.png | original | diagram | 会社設立フロー図 | Kigyou Flow | そのまま | images/seturitu.png |
| 7 | sozoku.png | original | diagram | 相続申告フロー図 | Sozoku | そのまま | images/sozoku.png |
| 8 | kakutei.png | original | diagram | 法人確定申告フロー図 | Services | そのまま | images/kakutei.png |

## 画像統一ルール
- Purpose Cards 4枚: 元は全てストック → 全て Unsplash に統一（士業・ビジネス系で4枚揃える）
- Services カード: 画像なしでアイコン（CSS/SVG 代替）で統一 → 画像の混在を避ける
- About 所長写真: original × 1枚（単独配置なので混在問題なし）

## テキスト省略ルール
- 各ページの料金詳細（相続税価格表など）は、index に全量載せると冗長なので代表サービスの料金表のみ掲載。その他は「詳細はお問い合わせください」ではなく、元サイトの「料金表（例）」の範囲を忠実に掲載
- News は index 用に4件（トピックス一覧にある最新4件）をそのまま
- 対応地域のフル展開はアコーディオンで折り畳み（原文はそのまま保持）
