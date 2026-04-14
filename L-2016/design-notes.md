# 分析結果 — 遠藤久税理士事務所 (L-2016)

## 元サイト
- URL: https://www.tkcnf.com/endouzeirishi (兄弟ドメイン: https://tkc-nf.com/endouzeirishi)
- プラットフォーム: TKCネットワーク CMS（テンプレート 4.3.18）
- 診断スコア: 7/10 (html:3, visual:4)
- 問題: 2015年頃のテンプレ流用、中央コンテンツが空白だらけ、事務所独自の魅力が伝わらない

## 企業の特徴（text-inventory から抽出）
- 1988年（昭和63年）開設、会津若松市八日町で37年以上の実績
- 代表: 遠藤 久（国税専門官 第6期生、税理士番号63621）
- 所属税理士: 遠藤 博人（令和7年2月20日登録、税理士番号155894）
- 職員12名（税理士2、監査担当7、事務3）
- 強み: 農業法人・福祉法人対応、政治資金監査人、経営革新等支援機関
- 対応地域: 会津若松市・喜多方市・南会津郡・耶麻郡・河沼郡・大沼郡
- 本人・代表・スタッフ・事務所外観の原写真が豊富

## アーキタイプ
**B: 伝統重厚（ただし過度に格式張らず、地域密着の信頼感を前面に）**

根拠:
- 昭和63年創業、代表が 70代、地方都市（会津若松）、地域に根ざした士業
- 顧客層は地元中小企業・農業法人・相続相談者で、派手さより誠実さ・実績を求める
- 既存サイトも落ち着いた青系でシンプル、信頼感重視
- 一方、若手税理士（遠藤博人）・採用情報・DX支援などモダン要素もあるため、重厚すぎず読みやすさも確保

実装方針:
- 見出しのみ Noto Serif JP（威厳）、本文は Noto Sans JP（読みやすさ）
- 余白をたっぷり取り、横幅 1080-1160px の落ち着いたレイアウト
- 写真は現場の代表・職員・事務所外観を主役にする（既存サイトは TKC 固有画像ゼロだが、office-info / strength / recruit-interview ページに本物の写真が大量に埋もれている）
- 数字・年次（1988年 / 37年 / 12名 / 125日）を印象的に見せる

## カラーパレット
既存サイトはほぼモノトーン＋差し色青緑系。継承しつつ落ち着きを強化:

- メイン: `#0f3e52`（深い藍 / 代表写真背景の青緑をトーンダウン）
- サブ: `#f4f1ea`（温かいクリーム / 背景）
- アクセント: `#b8944a`（抑えた金 / CTA とライン）
- テキスト: `#1f2a2e`（ほぼ黒）
- 補助: `#c9d6dc`（淡い青グレー / カード枠）

60-30-10: クリーム背景60% / 深藍30% / 金10%

## 画像分類

オリジナル写真を積極的に引き継ぐ。TKCテンプレの焼き込み画像（イラスト・見出しバナー）は全排除。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | library/.../6971d72fa17a3b0d38020e67.jpg | original | photo | そのまま | 事務所外観（看板付き、全体） |
| 2 | library/.../697c339f6d76b84461c9a9cd.jpg | original | photo | そのまま | 事務所外観（別アングル） |
| 3 | library/.../6971d859abf395369736415e.jpg | original | photo | そのまま | 代表 遠藤 久 ポートレート（A） |
| 4 | library/.../6971d85970374e0d31a0a445.jpg | original | photo | そのまま | 遠藤 博人 ポートレート（A） |
| 5 | library/.../698af09257566857bb59efef.jpg | original | photo | そのまま | 代表 遠藤 久 ポートレート（B） |
| 6 | library/.../698aefd69eeefb10776662e4.jpg | original | photo | そのまま | 遠藤 博人 ポートレート（B） |
| 7 | library/.../6971d2ab7e99c425987540d4.jpg | original | photo | そのまま | 看板プレート（税理士 遠藤久事務所／東北税理士会会員） |
| 8 | library/.../6971d2aba201043a964f8274.jpg | original | photo | そのまま | 代表が執務中（PC作業） |
| 9 | library/.../6971d2ab269d970bf0d6cde3.jpg | original | photo | そのまま | 女性スタッフが電話対応 |
| 10 | library/.../6971d2ab70374e0d31a0a3b1.jpg | original | photo | そのまま | 3人ミーティング風景 |
| 11 | library/.../6971d74aabf3953697364142.jpg | original | photo | そのまま | ノートPCで作業する手元 |
| 12 | library/.../6971d74970374e0d31a0a429.jpg | original | photo | そのまま | アクリル看板アップ |
| 13 | library/.../6971d74a8377cd369e814e86.jpg | original | photo | そのまま | 応接室・会議室内観 |
| 14 | library/.../6971d74a3ee60f0d3f6b3df6.jpg | original | photo | そのまま | TKC 2025 完全防衛推進事務所表彰状 |
| 15 | library/.../6971d74a8377cd369e814e87.jpg | original | photo | そのまま | 社訓の書（4枚額） |
| 16 | library/.../6971d74ae9fa8629b21ff31b.jpg | original | photo | そのまま | TKC企業防衛マスターズ会員プレート |
| 17 | library/.../6971d74ad6773210047a3d5a.jpg | original | photo | そのまま | ふくしま健康経営優良事業所認証状 |
| 18 | www.tkcnf.com/library/.../6971d3ffe9fa8629b21ff2ac.png | original | text-embedded | 差替 | 社名ロゴ（テキスト再現で CSS 代替） |
| 19 | material/lib01/14973348.jpg | template/stock | photo | 差替 | TKCテンプレ背景（会議室、ストック） |
| 20 | design/images/common/btn-sp-menu.png | template | icon | CSS 代替 | ハンバーガーボタン |
| 21 | design/images/bnr-fixed/bnr-*.png | template | text-embedded | 差替 | TKC 固定バナー（電帳法・年収の壁）— 不要 |
| 22 | library/.../693f*.png 一連（ご挨拶、バナー、イラスト） | template | text-embedded | 差替 | CMS上の見出しバナー・説明アイコン — HTML 見出しで代替 |
| 23 | library/.../6972*.png 一連（税務カレンダー/共済等） | template | text-embedded | 差替 | 機能バナー — 不要（NEWS リンクで代替可能だが v6 では含めない） |
| 24 | material/lib07/* | template | text-embedded | 差替 | サービスカード用のテンプレ画像 — 不要 |
| 25 | library/.../5743c72e...（元気活力朝礼） | original | photo | 差替 | 240x180 と極小すぎ使用しない |
| 26 | library/.../5da6c5b8...（お花見） | original | photo | そのまま | 1440x960 職員集合写真（任意で使用） |
| 27 | library/.../5a0cfc3d...（社員旅行） | original | photo | そのまま | 1440x960 職員集合写真（任意で使用） |

## 採用する画像方針
- Hero: 看板付き事務所外観（#1）— 地域に根ざした雰囲気
- About: 代表ポートレート（#5, 落ち着いた B アングル）
- Team: 代表A + 博人A の2枚
- Office: 看板プレート（#7）, 会議室（#13）, ミーティング（#10）
- 強みセクション: 数字ベース（1988 / 37年 / 12名 / 125日）で写真は最小限

## 画像の論理的統一
- ポートレート系はすべて同一カメラマンの同ライティングで撮影されており、統一感あり
- 事務所外観・内観も同シリーズ、混在問題なし
