# 分析結果 — 税理士法人 斉藤会計事務所 (L-2071)

## アーキタイプ
名前: **A: モダンミニマル**（士業ベース）+ 軽く B 的権威感

根拠:
- 業種: 税理士法人（権威・信頼性・正確性が重要）
- 顧客層: 中小企業経営者、後継者問題を抱えるオーナー、地域の個人事業主（福島県須賀川市）
- 文体: 丁寧・正確・誠実（「親切・丁寧・正確をモットー」）
- 元サイトは三カラムで情報量は多いが古典的 TKC テンプレ。リデザインでは余白を広く取り、見出しで情報をカテゴライズ、CTA 導線を強化する
- 明朝体の見出しで士業の権威感を少しだけ出し、本文は Noto Sans JP で読みやすさ重視

## カラーパレット
元サイトは青基調の典型的 TKC テンプレ。色相（青系）を継承しつつ、深みと彩度を調整してモダンに。

- メイン: `#0f2b52`（深いネイビー。信頼・権威）
- サブ: `#1e4a8a`（鮮やかなブルー。アクセント寄り）
- アクセント: `#c49a3f`（品のある金茶。CTA / 差し色）
- 背景ベース: `#ffffff` / `#f5f7fa`（ライトグレー）
- テキスト: `#1a1a1a`（濃グレー）

## 画像分類

元サイトの画像は **全て TKC テンプレート由来 or テキスト焼込バナー** で、斉藤会計事務所固有の写真（代表者・事務所外観/内観・スタッフ等）は **ゼロ**。Google Maps の地図を除き、事務所の実写素材は存在しない。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | SP メニューアイコン |
| 2 | library/.../58871ef684ce28143b7f987f.png | original | text-embedded | 差替（HTML テキスト化） | 社名ロゴ（テキスト PNG） |
| 3 | library/.../58871ecf84ce28143b7f9878.png | original | text-embedded | 差替（HTML テキスト化） | TEL 画像 |
| 4 | material/lib03/bnr_saiyou009_d.png | template | text-embedded | 差替/削除 | TKC 採用バナー |
| 5 | library/.../58a3bf1f9b39b750248ed410.png | template | text-embedded | 差替/削除 | お役立ちコーナー見出し |
| 6 | material/lib02/tkc_logo1.gif | template | icon | 不要 | TKC 全国会ロゴ（文言で代替） |
| 7-10 | library/.../58a2ce69*.jpg (hero スライダー4枚) | template | text-embedded | Unsplash 差替 | 「ご満足を最優先…」焼込 |
| 11 | library/.../58a2ce69befe75cf12136f39.jpg | template | text-embedded | 不要 | 重複 |
| 12-22 | library/.../* (lib03/bnr_*) バナー群 | template | text-embedded | 差替（カード化） | サービス案内バナー |
| 23 | library/.../588804a23d7072eb4bd1d3c6.jpg | original | text-embedded | 差替（HTML テキスト化） | TEL 画像 |
| 24 | library/.../58789d8a5428df78316f1026.jpg | template | text-embedded | 差替（CTA ボタン化） | お問合せフォーム |
| 25-30 | design/images/bnr-fixed/* | template | text-embedded | 差替/削除 | 固定バナー（インボイス・年収の壁） |
| 31 | library/.../587845d4aac8bdbf7a2e3d60.jpg | template | photo/bg | Unsplash 差替 | CSS 背景、線香花火/夜景 |
| 32 | connect.facebook.net/*.png | template | icon | 不要 | FB トラッキング |
| 33-151 | その他サブページのバナー群 | template | text-embedded | 差替/削除 | 全て TKC テンプレ |

**結論**: **引き継ぐ画像ゼロ**。images/ ディレクトリは空でもよいが、Hero 背景・About セクション等に Unsplash の高品質画像（オフィス・事務所内観・ビジネス系）を使用する。CSS/SVG で代替可能な装飾はそれらで置き換える。

## 画像戦略
- **Hero 背景**: Unsplash の「office」「business desk」「japanese office」等から抽象度の高い落ち着いた画像を選定
- **About セクション**: 書類・書き物のクローズアップや、落ち着いたオフィス内観
- **Service カード**: アイコン（SVG）+ テキストで構成。写真は使わない（統一性確保のため）
- **Contact セクション**: 事務所の存在感を出したい → 抽象的な建物 or オフィス画像

## レイアウト方針
- ヒーロー: 大判ビジュアル + 社名 + キャッチコピー + CTA 2つ（電話・問合せフォーム）
- About: TKC 全国会員・東北税理士会所属・親切丁寧正確モットー
- Services: 8〜10 枚のサービスカード（相続、事業承継、経営支援、TKC システム、BAST、補助金情報、経営革新等支援機関、etc）
- Highlight: 経営革新等支援機関認定、TKC 全国会会員
- Office info: 住所・電話・FAX・Google Maps 埋込（既存リンク）
- Contact CTA バンド + Footer
