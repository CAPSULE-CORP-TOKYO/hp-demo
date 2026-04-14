# 分析結果 — 菖蒲会計事務所（菖蒲雅弘税理士事務所）

## アーキタイプ
**名前: A: モダンミニマル（＋B:伝統重厚を部分継承）**
根拠:
- 業種: 税理士事務所。士業のため「信頼感」「専門性」「誠実さ」を軸にしたモダンミニマルが最適。
- 所長の語り（方言「けろ！！」、笑顔応援）に人間味があり、純粋にドライなコンサル調ではなく、親しみ込みのトーンが合う。
- 元サイトの赤系（えんじ色系）は権威・伝統色。完全に捨てずにアクセントとして継承し、ベースはオフホワイトのクリーンな配色で刷新する。
- 見出しだけ Noto Serif JP、本文は Noto Sans JP とし、士業らしい格と可読性を両立する。

## カラーパレット
元サイトは焦げ赤（えんじ）主体の TKC temp05 赤パターン。色相を継承しつつ彩度/明度を調整。

- **メイン（Primary / アクセント）**: `#8a1d1d`（深いえんじ / CTA・見出し下線）
- **セカンダリ（ベース背景）**: `#fbf9f5`（温かみのあるオフホワイト）
- **テキストダーク**: `#1f1a17`（ほぼ黒）
- **テキストミュート**: `#6b615d`
- **ボーダー/サブ背景**: `#ede6db`（ベージュ）
- **アクセントライト**: `#c9472d`（ホバー・リンク色）

比率: base `#fbf9f5` 60% / text `#1f1a17` 30% / primary `#8a1d1d` 10%。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | /design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | SP メニューアイコン |
| 2 | /material/lib02/temp05_main01.jpg | template | photo | Unsplash 差替 | 兼六園（TKC temp05 付属） |
| 3 | /material/lib02/temp05_main02.jpg | template | photo | Unsplash 差替 | 富士山（TKC temp05 付属） |
| 4 | /material/lib02/temp05_main03.jpg | template | photo | Unsplash 差替 | 尾瀬（TKC temp05 付属） |
| 5 | /material/lib02/tkc_logo1.gif | template | text-embedded | CSS/SVG 代替 | TKC 全国会ロゴ（テキスト＋SVG風に再現） |
| 6 | /library/.../6113cc7b...jpg | original | photo | **そのまま引き継ぎ** | 所長・菖蒲雅弘氏の顔写真 |
| 7 | /library/.../6113cc29...jpg | original | photo | **そのまま引き継ぎ** | 事務所看板（真鍮プレート「菖蒲雅弘税理士事務所」） |
| 8-12 | /material/lib02/KFS_01〜05.png | template | text-embedded | 差替（不使用） | TKC KFS バナー |
| 13-14,17-18 | /design/images/bnr-fixed/bnr-*.png | template | text-embedded | 差替（不使用） | 電帳法・年収の壁バナー |
| 15-16 | /design/images/common/icon-*.png | template | icon | CSS/SVG 代替 | 開閉アイコン |
| 19 | /design/images/bg/bg-pat-B022.png | template | pattern | 不要 | 背景パターン |
| 20 | facebook.net fav | template | icon | 不要 | FB トラッキング |
| 21-25 | /material/lib02/tempcommon_p04_*.jpg | template | photo | Unsplash 差替 | 業務内容ページ TKC 共通素材 |
| 26-27 | /material/lib02/tempcommon_p07_*.jpg | template | photo | Unsplash 差替 | 料金ページ TKC 共通素材 |
| 28-50 | /library/.../ブログ・記事図表 | template | diagram/text-embedded | 不使用 | ブログ・インボイス・年収の壁記事。トップデモ対象外 |

**引き継ぎ画像（ローカル化対象）**:
- `6113cc7ba0677dd006961660.jpg` → `daihyo.jpg`（所長写真）
- `6113cc29a9e3476107772464.jpg` → `kanban.jpg`（看板写真）

**Unsplash 差替**:
- ヒーロー背景: 税理士/会計/書類イメージ
- 特長セクション: 必要なら business/office ジャンル（なければ CSS 装飾のみ）
