# コンポーネント割当表

## サイト構造

1. **Header** — ロゴ（社名テキスト）+ ナビ + TEL
2. **Hero** — 上杉銅像・天地人・米沢市街のスライダー風（CSS のみ、静的複数枚でOK）+ キャッチコピー + CTA
3. **About（事務所紹介 / 経営理念）** — 社名変更のご挨拶 + モットー + 自利利他揮毫
4. **Representatives（代表者紹介）** — 代表社員・副所長のポートレート2枚 + 経歴
5. **Services（業務案内）** — 税務・会計・記帳代行・コンサル・相続・税務調査立会の6カード
6. **Management Philosophy（経営理念 & 行動指針）** — 経営基本方針 + ＴＫＣ会計人の行動指針（アコーディオン化）
7. **Office（事務所概要）** — 事務所名・所長・登録番号・住所・電話・FAX・業務内容 + TKC全国会所属
8. **News（新着情報）** — トップに載ってる10件の固定リスト
9. **Access（交通案内）** — 住所・JR米沢駅から車で10分 + Google Maps iframe
10. **Contact** — TEL / メール / お問合せ文
11. **Footer** — コピーライト
12. **Mobile Sticky CTA** — 768px 以下で TEL + お問合せ

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 税理士法人　松田パートナーズ会計 | ヘッダーロゴ | Header | そのまま（Noto Serif JP） |
| T2 | 山形県米沢市の税理士法人　松田パートナーズ会計 | ヒーローサブタイトル | Hero | そのまま |
| T3 | 会計業務、税務申告だけが税理士業務では有りません。/ 会社発展の全てをサポートし、経営者の皆様の悩みを解決いたします。 | ヒーロー見出し | Hero | そのまま |
| T4 | 当法人のモットーは「元気な人づくり、企業づくり、町づくり」です。 | ヒーロー下部 + About | Hero/About | そのまま |
| T5 | （office）社名変更のご挨拶 本文 | About セクション本文 | About | そのまま |
| T6 | 代表社員・所長 税理士 松田純一（経歴） | 代表者カード1 | Representatives | そのまま |
| T7 | 副所長 税理士 岩間正満（経歴） | 代表者カード2 | Representatives | そのまま |
| T8 | 業務案内（税務業務・会計業務・記帳代行・コンサル・相続・税務調査立会） | Services 6 カード | Services | そのまま |
| T9 | 経営理念 1〜3 | Philosophy セクション | Philosophy | そのまま |
| T10 | 自利利他の解説（飯塚毅の言葉） | Philosophy 引用ブロック | Philosophy | そのまま |
| T11 | ＴＫＣ会計人の行動指針（6項目 x 4細目） | Philosophy アコーディオン | Philosophy | アコーディオン |
| T12 | 事務所概要（9項目） | Office 定義リスト | Office | そのまま |
| T13 | TKC全国会会員です + 東北税理士会所属 + TKC全国会の説明 | Office 補助文 | Office | そのまま |
| T14 | 新着情報 10件 | News リスト | News | そのまま |
| T15 | 山形県米沢市城西2丁目3番70号 / JR米沢駅から車で10分 | Access | Access | そのまま |
| T16 | TEL 0238-40-0301（代）/ FAX 0238-40-0401（代）/ matsuda-junichi＠tkcnf.or.jp | Contact + Header + Sticky CTA | Contact | そのまま |
| T17 | お気軽にお問合せください。 | Contact 見出し | Contact | そのまま |
| T18 | Copyright (c) 2025 - 2026 matsuda-sasaki All Rights Reserved. | Footer | Footer | そのまま |

**漏れチェック**: TKC 関連サブページ（tkc-menu7-003 = 病院・診療所向け、tkc-menu8-003 = 社会福祉法人向け 等）は TKC グループ共通テンプレで、松田会計固有の文言ではない。メインナビには含めず、Services セクション最下部に「業種別サポート」として社会福祉法人・病院診療所の2つをリンクなしで見出しのみ表示する（元サイトのメニュー構造を尊重）。

**別ページ送り（今回は収録しない）**: form/inquiry ページは連絡先のみ抽出。tkc-syatyou-menu-asp、tkc-system-qa 等のツール誘導ページはテンプレ流用なので除外。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| A | .../571777d02fd8cc921100064d.jpg | original | photo | ヒーロー画像1 | Hero | そのまま → images/hero1.jpg |
| B | .../571777d22fd8cc921100064e.jpg | original | photo | ヒーロー画像2 | Hero | そのまま → images/hero2.jpg |
| C | .../571777d32fd8cc921100064f.jpg | original | photo | ヒーロー画像3 | Hero | そのまま → images/hero3.jpg |
| D | .../5d390fcb8507fe8a17e912e1.jpg | original | photo | 代表社員ポートレート | Representatives | そのまま → images/rep1.jpg |
| E | .../5d301bc17f60cd0977dadb2a.jpg | original | photo | 副所長ポートレート | Representatives | そのまま → images/rep2.jpg |
| F | .../571777d82fd8cc9211000652.png | original | photo | 自利利他揮毫 | Philosophy | そのまま → images/jiririta.png |

**その他の元サイト画像**: 全て差替 or 不要。ストック系画像は一切使わない（Unsplash も含めて使わない）。写真が足りないセクションは CSS グラデーション・アイコン SVG・テキストのみで構成する。

## 統一性チェック

- Representatives セクション: ポートレート2枚あり → 統一OK
- Hero: 3枚とも地元米沢の風景で統一
- Services: 6カードは全て SVG アイコンで統一
- Office: 画像なし、定義リスト+TKC会員ロゴはテキストのみ
- Philosophy: 揮毫1枚のみ（引用ブロック専用）

OK、画像混在なし。
