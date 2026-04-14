# コンポーネント割当表

## サイト構造

- Header（ロゴ＋ナビ＋TEL）
- Hero（キャッチ・サブコピー・CTA）
- Introduction（ＴＫＣ全国会会員・自利利他の抜粋）
- Services（業務内容 5 本柱）
- Action Guidelines（TKC 会計人の行動指針 6 項目 / 折りたたみ）
- Office Info（事務所概要）
- Career / History（事務所紹介の経歴）
- Access（住所・TEL・FAX・メール）
- Contact CTA
- Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 李寿仁税理士事務所・桂会計／ＷＯＮＤＥＲＳ | ロゴテキスト | Header | そのまま |
| T2 | 成す事は自然に成され、得たい物は自然と得て、全てが収まるところへ収まっていく。 | ヒーロー見出し | Hero | そのまま（1行で改変なし） |
| T3 | 直感や感性、閃き、インスピレーションなどが花開く時代です。 | ヒーローサブコピー | Hero | そのまま |
| T4 | 李寿仁税理士事務所／　桂会計 はＴＫＣ全国会会員です | 所属見出し | Introduction | そのまま |
| T5 | ＴＫＣ全国会は、租税正義の実現をめざし関与先企業の永続的繁栄に奉仕するわが国最大級の職業会計人集団です。 | 所属説明 | Introduction | そのまま |
| T6 | いわき所属 | バッジ | Introduction | そのまま |
| T7 | 業務内容 ①〜⑤（5 本柱全文） | サービスカード 5 枚 | Services | カード化（原文そのまま） |
| T8 | 月次巡回監査の実施 / お客様と毎月面談し〜 | サービス詳細カード | Services | カード化 |
| T9 | 自計化支援 / お客様自らパソコン入力〜 | サービス詳細カード | Services | カード化 |
| T10 | 独立・創業支援 / お客さんの考えを〜 | サービス詳細カード | Services | カード化 |
| T11 | 事業再生・事業改善計画策定支援 | サービス詳細カード | Services | カード化（タイトルのみ） |
| T12 | 業績管理体制の構築支援 / 四半期〜半年毎に〜 | サービス詳細カード | Services | カード化 |
| T13 | 事業承継・相続対策支援 / 還暦を迎えた〜 | サービス詳細カード | Services | カード化 |
| T14 | ＴＫＣ会計人の行動指針 + 1〜6 の見出しと 1-1〜6-4 の全 24 項目 | 6 グループのアコーディオン | Action Guidelines | アコーディオン（原文全文） |
| T15 | 事務所概要（事務所名 / 所在地 / 電話番号 / FAX番号 / 業務内容） | 定義リスト | Office Info | そのまま |
| T16 | 事務所紹介 経歴（1988-2022 の全文） | タイムライン | Career | そのまま |
| T17 | 経営理念 見出し + 「地域社会に貢献〜」「誠実さを動機〜」 | 理念セクション | Philosophy | そのまま |
| T18 | 「自利利他」の理念の実践とは（飯塚毅の長文引用） | 折りたたみ or 引用ブロック | Philosophy | アコーディオン（原文全文） |
| T19 | 福島県いわき市平字愛谷町１－４－１０ | 住所 | Access | そのまま |
| T20 | 0246-21-8737 / 0246-21-8738 | TEL/FAX | Access | そのまま（tel: リンク） |
| T21 | t-lee-katsura@tkcnf.or.jp | メール | Access / Footer | そのまま（mailto リンク） |
| T22 | お気軽にお問合せください。 | CTA 見出し | Contact CTA | そのまま |
| T23 | Copyright (c) 2023 - 2026 TOSHIHITO LEE All Rights Reserved. | コピーライト | Footer | そのまま |
| T24 | 経営革新等支援機関とは（2012年11月取得） | バッジ / 経歴 | Career | そのまま |

## 画像マッピング

| # | 元 URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| all | — | template/stock | — | — | — | **Unsplash 差替または CSS/SVG 代替（全て）** |

元サイトに引き継ぐべきオリジナル画像がないため、ビジュアルは以下で構成する:

| 用途 | セクション | ソース | URL |
|------|-----------|--------|-----|
| Hero 背景 | Hero | Unsplash | https://images.unsplash.com/photo-1436450412740-6b988f486c6b（朝日・自然光の木々） |
| Introduction 装飾 | Introduction | Unsplash | https://images.unsplash.com/photo-1528164344705-47542687000d（和紙・書の質感） |
| Services ヘッダ装飾 | Services | CSS グラデーション + SVG アイコン | — |
| Career 背景 | Career | Unsplash | https://images.unsplash.com/photo-1450101499163-c8848c66ca85（オフィス・書類） |
| Philosophy 背景 | Philosophy | Unsplash | https://images.unsplash.com/photo-1528164344705-47542687000d |
| Access マップ | Access | Google Maps iframe（embed API 使用せず、静的リンクボタンのみ） or プレースホルダ | — |

Unsplash は URL パラメータ `?w=1600&q=80&auto=format&fit=crop` を付けて軽量化。

## 処理ルール遵守

- 全サービスカードの画像は CSS/SVG アイコンで統一（Unsplash とオリジナル混在させない）
- ヒーローとセクションヘッダの Unsplash 画像は色相を揃える（自然・木・和 の系統）
- CTA ボタンはゴールド #D4A017 に統一
