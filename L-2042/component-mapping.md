# コンポーネント割当表 — L-2042 長谷川淳税理士事務所

## サイト構造

Header → Hero → About（ご挨拶）→ Representative（代表者略歴）→ History（沿革）→ Access（所在地・連絡先）→ Footer

モバイル追従 CTA バー（TEL + お問い合わせ）を 768px 以下で常時表示。

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 長谷川淳税理士事務所 | ヘッダーロゴ / Footer 社名 | Header / Footer | そのまま |
| T2 | home / 事務所概要 / アクセス | グローバルナビ | Header | そのまま（内部アンカーに繋ぎ替え） |
| T3 | 会津若松市の長谷川淳税理士事務所です。 | ヒーロー見出し（大） | Hero | そのまま（1 行で表示） |
| T4 | 皆様のお役に立てますよう、職員一同日々精進しております。 | ヒーローサブコピー | Hero | そのまま（1 行で表示） |
| T5 | 事務所概要 | セクション見出し | About | そのまま |
| T6 | 平成3年1月、先代の渡部浩二郎が「渡部浩二郎税理士事務所」として開業致しました。 | About 沿革本文 1 | About/History | そのまま |
| T7 | 令和3年4月より、先代の引退により長谷川淳が事務所を引き継ぎ、現在に至ります。 | About 沿革本文 2 | About/History | そのまま |
| T8 | 【 代表者略歴 】 | サブ見出し | Representative | そのまま |
| T9 | 長谷川 淳 (あつし) | 代表者名 | Representative | そのまま |
| T10 | ・慶應義塾大学商学部出身 | 略歴リスト | Representative | そのまま |
| T11 | ・平成17年税理士試験合格 | 略歴リスト | Representative | そのまま |
| T12 | ・平成28年税理士登録 | 略歴リスト | Representative | そのまま |
| T13 | アクセス | セクション見出し | Access | そのまま |
| T14 | 〒965-0008     会津若松市桧町4-1 | 住所 | Access | そのまま |
| T15 | Tel  0242-29-0088 | 電話 | Access / CTA bar | そのまま（tel: リンク化） |
| T16 | Mail : wtnb88@arion.ocn.ne.jp | メール | Access | そのまま（mailto: リンク化） |
| T17 | Copyright © 長谷川淳税理士事務所 All Rights Reserved. | コピーライト | Footer | そのまま |

**全テキスト漏れなしチェック**: 元サイトのコンテンツは上記 T1〜T17 で網羅。「コンテンツへスキップ」「ナビゲーションに移動」「MENU」「PAGE TOP」「HOME > 事務所概要」等の UI ラベル・パンくず・WordPress クレジット（「Powered by WordPress with Lightning Theme & VK All in One Expansion Unit by Vektor,Inc. technology.」）は引き継がない（新サイトの UI で自然に置き換え / WP 固有のクレジットは不要）。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | https://ah-taxacct.com/wp-content/uploads/2023/08/事務所外観-scaled.jpg | original | photo | アクセスセクションの事務所写真 | Access | **そのまま** (`images/jimusho-gaikan.jpg`) |
| 2 | https://ah-taxacct.com/wp-content/uploads/2023/08/IMG_4035-1024x769.jpg | original | photo | 代表者ポートレート | Representative | **そのまま** (`images/IMG_4035-1024x769.jpg`) |

- Hero は **写真不使用**（CSS グラデーション + Serif タイポグラフィで構成）
- ファビコンは SVG インラインで作成（CSS/SVG 代替）
- アイコン類（電話・メール・住所マーカー）は Unicode / インライン SVG

## マッピング方針

- 余白を大胆に取り、タイポグラフィ主体のモダンミニマル構成
- 見出しは Noto Serif JP（権威・信頼感）、本文は Noto Sans JP
- 主要 CTA はアクセントのゴールド（`#c9a961`）、電話リンクを目立たせる
- セクション間の流れ: Hero → 事務所紹介 → 代表略歴 → 沿革 → アクセス の順で、情報の薄さを「余白 × 丁寧なレイアウト」で補う
- 元サイトにないサービスメニュー・料金表・強み等は **AI で創作しない**（原文に無い情報は足さない）
