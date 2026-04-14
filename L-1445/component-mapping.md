# コンポーネント割当表

## サイト構造

- Header（固定、ロゴ＋ナビ＋TEL）
- Hero（キャッチ＋CTA）
- About（事務所紹介 / 所長挨拶）
- Philosophy（経営理念）
- Services（業務内容）
- Strength（当事務所の特長）
- Pricing（料金について）
- Office（事務所外観・会議室）
- News（お知らせ）
- Access（事務所概要）
- Contact（CTA）
- Footer
- Mobile sticky CTA bar

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|----------|----------------|-----------|------|
| T1 | 三上貴也税理士事務所 | ロゴテキスト | Header | そのまま |
| T2 | TEL: 0229-25-8167 | ヘッダー右 / CTA | Header, Contact | そのまま（tel: リンク） |
| T3 | 気軽に相談できる専門家にお任せ下さい | ヒーローキャッチ（サブ） | Hero | そのまま |
| T4 | 貴社を毎月訪問し、自計化システムの活用と経営改善計画策定により黒字決算を支援します | ヒーローメイン見出し | Hero | そのまま |
| T5 | 三上貴也税理士事務所のサービス〈会計・税務でお悩みの会社経営者、個人事業主様〉三上貴也税理士事務所は、巡回監査の実施により、お客様と毎月面談し、会計資料並びに会計記録の適法性、正確性及び適時性を確認します。これにより、経営者の意思決定に役立つデータを提供し、会計、税務や経営面のアドバイスを行います。この際、経営面のアドバイスでは、毎月の面談等を通して得られるお客様からの情報や『ＴＫＣ経営指標』の同業他社比較等によって、お客様の強みや経営課題等を分析・報告します。 | サービス説明リード | About | そのまま |
| T6 | 三上貴也税理士事務所の特長 1〜3 | 特長カード3枚 | Strength | そのまま |
| T7 | 事務所紹介（page2 本文 2段落） | About本文 | About | そのまま |
| T8 | 所長挨拶（page2 5段落） | 所長挨拶ブロック | About | そのまま |
| T9 | 所長経歴（氏名・出身地・学歴・趣味） | 所長プロフィール | About | そのまま |
| T10 | 経営理念（page3 3項目） | 経営理念カード | Philosophy | そのまま |
| T11 | 事務所の行動指針「独立自尊」4項目 | 行動指針リスト | Philosophy | そのまま |
| T12 | 業務内容（page4）(1)〜(6) + 本文4ブロック | サービスカード6 + 説明 | Services | そのまま |
| T13 | 料金について（page5 本文 + 法人/個人料金） | Pricingセクション | Pricing | そのまま |
| T14 | お知らせ5件（2025.12.12〜2022.04.01） | Newsリスト | News | そのまま |
| T15 | 事務所概要（住所・TEL・FAX・業務内容・ＴＫＣ全国会会員等） | Access / Footer | Access, Footer | そのまま |
| T16 | 営業時間 平日8:30〜17:00 土日祝日は休業 | Access補足 | Access | そのまま |
| T17 | Copyright (c) 2025 - 2026 三上貴也税理士事務所 All Rights Reserved. | Footer copyright | Footer | そのまま |
| T18 | 適格請求書発行事業者登録番号 T4810917133490 | Footer/Access | Access | そのまま |

**長文原則**: 経営理念本文（「自利利他」の哲学解説）、ＴＫＣ会計人の行動指針（1〜6の詳細）はページのスクロール性を考慮し、**アコーディオン**にせず通常のセクションで展開する（読み物的な士業の権威訴求に必須）。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | .../62da574cb5f1b9ec051e6925.png | original | text-embedded | — | — | 差替（ヘッダーはテキストロゴ） |
| 2 | .../6239170bcd1b4f0a0673354d.png | original | photo(illust) | 所長挨拶の肖像 | About | そのまま引き継ぎ → `images/chairman-illust.png` |
| 3 | .../62464f5571a0ee3606e05942.jpg | original | photo | 事務所外観カード | Office | そのまま → `images/office-exterior.jpg` |
| 4 | .../62425c4ac0e523f6053073e0.jpg | original | photo | 会議室カード | Office | そのまま → `images/meeting-room.jpg` |
| 5 | .../tkc_logo1.gif | template | photo | TKC全国会会員表記 | Footer | そのまま → `images/tkc-logo.gif` |
| 6 | .../slideshow*.jpg | template | photo | — | Hero | Unsplash 差替（ビジネスシーン） |
| 他 | TKC素材全般 | template | various | — | — | Unsplash or CSS代替 |

**統一性**: Office セクションの2枚（外観・会議室）はどちらも original photo で統一。
所長セクションは1枚のみ（イラスト似顔絵）なので単独表示。
Hero は Unsplash 風景1枚または CSS グラデーション背景で対応（混在禁止）。
**本デモでは Hero は CSS グラデーション + subtle pattern のミニマル構成**とする（TKCスライダー素材は全滅のため、Unsplash は外観/会議室との統一性のために使わない）。

## Phase 5-0 ダウンロード対象

1. `https://mikamikaikei.tkcnf.com/library/622ed8ef3ac3893a0aba065c/6239170bcd1b4f0a0673354d.png` → `images/chairman-illust.png`
2. `https://mikamikaikei.tkcnf.com/library/622ed8ef3ac3893a0aba065c/62464f5571a0ee3606e05942.jpg` → `images/office-exterior.jpg`
3. `https://mikamikaikei.tkcnf.com/library/622ed8ef3ac3893a0aba065c/62425c4ac0e523f6053073e0.jpg` → `images/meeting-room.jpg`
4. `https://mikamikaikei.tkcnf.com/material/lib02/tkc_logo1.gif` → `images/tkc-logo.gif`
