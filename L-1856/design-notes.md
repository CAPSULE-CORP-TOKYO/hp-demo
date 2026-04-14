# 分析結果 — L-1856 大手門会計（税理士法人）

## アーキタイプ
名前: **B: 伝統重厚**（+ E: テキストヘビー の要素も取り込む）
根拠:
- 昭和29年創業・平成14年法人化の老舗（税理士＋弁護士＋中小企業診断士ネットワーク）
- 玄関に PAX INTRANTIBVS SALVS EXEVNTIBVS（ラテン語）と東山魁夷の訳を掲げる格式
- 小峰城大手門の跡地という歴史的立地、社名由来
- 顧客層は地元経営者・相続案件、「権威 × 親しみやすさ」が軸
- 税務ニュース / 今月のお仕事 / 税務基礎講座 / 書式集 等の情報量が非常に多い

→ Noto Serif JP を見出しに使い、格式を出しつつ、余白と明朝ゴシックの階調で現代化する。
  本文は Noto Sans JP で可読性を確保（テキスト量が多いため）。

## カラーパレット

元サイトは「毛筆風ロゴ黄系 × 青グレー立体ヘッダー × 黒帯フッター」で、色相がバラバラ。
実際の事務所外観写真（kaisha01/02.jpg）から「クリーム（モルタル壁）× 深緑シャッター × 赤い花」が得られる。
玄関アーチの PAX 文字は金色に近い黄土。

これを踏まえ:
- メイン: `#1a2e3f` — 深い紺藍（事務所のシャッター緑と旧サイトの青グレーを整えた重厚色）
- サブ: `#f7f3ec` — オフホワイト／クリーム（事務所外壁の色、背景）
- アクセント: `#c0392b` — 深い朱色（CTA・ライン）事務所玄関の花と、老舗士業の信頼感
- テキスト: `#1c1c1c` / ミュート `#5a5a5a`

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | files/会社ﾛｺﾞ（ｽﾏﾎ対応）.jpg | original | text-embedded | 差替 | 社名タイポの焼込、ヘッダー用 |
| 2 | files/会社ﾛｺﾞ3-1.jpg | original | text-embedded | 差替 | 社名タイポの焼込（大） |
| 3-4, 7, 9 | design/top_caption_*.png | original | text-embedded | 差替 | 「やさしい税務会計ニュース」等の見出し焼込画像。HTML 見出しに置換 |
| 5 | gazou-data.com/.../20260410-top.jpg | template (TKC) | text-embedded | 差替 | TKC 提供の記事バナー |
| 8 | gazou-data.com/.../2603-04-top-title.jpg | template (TKC) | text-embedded | 差替 | 旬の特集バナー（電話応対） |
| 10-12 | gazou-data.com/.../keiri/soumu/keiyaku.gif | template | text-embedded | 差替 → CSS/SVG ボタン | 書式集ボタン |
| 13-20 | design/menu_*.png | original | text-embedded | 差替 → テキストナビ | 立体感メニュー画像 |
| 21 | to-pagetop.png | template | icon | CSS/SVG 代替 | - |
| 22-23, 29, 31-33, 36, 44, 47, 49 | design/caption_*.png | original | text-embedded | 差替 | セクション見出しの焼込 |
| 24 | files/所長コメント付き３.jpg | original | photo+text | **そのまま** | 所長 佐藤俊彦 写真+プロフ（テキストは画像内のみで HTML 重複なし） |
| 25 | files/浦木先生コメント付きトリミング.jpg | original | photo+text | **そのまま** | 弁護士・税理士 浦木厚利 |
| 26 | files/浦木先生著書等2025.5.27#4.jpg | original | text | **そのまま** | 浦木先生 著書等（続き） |
| 27 | files/遠藤先生コメント付き2025.5.27.jpg | original | photo+text | **そのまま** | 税理士 遠藤徳 |
| 28 | files/須田先生コメント付き３.jpg | original | photo+text | **そのまま** | 税理士 須田茂 |
| 30 | gazou-data.com/.../0003-sashie.jpg | template | diagram/sashie | 差替 | TKC 提供の記事挿絵 |
| 34 | files/会社前01.jpg | **original** | **photo** | **そのまま** | 事務所外観（3階建て全景） — Hero 画像の最有力 |
| 35 | files/会社前02.jpg | **original** | **photo** | **そのまま** | 事務所玄関（PAX アーチ確認できる） — About セクション用 |
| その他 news_*.jpg/gif, form_*.gif | template | text/icon | 差替/除外 | TKC 書式集のサムネ等。当面の面で使わない |

### 要点
- **TKC 固有画像（`gazou-data.com` ドメイン・`design/` の caption/menu/btn）はゼロにする。** すべて HTML テキストまたは SVG/CSS に置き換え。
- **引き継ぐのは `files/` 配下の固有写真のみ**（事務所外観 2 枚 + 税理士 4 人分 5 ファイル = 計 7 ファイル）。
- Hero は `files/会社前01.jpg`（事務所全景）を背景に、紺藍オーバーレイ。
- About 冒頭は `files/会社前02.jpg`（玄関 PAX アーチ）でストーリー補強。

## テキスト忠実性の要点
- ラテン語 `PAX INTRANTIBVS SALVS EXEVNTIBVS` と東山魁夷訳「歩み入るものにやすらぎを、去り行く人にしあわせを」は **原文のまま配置**（分断禁止）。
- 【ホームページリニューアルのお知らせ】は告知バナー or お知らせセクションで **原文のまま** 掲示。
- 事務所方針（社是 3 項目 + 具体 3 項目）、業務内容 8 項目は **原文をリスト化**（要約禁止）。
- アクセス本文、税務ニュース見出し、旬の特集文面、書式集紹介文も **原文そのまま**。
