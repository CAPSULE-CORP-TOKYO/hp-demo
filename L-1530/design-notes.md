# 分析結果 — 井上公認会計士事務所 (L-1530)

## アーキタイプ
名前: **A: モダンミニマル**

根拠:
- 業種は税理士・公認会計士（士業、コンサル系）。
- 客層は中小企業経営者・創業者・資産税ニーズを持つ個人。プロフェッショナルな信頼感と、同時に「若さ・IT・クラウド会計」を訴求する必要がある。
- 文体は「世界一のNo.2」「変化を恐れず」「わかりやすく伝わる」など明快でポジティブ。重厚系ではない。
- 元サイトは既にモダン WordPress 実装で、丸み控えめ・余白豊富・サンセリフ・大判の写真。リデザイン後もこの方向を継承し、より洗練させる。
- 注意: webPresence=own_site で diagnosis は http→https の SSL 問題のみ（htmlScore=1）。デザインはモダンのまま、SSL / 情報整理 / 可読性 / モバイル対応を高める方向でリデザインする。

## カラーパレット
元サイトのキーカラー（value アイコンの緑系）と黒ベースを継承する。

- メイン（primary ブランドカラー）: `#2F7D4E`  （深みのあるグリーン。信頼・成長・クラウド会計らしさ）
- サブ（dark text / nav）: `#111827`  （ほぼ黒。見出し・本文の主テキスト）
- ベース（背景）: `#FFFFFF` / `#F5F7F5`  （白 + 微かに緑がかったオフホワイト）
- サブテキスト: `#4B5563`  （段落本文）
- ボーダー・罫線: `#E5E7EB`
- アクセント（CTA）: `#1F5F3A`  （primary の濃色版。CTA ボタンに集中使用）
- 補助アクセント: `#F0B400`  （#No.2 バッジなど最小限のワンポイント）

60-30-10 配分:
- 60% = 白 / オフホワイト
- 30% = 黒に近いダークグレー（見出し・本文・ヘッダーフッター）
- 10% = グリーン（アクセント・CTA・リンク・見出しの装飾）

## 画像分類

元サイトには豊富な original × photo 画像（スタッフ集合写真・オフィス風景・代表写真）がある。これらは全てそのまま引き継ぐ価値が高い。一方、value アイコン／ill_* アイコン／text-embed 系 svg は CSS/SVG 代替。

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| 1 | .../themes/inouekaikei-cpa/images/logo.svg | original | diagram | そのまま | 事務所ロゴ。複合 SVG、そのまま使える |
| 6 | .../home/t-mv_1.jpg | original | photo | そのまま | スタッフ集合写真（ヒーロー候補） |
| 7 | .../home/t-mv_2.jpg | original | photo | そのまま | 代表が顧客と面談（ヒーロー候補） |
| 8 | .../home/t-mv_3.jpg | original | photo | そのまま | ミーティング風景（ヒーロー候補） |
| 9 | .../home/t-mv_4.jpg | original | photo | そのまま | データ分析風景 |
| 14 | .../home/t_vision_img1.png | original | photo | そのまま | 代表の大判写真（Vision セクション用） |
| 16,19,21,23,25 | .../home/value_img1〜5.png | — | — | **未使用** | Value 説明はテキスト＋CSS アイコンで統一するため使わない（混在回避） |
| 15,18,20,22,24 | .../icon/ico_value1〜5.svg | template | icon | CSS/SVG 代替 | 各バリューは大きな英字イニシャル（S/T/C/S/F）で表現 |
| 26 | .../cloud_img1.png（東北トップクラス！250件以上） | original | text-embedded | 差替 | 数字を HTML テキスト化（#250件以上 や bigstat で表示） |
| 29-37 | .../icon/ill_1〜8.svg | template | icon | CSS/SVG 代替 | サービスカードは Unicode/SVG アイコンで統一 |
| 38 | .../bgimg_about.jpg | original | photo | そのまま | About セクション背景（オフィス全景） |
| 39 | .../txt/txt_abouus.svg | — | text-embedded | 差替 | HTML テキスト化 |
| 45 | .../t_member_img.jpg | original | photo | そのまま | Member セクションの集合写真 |
| 46 | .../t_recruit_img.jpg | original | photo | そのまま | Recruit セクションのミーティング風景 |
| 49 | .../bgimg_contact.jpg | original | photo | そのまま | Contact セクション背景 |
| 50 | .../txt/txt_sns.svg | — | text-embedded | 差替 | HTML テキスト化 |
| 142 | .../member/m_img1.png | original | photo | そのまま | 代表・井上哲寿 顔写真（代表メッセージ用） |
| 10,11 | s.w.org emoji svg | — | icon | 不要 | 削除 |
| Instagram 画像 (uploads/sb-instagram-*) | original? | photo | 不要 | Instagram セクション自体を簡略化（外部リンクボタンのみ）。投稿画像群は取り込まない（投稿個別の文脈を切り離すと意味を失う + 枚数多すぎ） |
| Facebook tracking (connect.facebook.net) | — | icon | 不要 | 削除 |
| ogimage/emoji/wpcf7_captcha 系 | — | — | 不要 | 削除 |

### 引き継ぎ画像リスト（Phase 5-0 でローカル化するもの）

1. `logo.svg`        — ヘッダーロゴ
2. `t-mv_1.jpg`      — ヒーロー: スタッフ集合写真（モバイル/縦配置）
3. `t-mv_2.jpg`      — ヒーロー: 代表面談
4. `t-mv_3.jpg`      — ヒーロー: ミーティング
5. `t-mv_4.jpg`      — ヒーロー: データ分析
6. `t_vision_img1.png` — Vision セクション: 代表
7. `bgimg_about.jpg` — About 背景
8. `t_member_img.jpg` — Member セクション画像
9. `t_recruit_img.jpg` — Recruit セクション画像
10. `bgimg_contact.jpg` — Contact 背景
11. `m_img1.png`      — 代表メッセージ用の顔写真

全てローカル `images/` に保存し、HTML からは相対パスで参照する。Unsplash 差替は不要（十分な original 素材がある）。

## タイポグラフィ方針

- メイン: Noto Sans JP（400/500/700）
- 見出し装飾: Noto Sans JP Bold + 英語見出しに Inter/Noto Sans のオールキャップスを併記する元サイトのスタイルを踏襲
- 業種は士業だが「若さ・IT・クラウド」訴求のため明朝体（Noto Serif JP）は使わない

## レイアウト方針

- ヒーローは左右 2 カラム（デスクトップ）:  左にコピー「世界一のNo.2 を目指すプロフェッショナル会計チーム」＋サブ「若さとITの力で顧客のビジネスを加速させる東北の会計事務所」、右に t-mv_1.jpg + 小画像スタック
- セクション順（上から）:
  1. Header（ロゴ + ナビ + 右端 CTA）
  2. Hero
  3. News（トップ 3 件）
  4. Vision（世界一の No.2）
  5. Our Feature（5 バリュー）
  6. Services（9 項目のグリッド）
  7. About（事務所概要 + オフィス画像）
  8. Member（集合写真 + 代表メッセージ）
  9. Recruit（採用バナー）
  10. Contact（TEL + フォーム誘導 + 背景画像）
  11. Footer（社名・住所・TEL・コピーライト・ナビ）
- モバイル追従 CTA バー（768px 以下）: TEL + 「お問い合わせ」ボタン
