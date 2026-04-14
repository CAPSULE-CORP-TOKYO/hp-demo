# 分析結果 — 堺田幸志税理士事務所 (L-1726)

## 元サイト状況
- URL: https://sakaida.tkcnf.com/
- テンプレート: TKCテンプレート（2016-2018年頃）
- 課題: アニメ風イラスト依存、バナー乱立、配色に統一感なし、情報設計散漫
- 原文コンテンツは充実（所長経歴、業務案内、よくある質問、セミナー履歴等）

## アーキタイプ
**A: モダンミニマル**

根拠:
- 業種: 税理士（士業）— 信頼性・専門性の訴求が最重要
- 所長経歴が充実（岩手県中小企業再生支援協議会統括責任者補佐、経営改善支援センター専門相談員、ＦＰ1級、行政書士、宅建等）— 権威系エッセンス
- 顧客層: 盛岡市を中心に岩手県全域、仙台、東京周辺の法人・個人
- 大胆な余白と高コントラスト、サンセリフで現代的な信頼感を作る
- 見出しは Noto Serif JP（Bold）で権威を添える、本文は Noto Sans JP（読みやすさ）

## カラーパレット
元サイトは黄・緑・青が散在して統一感なし。最も強いアクセントは TKC の緑系とナビの青系。ここでは**青（信頼・冷静）を主軸**に整理し、温かみを添える形で継承する。

- **メイン**: `#0F2E5C` （濃紺 — 信頼・落ち着き）
- **サブ**: `#1E4B8F` （ミッドブルー — ヒーロー・見出し）
- **アクセント**: `#C9A34E` （ゴールド — CTA・アクセント。権威ある士業らしい金）
- **ベース（背景）**: `#FFFFFF`
- **サブ背景**: `#F5F7FA` （薄グレー）
- **テキスト**: `#1A1A1A` 本文 / `#555` サブ

60-30-10: 白60% / 濃紺+薄グレー30% / ゴールド10%

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | library/.../201507181443_WNy3n.jpg (418x503, 実体 PNG) | original | photo | そのまま | 所長顔写真（office ページ）→ About セクションで使用 |
| 2 | library/.../201604080221_3OyDZ.JPG (1280x917 女性写真) | stock? (判別不能) | photo | 差替 | staff ページ掲載だが説明テキスト皆無。事務所実スタッフか確証なく、個人情報リスク回避のため不使用 |
| 3-n | material/lib03/bnr_*.png | template | text-embedded | 差替 | TKC 共通バナー素材、テキスト焼込 |
| 4-n | library/575526a6e4e0c92ab1621279/5756*.jpg/gif | template | text-embedded | 差替 | 「経営改善計画」等のバナー画像 |
| 5-n | library/5656ef252d0fbe3c300c1ef4/*.png (FX4クラウド等) | template | diagram/text-embedded | 差替 | TKC システム図表 |
| 6-n | connect.facebook.net/...png | stock | icon | CSS/SVG代替 | FB ピクセル、不要 |
| 7-n | design/images/common/btn-sp-menu.png, icon-*.png | template | icon | CSS/SVG代替 | メニューボタン等 |
| 8-n | images/ttl_qatax.gif, btn_pagetop.gif 等 | template | text-embedded | 不要 | 旧タイトル画像 |
| 9 | material/lib02/KFS_0*.png | template | icon | 不要 | KFS系アイコン |
| 10 | design/images/bnr-fixed/bnr-invoice-*, bnr-nensyunokabe-* | template | text-embedded | 差替 | インボイス・年収の壁の固定バナー |

**引き継ぎ画像**: 所長写真 1 枚のみ（`201507181443_WNy3n.jpg`）。
その他のヒーロー・セクション画像は **Unsplash の業務系ストック**（office, desk, accounting, business）で統一して差替。

## 備考
- 事務所外観・内観の写真はゼロ（タイトルに「事務所外観や所内など」とあるが実際の写真は存在せず、所長顔写真1枚のみ掲載）
- セミナー写真ゼロ → テキストのみで表現
- アニメ風イラストキャラクター（診断notes 記載）は全て template/stock カテゴリで差替対象
