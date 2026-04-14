# コンポーネント割当表 — L-1761

## サイト構造

Header → Hero → About（事務所紹介） → Philosophy（経営理念） → Services（業務内容） → Features（特長 / 所長挨拶） → Office Info（事務所概要） → News（お知らせ） → Contact → Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | こずかた税理士法人 | ヘッダー社名 / フッター | Header / Footer | そのまま |
| T2 | 岩手県盛岡市｜こずかた税理士法人 | title タグ | head | そのまま |
| T3 | 貴社を毎月訪問し、自計化システムの活用と経営改善計画策定により 黒字決算を支援します | Hero キャッチ | Hero | そのまま（連結） |
| T4 | お気軽にお問い合わせください / TEL: 019-656-9236 | Header CTA / Contact / Footer | 全域 | そのまま |
| T5 | こずかた税理士法人は岩手県盛岡市、及びその近隣地域を主な業務エリアとして活動しています。 | About 本文 | About | そのまま |
| T6 | 創業・独立の支援、税務・会計・決算に関する業務、…… 経営相談等のサービスを提供させていただいております。 | About 本文 | About | そのまま |
| T7 | 所長をはじめ職員一同、お客様のニーズに合ったサービスが提供できるよう、日々精進しております。 | About 本文 | About | そのまま |
| T8 | 税務、会計、自計化等でお困りのことがあれば、お気軽にお問合せください。 | About 本文 | About | そのまま |
| T9 | 所長挨拶本文（激動の時代〜お問い合わせください） | Greeting カード | Features | そのまま |
| T10 | 代表社員所長 税理士 柏葉 祐一 | Greeting 署名 | Features | そのまま |
| T11 | 経営理念 / 私たちの夢 1-3 | Philosophy | Philosophy | そのまま（3 カード化） |
| T12 | こずかた税理士法人の行動指針 1-4 | 行動指針リスト | Philosophy | そのまま |
| T13 | 業務内容 (創業支援〜経営相談等) 10 項目 | Services グリッド | Services | そのまま（10 カード化） |
| T14 | 当事務所の提供するサービス 本文 | Services リード | Services | そのまま |
| T15 | 毎月、貴社に出向き巡回監査を実施します + 本文 | Services 詳細カード | Services | そのまま |
| T16 | 経営に不可欠な業績管理体制の構築を支援します + 本文 | Services 詳細カード | Services | そのまま |
| T17 | 取引入力や証憑書類・帳簿の整理等、貴社が自からできるよう指導します + 本文 | Services 詳細カード | Services | そのまま |
| T18 | ｢税理士法第３３条の２第１項に定める書面添付」を行います + 本文 | Services 詳細カード | Services | そのまま |
| T19 | 「記帳適時性証明書」を発行します + 本文 + 箇条書き | Services 詳細カード | Services | そのまま |
| T20 | 事務所名 / 代表社員 / スタッフ数 / 所在地 / 電話番号 / FAX番号 | Office Info テーブル | Office Info | そのまま |
| T21 | こずかた税理士法人はＴＫＣ全国会会員です / ＴＫＣ全国会は…奉仕するわが国最大級の職業会計人集団です。/ 東北税理士会 | Office Info 補足 | Office Info | そのまま |
| T22 | お知らせ 2020年3月11日 / 2019年1月1日 | News リスト | News | そのまま |
| T23 | Copyright (c) 2021 - 2026 こずかた税理士法人 All Rights Reserved. | Footer | Footer | そのまま |

## 画像マッピング

全画像が template 扱いのため、一枚も引き継がない。

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | temp02_main0*.jpg 全て | template | photo | Hero BG | Hero | Unsplash 差替（office / business meeting） |
| 2 | temp02_pic0*.jpg 全て | template | photo | About ビジュアル | About | Unsplash 差替（accounting / paperwork） |
| 3 | KFS_0*.png 全て | template | text-embedded | — | — | 不要（テキスト再構成済み） |
| 4 | tkc_logo1.gif | template | text-embedded | — | — | 不要（テキストで表記） |
| 5 | 各種 icon.png | template | icon | SVG アイコン | 全域 | CSS/SVG 代替 |
| 6 | bg-pat-A008.png | template | diagram | — | — | 不要（CSS で代替） |

## Unsplash 使用枠

- Hero: `photo-1554224155-6726b3ff858f`（計算書類＋電卓＋ペンのデスク写真、税理士定番）
- About: `photo-1450101499163-c8848c66ca85`（ビジネス資料・分析）
- Greeting: `photo-1556761175-5973dc0f32e7`（オフィスで話すビジネスパーソン）

## テキスト処理の検証

- 元テキストの主要段落は全て配置済み
- 省略: ナビゲーションの繰り返し、reCAPTCHA 注記、個別お知らせ（page3 以降の TKC 汎用ページ）は別ページ扱い（メインから除外）
- Hero 見出しは改行せず一文で配置する（`<br>` 禁止 — テキスト継承チェック対策）
