# 分析結果 — L-1894 株式会社 綜合税経センター つくばオフィス

## サイト前提

- **website 指定:** `http://www.zeikei-c.com/about.php`（= グループ会社概要ページ、実質的にはトップ扱い）
- **リード仕様:** 「株式会社 綜合税経センター つくばオフィス」(茨城県つくば市)
- **本店:** 千葉県柏市
- **関係性:** history.php に「2023年 株式会社茨城税経センターは、株式会社綜合税経センターと合併し、株式会社綜合税経センターつくばオフィスとなる」と明記。本店サイト内で access.php に「つくばオフィス」として住所・TEL・FAX・アクセス方法が個別セクションで存在。**DEC-026 該当せず（記述ゼロではない）**、ビルダー続行。
- **つくばオフィス情報（leads.json と access.php で一致）:**
  - 〒300-2658 茨城県つくば市諏訪Ｃ-15街区4　パークハイム102
  - TEL: 029-839-0298 / FAX: 029-839-0299
  - つくばエクスプレス線「万博記念公園駅」より徒歩1分

## デザインスタンス

元サイトは本店（柏）中心のグループ総合サイト。リードのターゲット（つくばオフィス）向けにリデザインする場合、本店サイトのコピー・サービス・ブランド・組織情報は引き継ぎつつ、ヒーロー／連絡先／アクセスを「つくばオフィス」に寄せた構成にする。テキストは原文忠実。創作・要約・言い換えは禁止。

## アーキタイプ

**A: モダンミニマル**
- 根拠: 税理士＋司法書士＋社労士＋行政書士を束ねる総合コンサルファーム。ターゲットは中小企業経営者。信頼・専門性・総合力を視覚化する必要があり、旧テンプレの青ヘッダーを継承しつつ、余白とタイポ整理で 2026 年水準に引き上げる。明朝主体の伝統重厚よりも、グループの「経営コンサルティングファーム」という自己定義に合う。
- サブ要素: 見出しフォントには Noto Serif JP を一部使い、士業らしい堅実感を残す。

## カラーパレット

元サイトの screenshot とロゴ（logo_navy.png）から抽出。ブランド色の紺系を継承。

- **メイン（primary）**: `#13315C`（ロゴのネイビー）
- **サブ（secondary）**: `#2E5A88`（明るめのブルーグレー、元サイトヘッダー系）
- **アクセント（accent）**: `#2FB6C3`（元サイトの cyan 矢印色由来。CTA に集中）
- **ベース（base）**: `#FFFFFF` / `#F5F7FA`
- **テキスト**: `#1A1F36` / `#54627A`

60-30-10 の法則: ベース白 60% / ネイビー帯 30% / cyan 10%。色相は変更しない。

## 画像分類

| # | URL | 出自 | 適性 | 処理 | 備考 |
|---|-----|------|------|------|------|
| logo_navy.png | `sixtyel_images/common/logo_navy.png` | original | text-embedded(ロゴ) | **そのまま** | ヘッダーロゴ。ロゴは text-embedded 例外 |
| president_photo.png | `sixtyel_images/company/president_photo.png` | original | photo | **そのまま** | 代表取締役 栗山隆史の切り抜き。代表挨拶セクションに使用 |
| top_mainimage.jpg | `sixtyel_images/top/top_mainimage.jpg` | stock | photo | **差替（Unsplash）** | ビジネスストック写真。Hero 背景は別の高品質写真に差替 |
| top_mainimage_catch.png | `sixtyel_images/top/top_mainimage_catch.png` | original | text-embedded | 差替 | テキスト焼込を HTML で再現 |
| vision_catch.png | `sixtyel_images/company/vision_catch.png` | original | text-embedded | 差替 | テキスト焼込を HTML で再現 |
| president_name.png | `sixtyel_images/company/president_name.png` | original | text-embedded | 差替 | 「TAKASHI KURIYAMA」を HTML で再現 |
| consultant_*.png（15枚） | `sixtyel_images/consultant/*` | original | photo | **使わない** | 柏本店所属のコンサルタント写真。つくばオフィス向けデモでは載せない |
| sixtyel_images/common/icon_*.png | original | icon | CSS/SVG 代替 | サービスカードのアイコンは SVG で代替 |
| sixtyel_images/common/bar_*.png | template | text-embedded | 不要 | グループ会社ロゴバナー。フッターで会社名テキスト列挙に変更 |
| sdgs_icon*.png（17枚） | template | icon | 不要 | SDGs のカラフル17ゴールアイコン。使わない |
| sixtyel_images/common/tel.png | original | text-embedded | 差替 | 電話番号焼込 → HTML リンク |
| sixtyel_images/top/top_num88.png 他 | original | text-embedded | 差替 | 統計数値焼込 → HTML で再現 |
| sixtyel_images/top/top_recruit_*.png 他 | original | text-embedded | 不要 | 採用セクションは中小 HP デモでは省略 |
| org_20260407.webp | original | diagram | 不要 | 柏本店基準の組織図。つくばオフィス向けに不要 |

### 採用する画像（ローカル化対象）

1. `logo_navy.png` — ヘッダーロゴ
2. `president_photo.png` — 代表挨拶

**合計 2 枚**。それ以外の Hero 背景・サービスアイコン・会社写真は Unsplash or CSS/SVG で代替する。
