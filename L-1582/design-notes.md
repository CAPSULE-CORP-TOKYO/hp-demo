# 分析結果 — L-1582 税理士法人 おおぞら総合会計事務所

## 元サイト概要
- URL: https://www.tkcnf.com/hide-katocpa
- スタイル: TKC 定型テンプレート（2010年代前半）、青グラデ背景、左サイドナビ、PC固定幅
- 固有画像: ロゴ（テキストのみ / シンボル+テキスト）、代表者写真、事務所外観、会議室、執務室、スタッフ集合写真、個別スタッフ写真多数
- TKC テンプレ装飾画像（クリップアート風キャラ・テキスト焼込バナー）多数あり

## アーキタイプ
名前: **A: モダンミニマル**（権威感を適度に付与）
根拠:
- 業種: 士業（税理士法人）
- 顧客層: 中小企業経営者・個人事業主
- 権威系の性格もあるが、文体は親しみやすく「お気軽にご相談下さい」「関与先企業の繁栄は私たちの喜びです」等フレンドリー寄り
- 元サイトの色相（青）を継承しつつ、大胆な余白・サンセリフ中心で現代化
- 見出しは Noto Serif JP で権威・信頼感を、本文は Noto Sans JP で可読性を確保するハイブリッド

## カラーパレット
元サイトは青グラデ主体、ロゴシンボルも青系。色相を継承して調整。
- メイン（primary）: `#1E3A8A`（ロゴの濃い青 #203d89 ベース）
- サブ（base/background）: `#F5F7FB`（薄いブルーグレー、元サイトの淡い青背景を継承）
- テキスト: `#1A2238`（濃紺寄り）
- アクセント: `#D97706`（代表者のネクタイのオレンジを継承、CTA に集中）
- ボーダー/サブグレー: `#E2E8F0`

60-30-10:
- base (#F5F7FB / #FFFFFF) 60%
- primary (#1E3A8A) 30%
- accent (#D97706) 10%

## フォント
業種判定: 士業（権威＋親しみ）→ ハイブリッド
- 見出し（ヒーロー H1・セクション H2）: Noto Serif JP 700
- 本文・UI: Noto Sans JP 400/500/700

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../common/btn-sp-menu.png | template | icon | CSS/SVG 代替 | ハンバーガー |
| 2 | .../5a685b65b85c77e761f9e6bc.png | original | text-embedded | CSS 代替 | 社名テキストロゴ（テキストのみ）→ HTML テキストで再現 |
| 3 | .../62ff4013a5d77cd705eda064.jpg | template | photo | 差替 | 内容不明（バナー） |
| 4 | .../683d357817b8354339ab28cb.png | template | text-embedded | 差替 | バナー |
| 5 | .../tkc_logo1.gif | template | icon | 差替 | TKC バナー（フッターで小さく表示） |
| 6 | .../bnr_fourseasons_c.png | template | text-embedded | 差替 | 経営者の四季バナー |
| 7 | .../59f9593bb70490d020f06212.jpg | template | photo | 差替 | 経営改善支援ストック |
| 8 | .../59f95983f8e6c173158f7df4.jpg | template | photo | 差替 | 事業承継ストック |
| 9 | .../59f959839cb431f00cb6f77b.jpg | template | photo | 差替 | 相続対策ストック |
| 10-20 | 各種 TKC 装飾バナー | template | text-embedded | 差替/省略 | バナー群 |
| 14 | .../5a685b8a711baed96016ae69.png | original | text-embedded | **そのまま引き継ぎ** | 社名+シンボルロゴ。シンボル部分が固有のため使用。背景透過 PNG |
| 23 | office: .../575fb4aa44861b2a0b002dc4.jpg | original | text-embedded | 差替 | おしょうしな（テキスト焼込） |
| 24 | office: .../201407171651_1NAs6.jpg | template | text-embedded | 差替 | 事務所紹介（テキスト焼込、古いキャラ画像） |
| 25 | office: .../59f95a93dc1026af249670a0.jpg | original | photo | **そのまま** | 代表者挨拶写真（加藤英樹）— 純写真、質高い |
| 26 | office: .../59f95ae0dc1026af249670b9.jpg | original | photo | **そのまま** | 事務所外観 — 純写真、建物にロゴ看板 |
| 27 | office: .../59f95ae0f46b4fc119f98b57.jpg | original | photo | **そのまま** | 会議室 — 純写真 |
| 28 | office: .../59f95adf1247128224ebe010.jpg | original | photo | **そのまま** | 執務室 — 純写真 |
| 32 | staff: .../683d0a73ac8a3a43406895f0.jpg | original | photo | **そのまま** | スタッフ集合写真 — 純写真、新しい（日付的にも） |
| 34-46 | staff: 個別スタッフ写真 | original | photo | — | ページ簡略化のため 1 ページ版では省略（About の集合写真のみ使用） |

## 引き継ぎ画像リスト（Phase 5-0 でローカル化）

| local filename | URL |
|---|---|
| logo.png | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/5a685b8a711baed96016ae69.png |
| representative.jpg | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/59f95a93dc1026af249670a0.jpg |
| office-exterior.jpg | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/59f95ae0dc1026af249670b9.jpg |
| meeting-room.jpg | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/59f95ae0f46b4fc119f98b57.jpg |
| work-room.jpg | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/59f95adf1247128224ebe010.jpg |
| staff-group.jpg | https://www.tkcnf.com/library/575e58d2ace2665de4991fc7/683d0a73ac8a3a43406895f0.jpg |

## 差替方針（TKC テンプレ装飾・クリップアート等）
- ヒーロー背景: 事務所外観の純写真を使う（office-exterior.jpg を base でオーバーレイ）→ Unsplash 不要
- サービスカード背景: CSS/SVG アイコン（電卓・書類・計算・握手等）で代替
- ロゴ: logo.png をヘッダー・フッターで使用
