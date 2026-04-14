# 分析結果 — L-1577 五十嵐俊晴公認会計士・税理士事務所

## アーキタイプ

**A: モダンミニマル**（サブ要素として B: 伝統重厚のトーン）

根拠:
- 士業（公認会計士・税理士）で信頼感・権威が最優先
- 元サイトも濃紺 × 白ベースでシンプル基調（ただし2015年前後の WP テーマ感で古い）
- 顧客層は地域の中小企業経営者・個人事業主 → 誠実・硬派な印象
- 情報量は多いがカード UI で整理されている
- 見出しには明朝体（Noto Serif JP）を部分的に使用し、信頼感を強化。本文は Noto Sans JP

## カラーパレット

元サイトの濃紺を継承する:

- メインカラー: `#0F3A63`（ディープネイビー / 元サイトのインフォ帯より）
- サブカラー: `#2D5A8C`（やや明るいネイビー、アクセント帯）
- ベース: `#FFFFFF` / `#F5F7FA`（オフホワイト / ライトグレー背景）
- テキスト: `#222222`（本文）/ `#555`（サブ）
- 罫線: `#E3E7EC`
- アクセント（CTA）: `#C99A4C`（ゴールド。士業の格調 + CTA 視認性のため追加。60-30-10 の 10%）

## 画像分類

| # | URL（ファイル名） | 出自 | 適性 | 処理 | 備考 |
|---|---|---|---|---|---|
| 1 | `logo_ogp.jpg` | original | photo | そのまま（images/logo_ogp.jpg） | ロゴ（OGP用、白背景大判）- ヘッダ用に使用 |
| 2 | `logo-bottom.png` | original | photo | そのまま（images/logo-bottom.png） | フッタ用ロゴ（透過 PNG） |
| 3 | `hdr_tel.png` | template | text-embedded | 差替 | 電話番号を画像化したもの。HTML テキスト + tel: で再現 |
| 4 | `image1.jpg` | stock | photo | 差替 | 握手等の汎用ストック |
| 5 | `sp_image1.jpg` | stock | photo | 差替 | モバイル版スライダー |
| 6 | `image2.jpg` / `sp_image2.jpg` | stock | photo | 差替 | 汎用ストック |
| 7 | `image3.jpg` / `sp_image3.jpg` | stock | photo | 差替 | 汎用ストック |
| 8 | `main_copy.jpg` / `sp_main_copy.jpg` | template | text-embedded | 差替 | キャッチコピー焼込。HTML テキストで再現 |
| 9 | `top_img001.jpg` | stock | photo | 差替 | 書類 + PC の汎用ストック |
| 10 | `top_img002.png` | template | text-embedded | 差替 | "動善なりや 私心なかりしか" 焼込 → HTML テキストで再現 |
| 11 | `bnr_img001.jpg`〜`bnr_img009.jpg` | template | text-embedded | 差替 | テンプレバナー（会社案内/業務内容/カレンダー/お客様の声/企業経営情報/医業経営情報/ビジネス書式集/国税庁/Q&A） |
| 12 | `240924_img001.jpg`（所長室） | template | text-embedded | 差替 | "Coming soon" の placeholder |
| 13 | `company_img002.jpg`（外観） | **original** | photo | **そのまま（images/company_img002.jpg）** | 事務所外観の実写 |
| 14 | `company_img004.jpg`（事務所内） | **original** | photo | **そのまま（images/company_img004.jpg）** | 執務風景の実写 |
| 15 | `company_img005.jpg`（研修室） | **original** | photo | **そのまま（images/company_img005.jpg）** | 書棚と会議机の実写 |
| 16 | `company_img007.jpg`（品質方針掲額） | original | photo/diagram | そのまま（images/company_img007.jpg） | 額装された品質方針の実写。会社案内セクションで使用 |
| 17 | `company_img008/009/010.jpg` | template | text-embedded | 差替（使わない） | 経営コーチ/jkca/kc-club 等ロゴバナー。HTML で社名表記に置換 |
| 18 | `business_img002/003/004/005.jpg` | template | text-embedded | 差替 | "法人のお客様" 等のボタン画像 → HTML ボタン |
| 19 | `business_img007.jpg`（月次決算業務図） | original | diagram | 使わない | 図表だが HTML 再構築しやすいためあえて使用しない。テキストで代替 |
| 20 | `business_img008`〜`016.jpg` | template | text-embedded | 差替 | 見出し画像等 |
| 21 | `settlement_img*.jpg` | template | text-embedded / stock | 差替 | 決算診断ページは今回メインに含めないため未使用 |
| 22 | `link_img*.jpg` | template | photo | 差替（使わない） | 外部サービスのバナー |
| 23 | `greeting_img004.jpg` | template | text-embedded | 差替（HTML テキスト） | 経営理念（顧客満足/最高のサービスの提供/知識・能力の向上/業績拡大/共存共栄・社員の幸福の追及）をテキスト再現 |
| 24 | `h1_bg_company/business/settlement/voice/link/calender/greeting.jpg` | template/stock | photo | 差替 | ページヘッダ背景のキーボード等ストック画像 |

## 引き継ぎ画像サマリー（Phase 5-0 でローカル化）

以下の 5 点のみをローカル化:

1. `logo_ogp.jpg` → `images/logo_ogp.jpg`（ロゴ OGP 版）
2. `logo-bottom.png` → `images/logo-bottom.png`（フッタ用ロゴ透過版）
3. `company_img002.jpg` → `images/company_img002.jpg`（事務所外観）
4. `company_img004.jpg` → `images/company_img004.jpg`（事務所内）
5. `company_img005.jpg` → `images/company_img005.jpg`（研修室）

上記以外は全て HTML テキスト / CSS・SVG / Unsplash で代替する。

## 画像差替方針

- ヒーロー: Unsplash の士業/会議/書類系（例: unsplash office meeting documents）
- 「法人のお客様」「個人のお客様」等のセクション: 画像は使わず、SVG アイコン + テキストのカード UI で統一
- セクション見出し背景: 使わず、CSS グラデーションで処理（画面端接触を回避しつつモダン）
