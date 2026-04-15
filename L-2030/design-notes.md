# 分析結果 — L-2030 島尾雅行税理士事務所

## アーキタイプ
名前: A モダンミニマル
根拠:
- 業種: 税理士（士業）。若手所長（2013年開業、独立14年目）、会津若松の地域密着。
- 客層: 中小企業経営者・個人事業主・創業希望者。信頼感と専門性が必須。
- 文体: 落ち着いた敬語、専門的だが親しみやすい。
- 元サイトは TKC テンプレ未完成（プレースホルダー残存・コンテンツ空白多数・CTA 不明瞭）で、現代的な情報整理と CTA 強調が必要。
- 「モダンミニマル」で大胆な余白・サンセリフ・高コントラストにし、「若手・対話重視・地域に寄り添う」というブランドを表現する。

## カラーパレット
元サイトはヘッダ・見出しが TKC テンプレ標準のシアン/アクア系。色相を継承。
- メイン: `#0EA5BF`（深めのシアン、信頼感）
- サブ: `#0F172A`（紺寄りの墨色、見出し）
- アクセント: `#F59E0B`（CTA 用、温かみのあるアンバー）
- 背景ベース: `#FFFFFF` / セクション交互に `#F5FAFB`
- 補助テキスト: `#475569`

## フォント
- 見出し: Noto Sans JP 700/800（モダン士業）
- 本文: Noto Sans JP 400/500
- 数字・英字アクセント: Inter 600

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | design/images/common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | UI アイコン |
| 2 | library/.../69a7b1af...png | original | text-embedded | 差替（HTMLテキスト化） | 「島尾雅行税理士事務所」テキストロゴ |
| 3 | library/.../69a7b3dd...png | original | text-embedded | 差替（HTMLテキスト化） | TEL 番号焼込画像 |
| 4 | library/.../69a7cd63...png | original | text-embedded | 差替（HTMLテキスト化） | CONTACT ボタン焼込 |
| 5,6 | library/.../69b774a9...png | template | text-embedded | 差替 | ヒーローキャッチ焼込（テンプレ） |
| 7 | material/lib01/57797329.jpg | template | photo | Unsplash 差替 | 「ご挨拶」用テンプレ写真 |
| 8 | material/lib01/77622619.jpg | template | photo | 不要 | bg 装飾 |
| 9 | material/lib01/54358380.jpg | template | photo | 不要 | bg 装飾 |
| 10 | material/lib01/63118049.jpg | template | photo | 不要 | bg 装飾 |
| 11-13 | library/.../69a7c6f...png | original | text-embedded | 差替 | 「事務所紹介」等の見出し焼込 |
| 14 | material/lib01/106230503.jpg | template | photo | Unsplash 差替 | サービスバナー |
| 15 | material/lib01/106235276.jpg | template | photo | 不要 | bg 装飾 |
| 16 | library/.../69a7cbf9...png | template | icon | CSS 代替 | page top |
| 17 | library/.../69a7d099...png | original | text-embedded | 差替 | フッターロゴ（テキスト焼込） |
| 18-23 | design/images/bnr-fixed/* | template | text-embedded | 不要 | 固定バナー（電帳法・年収の壁） |
| 29-36 | library/.../about... | template | photo/text-embedded | 差替/Unsplash | about ページ用テンプレ素材 |
| 37-49 | service ページ系 | template | mixed | 差替/CSS 代替 | 全 TKC テンプレ素材 |
| 51-60 | recruit ページ系 | template | photo | 不要 | 採用ページ用テンプレ素材 |
| 61-81 | tkc-ebooks/年収の壁 | template | text-embedded | 不要 | TKC 共通バナー、本案件と無関係 |

**結論**: 元サイトに固有写真ゼロ、ロゴすらテキスト焼込のみ。
- 引き継ぐ画像: **なし**（images/ にダウンロードする画像はゼロ）
- ヒーローおよびセクションビジュアルは Unsplash の士業/オフィス系画像で統一
- ロゴはテキスト＋シンボル（CSS）で表現

## レイアウト指針
- Hero: 大判背景（Unsplash 会津/山並み or オフィス）+ 半透明オーバーレイ + 見出し（原文「あなたと地域を支える、安心のパートナー」を分断せず1行〜2行に）+ 紹介文 + CTA 2 本
- About/Greeting: 2 カラム（Unsplash 士業ポートレート + 原文ご挨拶）
- Features: 3 カード（Feature01-03、原文そのまま）
- Services: 5 サービス（税務会計/自計化・デジタル化支援/創業支援/経営支援/相続・事業承継）
- Office: 表＋地図埋め込み（Google Maps Embed、住所クエリ）
- News: 1件（2026.03.24 リニューアル）
- Contact: TEL + 問い合わせフォーム URL リンク
- Footer: 事務所情報 + ナビ + コピーライト
- モバイル: ハンバーガー + 追従 CTA バー
