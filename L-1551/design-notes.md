# 分析結果

## アーキタイプ
名前: **B 伝統重厚 + A モダンミニマル の折衷（士業・権威系）**

根拠:
- 業種: 税理士事務所、昭和49年創業（1974年〜）、所長は早稲田大学大学院出身、山形県税理士政治連盟会長を務めた重鎮。権威性・歴史・信頼の訴求が最優先。
- 元サイトのカラーは濃紺（ネイビー）ベース、KAWAI の Y 型ロゴマーク、for you のタグラインがあり、堅実・誠実な印象。
- テキストの文体は「誠心誠意」「ここまでやってくれるのか」「独立した人格の形成と品位」など、保守的・格調高い言い回し。
- TKC 全国会員・社会保険労務士併設のトータルサポート、月次巡回監査など、情報量がそれなりにあるためモダンミニマルで余白を取りつつも、見出しは明朝体で重厚感を出す。
- カスタマー層: 山形県内の中小企業経営者（法人・個人事業）。

結論: ベースは A モダンミニマル（大胆な余白・高コントラスト・セマンティック構造）で作りつつ、見出しに Noto Serif JP を使って士業の権威・歴史を表現する。

## カラーパレット
- メイン（primary, ネイビー）: `#0b2b5c`（元サイトのネイビー色相を継承）
- サブ（secondary, ライトブルー）: `#4a6fa5`
- アクセント（accent, ゴールド）: `#b98c3d`（士業の権威・歴史を象徴）
- ベース: `#ffffff` / `#f6f7fb`（背景の薄グレー）
- テキスト: `#1a1a1a` / `#4a4a4a`
- ボーダー: `#e4e7ef`

比率目安: ベース 60% / primary 30% / accent 10%。CTA ボタンにアクセントを集中。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | img/head1.jpg | original | text-embedded | 差替 | 「川合会計事務所」ロゴ焼込 → HTML テキスト + SVG マークで代替 |
| 2 | img/head2.jpg | original | text-embedded | 差替 | 「税理士 川合賢助 / 社会保険労務士 横山郁子」バナー → HTML テキストで表現 |
| 3 | img/top_on.jpg ほか navi系 | original | text-embedded | 差替 | ナビゲーションボタン画像 → HTML ナビで置換 |
| 4 | img/about_off.jpg など | original | text-embedded | 差替 | 同上 |
| 5 | img/navi2.jpg | template | icon | CSS 代替 | 区切り装飾 |
| 6 | www.123.tkcnf.or.jp/.../btn_*.gif | template | text-embedded | 差替 | TKC 提供の共通バナー → HTML テキストリンクで代替 |
| 7 | img/spacer.gif | template | icon | 不要 | スペーサー |
| 8 | img/bird2.gif, bird2_bl.gif | template | icon | CSS/SVG 代替 | 小さな装飾 |
| 9 | img/new021_11.gif | template | icon | CSS 代替 | NEW アイコン |
| 10 | cgi-bin/Count.cgi | template | icon | 不要 | アクセスカウンタ画像 |
| 11 | **img/jimusyo.jpg** | **original** | **photo** | **そのまま引継** | **事務所外観（川合会計ビル）— 唯一無二の固有写真** |
| 12 | img/mail.gif | template | text-embedded | 差替 | 「メールはこちら」ボタン |
| 13 | img/about01_ti*.gif | original | text-embedded | 差替 | セクションタイトル焼込 |
| 14 | img/work_ti*.gif | original | text-embedded | 差替 | セクションタイトル焼込 |
| 15 | img/bu_*.gif | template | icon | CSS 代替 | 箇条書きマーク |
| 16 | img/boss_on.jpg / boss_ti*.gif | original | text-embedded | 差替 | タイトル焼込 |
| 17 | **img/boss_ph.jpg** | **original** | **photo** | **そのまま引継** | **川合賢助所長の顔写真 — 固有写真** |
| 18 | img/3-1.gif / 3-2.gif | original | text-embedded | 差替 | 「三信条」「誠意・情熱・独立」焼込 |
| 19 | img/event_on.jpg / event_ti01.gif | original | text-embedded | 差替 | タイトル焼込 |
| 20 | img/soukaikouen120919.JPG | original | photo | 差替（不採用） | 2012年のセミナー写真。古さを強調するため不採用。更新情報として 2020年コロナ関連を強調 |
| 21 | img/soukaikouen110922.JPG | original | photo | 差替（不採用） | 2011年のセミナー写真。同上 |
| 22 | img/soukaiyokyo110922_*.JPG | original | photo | 差替（不採用） | 2011年のこけし絵付け写真。同上 |
| 23 | img/seminar110411.JPG | original | photo | 差替（不採用） | 2011年の東日本大震災セミナー。同上 |
| 24 | img/square01_06.gif | template | icon | 不要 | 装飾 |
| 25 | img/sp_ti01.gif / sp_ti03.gif | original | text-embedded | 差替 | タイトル焼込 |
| 26 | https://connect.facebook.net/... | template | icon | 不要 | FB ウィジェット背景 |

### 引き継ぐ画像（ローカル化対象）
- `img/jimusyo.jpg` → `images/jimusyo.jpg`（事務所外観）
- `img/boss_ph.jpg` → `images/boss_ph.jpg`（所長顔写真）

### Unsplash 差替の考え方
- 数値的な情報（TKC 機能、業務内容）は、アイコン + テキストで表現。Unsplash 画像を多用しない。
- ヒーロー背景は上品な事務所内観・書類・万年筆等のストック画像か、CSS グラデーション + 幾何パターンで代替する。
- 士業の権威を損なう派手なストック画像（握手、CG ビジネスマン等）は使わない。
