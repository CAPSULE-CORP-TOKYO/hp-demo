# 分析結果 — Rita税理士法人 (L-1739)

## アーキタイプ

名前: **A: モダンミニマル（プロフェッショナル信頼感）**

根拠:
- 業種は税理士法人（士業）。盛岡市津志田の地域密着型で、TKC全国会加盟・経営革新等支援機関の認定を受けた権威ある法人。
- 代表3名（渡辺誠 / 和田孝仁 / 馬内和志）の顔写真が揃っており、スタッフ集合写真やスタイリッシュなオフィス内観（木の天井・モダンな執務空間）も豊富。
- テキストは経営理念の重み（「自利利他」）と、現代的なコーポレート訴求（「Our happiness is in the prosperity of the client」「働く、くつろぐ、つながる」）が共存。
- モダンミニマルで大胆な余白・クリアな階層・高コントラストを採用し、信頼感とアクセシビリティ（特に無料税務相談訴求）を両立する。

## カラーパレット

元サイトの配色を継承（deep wine red + warm off-white）。
- メイン: **#8B1A1A**（ディープワインレッド — 元サイトのアクセント/ロゴに使用）
- サブ: **#2B2B2B**（チャコール — 本文テキスト）
- ベース: **#FFFFFF** / **#FAF7F2**（温かみのあるオフホワイト）
- アクセント: **#C9A227**（ロゴの月の金色 — CTAやハイライト小面積で使用）
- 罫線/補助: **#E8E2D5**

60-30-10: ベース(白/オフホワイト) 60% / ワインレッド 30% / ゴールド 10%。

## 画像分類（トップ候補 + サブページ候補）

| # | URL（元） | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 2 | .../58e20256c04043933f85ab90.jpg | original | photo（ロゴ） | そのまま | ロゴ（Rita税理士法人 + Rita Tax accountant office） |
| 3 | .../58e724f20b432dda074df8f5.jpg | original | text-embedded | 差替（CSS/HTML） | 「盛岡市津志田の税理士法人です お気軽にご相談ください 019-681-7311」焼込 → HTMLで再現 |
| 4 | .../61a8209c5078c498050be48b.png | stock | text-embedded | 差替 | SDGsロゴ（汎用ストック、HTMLで再現不要） |
| 5 | .../577ca6f22710da38589bc9d4.jpg | original | photo | そのまま | 都南office 外観（駐車場・建物正面）|
| 6 | .../67f383fa286a2578be639b8f.jpg | original | photo | そのまま | オフィス内観（シャレたブース）|
| 7 | .../638ede9016e37893063c61c8.jpg | original | photo | そのまま | 山と日の出（岩手の自然／象徴写真）|
| 8 | .../681304606d88431ac5a4246a.jpg | original | photo | そのまま | 木の天井・モダンなインテリア |
| 9 | .../6438a6bb00a9697d7822fedf.jpg | original | photo | そのまま | 盛岡の川と岩手山（地域象徴） |
| 24 | office: 657171d9ddd71fdc5086e2d7.jpg | original | photo | そのまま | 代表税理士 渡辺誠 |
| 26 | office: 657171e35fcebb0150417fc4.jpg | original | photo | そのまま | 代表税理士 和田孝仁 |
| 27 | office: 657171dc44c0fe2b74b05221.jpg | original | photo | そのまま | 代表税理士 馬内和志 |
| 28 | office: 65289e7b44451d4023bf5f1b.jpg | original | photo | そのまま | 代表3名 集合写真 |
| 30 | staff: 6437868188951485717b3230.jpg | original | photo | そのまま | スタッフ全員集合（階段）|
| 31 | staff: 6386e48bf704a19005d25ec8.jpg | original | photo | そのまま | 「Our happiness is in the prosperity of the client」の壁 |
| 32 | staff: 657bdc9ff5af925972ccd1e7.jpg | original | photo | そのまま | Rita税理士法人 経営支援セミナー2023 |
| 33 | staff: 6879b32a71cb5f0609d393ab.jpg | original | photo | そのまま | オフィス執務風景 |
| その他 | bnr-*.png / icon-*.png / design/images/* | template（TKC） | icon/text-embedded | 差替（CSS/Unicode） | TKCテンプレ共通素材 |
| その他 | connect.facebook.net/... | external | pixel | 除外 | トラッキング |

### 合計引き継ぎ画像

オリジナル photo として引き継ぐもの: **#2, #5, #6, #7, #8, #9, #24, #26, #27, #28, #30, #31, #32, #33** の14点。

### 画像ローカル化の使用方針

- ロゴ(#2) → Header / Footer
- 外観(#5) → Aboutセクション または Contact/Access背景
- オフィスインテリア(#6, #8, #33) → Office/カルチャーセクションのグリッド
- 自然(#7, #9) → Hero 背景 または Values 装飾
- 代表写真(#24, #26, #27) → 税理士紹介セクション（3カラム統一）
- 集合・壁・セミナー(#28, #30, #31, #32) → People/カルチャー セクション

固有写真が豊富なため、本案件は **Unsplash 差替を一切使わず** 全てオリジナル画像で構成できる。
