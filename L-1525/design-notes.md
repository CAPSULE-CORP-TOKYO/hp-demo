# 分析結果

## アーキタイプ

名前: **A: モダンミニマル**（B 伝統重厚のニュアンスを一部取り入れ）

根拠:
- 業種は税理士法人（士業 / 権威系）で B: 伝統重厚も候補だが、採用サイトのミッション表現やロゴ（ASAHI + 三角形モチーフ）、代表写真の背景ウッドパネル + 金属レターのアート演出から、会社自体は「東北最大級・総勢160名超・RPA 研究所併設」等のモダンな経営支援系を打ち出している。
- 伝統的な士業の重厚さを残しつつ、余白を大きく取り現代的にリフレッシュするのが最適。
- 見出しにはセリフ（Noto Serif JP）を一部採用して士業の格を出し、本文はサンセリフで可読性を確保する。

## カラーパレット

元サイトは「茶系 + ベージュ」で、ロゴと応接棟のウッドパネル写真から落ち着いたブラウン系が主色。この色相を継承する。

- メイン: `#8B5A3C`（サドルブラウン。ロゴの茶系を継承）
- サブ: `#F5EDE4`（アイボリー / ベージュ背景）
- ダーク: `#2E211B`（見出し・テキストの濃茶）
- アクセント: `#C8281F`（スクリーンショットの赤丸マーカーと「検索」ボタンの赤を継承。CTA に集中）
- ベース: `#FFFFFF` / `#FAF7F2`

60-30-10:
- base `#FFFFFF` / `#FAF7F2` (60%)
- primary `#8B5A3C` + `#F5EDE4` (30%)
- accent `#C8281F` (10%, CTA のみ)

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../themes/responsive_056/images/logo_top.png | original | photo(logo) | そのまま | ロゴ。ヘッダーで使用 |
| 2 | .../uploads/2018/10/f889871dbfeb65dfd92aef17449c8f56.jpg | original | photo | そのまま | 田牧大祐代表の顔写真（ウッドパネル背景）。About セクションで使用 |
| 3 | .../uploads/2018/02/DSC_8547-1-800x300.jpg | original | photo | そのまま | 職員集合写真（事務所外観バック）。Hero or Company Section で使用 |
| 4 | .../uploads/2018/10/a6110c5977711f130eff803c88c688e9-800x300.jpg | original | photo | そのまま | 「あさひ会計ブレインズサポートセンター」看板 + 代表。About / Company で使用可 |
| 5 | .../uploads/2018/10/asahi_top_2015.12.10-877x329.jpg | original | text-embedded | 差替 | 「私達は、質の高い仕事を通じ…」焼込。HTML テキスト化 |
| 6 | .../themes/responsive_056/images/tamaki.JPG | original | photo | 重複除外 | #2 と同じ田牧代表。採用しない |
| 7 | .../themes/.../bu/bu_chusho.jpg 〜 bu_souzoku.png | template | text-embedded | 差替 | 業務ナビバナー（「中小企業向け」「税務・会計」等の焼込）。CSS カード化 |
| 8 | .../themes/.../banners/banner_tel.jpg | template | text-embedded | 差替 | 「お問合せは今すぐこちらへ」TEL 焼込。CSS ボタン化 |
| 9 | .../themes/.../banners/banner_keieikakushin.jpg | template | text-embedded | 差替 | 経営革新支援バナー焼込。CSS バッジ化（または除外） |
| 10 | .../themes/.../banners/banner_yamagata_pf.jpg | template | text-embedded | 差替 | 山形プラットフォームバナー。除外 |
| 11 | .../themes/.../banners/banner_souzoku.jpg | template | text-embedded | 差替 | 相続サポートセンター。CSS カード化 |
| 12 | .../themes/.../banners/banner_ma.jpg | template | text-embedded | 差替 | M&A サポートセンター。CSS カード化 |
| 13 | .../themes/.../banners/banner_npo.jpg | template | text-embedded | 差替 | 非営利法人サポート。CSS カード化 |
| 14 | .../themes/.../banners/banner_brains.jpg | template | text-embedded | 差替 | 旭ブレインズ。CSS カード化 |
| 15 | .../themes/.../banners/haken_banner.jpg | template | text-embedded | 差替 | 派遣事業。CSS カード化 |
| 16 | .../themes/.../images/map.jpg | template | text-embedded | 差替 | アクセスマップ（テキスト焼込）。Google Maps iframe or CSS 代替 |
| 17 | .../themes/.../images/header_hojin_no.jpg | template | text-embedded | 差替 | 法人番号。HTML テキストで表示 |
| 18 | .../themes/.../banners/230x60.png（ミラサポ） | stock | icon/ad | 差替 | 外部サービス広告。削除 |
| 19 | .../emoji/.../25b6.svg | system | icon | CSS/SVG 代替 | ▶ 絵文字。Unicode で代替 |

## 引き継ぎ判定（Phase 5 でローカル化する画像）

1. `logo_top.png` → `images/logo_top.png`
2. `f889871dbfeb65dfd92aef17449c8f56.jpg` → `images/daihyo_tamaki.jpg`
3. `DSC_8547-1-800x300.jpg` → `images/staff_group.jpg`
4. `a6110c5977711f130eff803c88c688e9-800x300.jpg` → `images/brains_sign.jpg`

その他の画像は全て差替（CSS カード / アイコン / 除外）。

## フォント方針

- 見出し: **Noto Serif JP**（weight 600/700）— 士業の格と信頼感
- 本文: **Noto Sans JP**（weight 400/500）— 可読性
- 数字（実績データ）: **Noto Sans JP** 700 でインパクト

## レイアウト方針

- 1 カラム構成（元サイトの 2 カラム + 左サイドリンク羅列は廃止）
- Hero → Philosophy(Mission) → Stats → About(代表挨拶) → Services → Group → Access → Contact → Footer
- 全幅 max-width 1120px、モバイル container padding 24px
- 見出し下に茶系の細いアクセントライン（B 伝統重厚の余韻）
