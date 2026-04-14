# コンポーネント割当表 — L-1822

## サイト構造

Header / Hero / About / Philosophy / Services / Office / Staff / News / Access / Contact / Footer

## テキストマッピング（原文そのまま使用）

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 佐藤英耕税理士事務所 | ヘッダーロゴ / Footer 社名 | Header/Footer | そのまま |
| T2 | 奥州市,税理士 | Header サブ | Header | そのまま（メタ風） |
| T3 | 当事務所は皆様の様々なニーズにお応えします。 | Hero サブリード | Hero | そのまま |
| T4 | 会計業務・税務申告だけが税理士業務では有りません。 | Hero 本文 | Hero | そのまま |
| T5 | 会社発展の全てをサポートし、経営者の皆様の悩みを解決する佐藤英耕税理士事務所のHPへようこそ！ | Hero 本文 | Hero | そのまま |
| T6 | 佐藤英耕税理士事務所は、平成８年に税理士事務所としての一歩を踏み出し、平成１１年１０月現事務所への移転を期に父が経営する佐藤剛税理士事務所と統合しました。これからの新しい時代を先取りする皆様のパートナーとしてお役に立てるよう、持てる力すべてを提供いたします。 | About 本文 | About | そのまま（2文） |
| T7 | 岩手県奥州市水沢 + 近辺記述 | About リード文 | About | そのまま（原文結合は避ける） |
| T8 | 経営理念 4項目 | Philosophy カード4枚 | Philosophy | そのまま |
| T9 | 業務案内のリード3行（お客様の繁栄は〜） | Services リード | Services | そのまま |
| T10 | 会計業務/経営コンサルティング/その他業務 各3-5項目 | Services カード3枚 | Services | カード化 |
| T11 | 事務所外観や所内など（レンガ色の建物〜） | Office 本文 | Office | そのまま |
| T12 | 所長経歴 + 所属団体資格 | About / Staff 下部 | About/Staff | そのまま |
| T13 | 職員紹介（勤務中は黙々〜） + 所長〜所員 12名 | Staff 本文 | Staff | そのまま |
| T14 | お知らせ（事業承継/相続対策/所員募集中）3項目 | News カード3枚 | News | カード化 |
| T15 | 交通案内（駐車場 / 所在地 / 電話番号） | Access 本文 | Access | そのまま |
| T16 | 事務所概要（所名/所長名/所在地/電話/FAX/業務内容/メール） | Contact Info テーブル | Contact | そのまま |
| T17 | ＴＫＣ全国会会員です + 東北税理士会所属 | Footer バッジ | Footer | そのまま |
| T18 | Copyright (c) 2024 - 2026 Sato Eikou All Rights Reserved. | Footer | Footer | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| H1 | .../5f4f3bc54b92bbc7772bb9aa.jpg | original | photo | 代表写真（丸型） | About | **そのまま**（ローカル化 `images/rep.jpg`） |
| H2 | .../56ff5245cb8619c9650003eb.jpg | original | photo | 事務所外観 | Office | **そのまま**（`images/office-ext.jpg`） |
| H3 | .../56ff5247cb8619c9650003ec.jpg | original | photo | 事務所玄関 | Office | **そのまま**（`images/office-entrance.jpg`） |
| H4 | .../56ff5248cb8619c9650003ed.jpg | original | photo | 事務所内観 | Office | **そのまま**（`images/office-interior.jpg`） |
| H5 | .../tkc_logo1.gif | original | photo | TKC 全国会バッジ | Footer | **そのまま**（`images/tkc-logo.gif`） |
| X1 | 社名文字焼込画像 | original | text-embedded | — | — | **差替**（テキスト化） |
| X2 | 各スライダー画像 | template | photo | — | — | **差替**（Hero は CSS グラデーション + 図形装飾、Unsplash 不使用で安全） |
| X3 | お役立ちボタンgif群 | template | text-embedded | — | — | **差替**（SVG アイコン + テキストリンク） |

**統一性**:
- Office セクションは3枚の原本写真（外観／玄関／内観）で統一。
- その他セクションには画像を差し込まず、タイポ＋色面＋SVG アイコンで構成してソース混在を避ける。

## テキスト処理のサマリ

- **そのまま**: 大半
- **カード化**: Services 3カード、News 3カード、Philosophy 4カード
- **別ページ**: TKC システム詳細ページ群、お役立ちコーナー、プライバシー条項（メインページには載せない）
