# コンポーネント割当表

## サイト構造

1. Header（ロゴ＝事務所名・ナビ・TEL）
2. Hero（事務所名 + リード文 + CTA）
3. About（所長紹介＋所長写真＋事務所概要）
4. Services（業務案内：会計業務 + 監査証明 + その他業務）
5. Software（推奨会計ソフト紹介）
6. Pricing（料金表 — HTML テーブルで原文再現）
7. Audit（労働者派遣業の許可申請に係る監査証明）
8. Columns（経理の窓・税務の壷 — 抜粋3件）
9. Access（所在地 + マップ画像 + 連絡先）
10. Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 橋本会計事務所（福島県　郡山市）・公認会計士　税理士　橋本寿 | サイトロゴ | Header | そのまま |
| T2 | 〒963-8002 郡山市駅前1-4-4 / 024-934-3720 | ヘッダー連絡先 | Header | そのまま |
| T3 | こちらは 橋本会計事務所（福島県 郡山市）・公認会計士 税理士 橋本寿 で御座います よく、おいで下さいました | Hero 見出し＋リード | Hero | そのまま（一行で原文連結。AI 創作禁止） |
| T4 | 公認会計士・税理士 橋本 寿 / 昭和33年郡山市生まれ / 昭和61年3月公認会計士登録 | プロフィール | About | そのまま |
| T5 | 私どもの業務内容です / 税理士・公認会計士業務です | About 補足 | About | そのまま |
| T6 | 会計業務（現金出納帳のみ作成のお客様） + 自計化が困難なお客様の場合... | サービスカード1 | Services | そのまま |
| T7 | 会計業務（自計化できるお客様） + フリーやマネーフォワード... | サービスカード2 | Services | そのまま |
| T8 | その他の業務（労働者派遣業の許可申請、学校法人/労働組合監査、社会福祉法人、公益法人、診療所/病院、相続税申告） | サービスカード3 | Services | そのまま（リスト化） |
| T9 | ご訪問及びクラウド上での操作（クラウド/訪問/遠方） | サービスカード4 | Services | そのまま |
| T10 | 推奨ソフト：弥生会計 / フリーfreee / マネーフォワードMF / 勘定奉行 / PCA会計 + 各説明文 | ソフトカードグリッド | Software | そのまま |
| T11 | 臨時サポート業務 + 1時間内10,000円 / 20,000円 | Software サポート補足 | Software | そのまま |
| T12 | 当事務所の料金表 (R04.08.26) お客様の状況によって異なる場合があります… | Pricing 見出し＋注記 | Pricing | そのまま |
| T13 | 法人 / 個人の料金表 + 注記（freee/マネフォの自計化要件） | Pricing 表 | Pricing | **画像→HTMLテーブル化（原文の数字を一字一句保持）** |
| T14 | 年末調整・償却資産・税務調査立会の追加料金 | Pricing 追加表 | Pricing | **画像→HTMLテーブル化** |
| T15 | 労働者派遣事業の許可申請に係る監査証明等を行います + 流れ + 費用 + 財産的基礎要件 | Audit セクション | Audit | そのまま（要点抜粋＋詳細をアコーディオン） |
| T16 | 経理の窓・税務の壷（自己責任 / 家業を営む上で経理の役割 / 法人の統治機構比較 などコラム抜粋） | コラム3カード | Columns | カード化（タイトル＋導入数行＋「続きを読む」省略） |
| T17 | 事務所　〒963-8002 郡山市駅前１ー４ー４ / 電話 024-934-3720 / s33hashi@alles.or.jp | Access 連絡先 | Access | そのまま |
| T18 | 以前、橋本折箱店があった場所で、夢一膳の北側隣です | Access 補足 | Access | そのまま |
| T19 | link free 但し、リンク以外の利用・転載を禁じます All-rights reserved | Footer 著作権 | Footer | そのまま |

**漏れチェック**: 全テキストブロックの行き先が割り当て済み。

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | hisashi220830-30.jpg | original | photo | プロフィール写真 | About | **そのまま**（images/hashimoto-cpa.jpg） |
| 2 | mapimg.gif | original | diagram | アクセスマップ | Access | **そのまま**（images/mapimg.gif） |
| 3 | price.jpg | original | text-embedded | — | Pricing | **HTMLテーブル化**（画像参照しない） |
| 4 | price2.jpg | original | text-embedded | — | Pricing | **HTMLテーブル化**（画像参照しない） |
| 5 | gava.jpg | original | text-embedded | — | （Columns 内コラム参考） | **HTMLテーブル化** または非表示 |
| 6 | yayoi.jpg / freee.png / mfc.jpg / obc.jpg / pcac.jpg | template/ベンダー | text-embedded | — | Software | **CSS テキスト代替**（ベンダーロゴは商標問題あり、テキスト＋カラーバーで代替） |
| 7 | maru.gif | template | icon | リスト装飾 | Services 等 | **CSS 代替**（::before の丸） |
| 8 | dango.gif / fmgig_banner.gif / logo_nomap.gif / valuecommerce / a8.net / imgvc 等 | external/template | icon/text-embedded | — | — | **不要**（外部広告） |
| 9 | eki.gif | original? | photo | — | — | **不要**（画質低・古い駅前風景） |
| 10 | kobito_c.gif / kobito_d.gif | template | icon | — | — | **不要**（汎用キャラ） |
| 11 | f-counter.net (×2) | external | icon | — | — | **不要**（カウンター） |
| 12 | Hero 背景画像 | — | — | Hero 背景 | Hero | **Unsplash 差替**（office / desk / business 系） |

### 統一性チェック
- Services のサービスカード（4枚）→ 全て CSS アイコン（SVG）で統一。混在しない。
- Software のソフトカード（5枚）→ 全て CSS テキスト＋カラー代替で統一。混在しない。
- Columns（3枚）→ 全て CSS 装飾のみ、画像なしで統一。

### ローカル化リスト
1. `https://userweb.alles.or.jp/s33hashi/hisashi220830-30.jpg` → `images/hashimoto-cpa.jpg`
2. `https://userweb.alles.or.jp/s33hashi/mapimg.gif` → `images/mapimg.gif`

以上 2 ファイルのみダウンロード。Hero 背景画像は Unsplash URL 直接参照。
