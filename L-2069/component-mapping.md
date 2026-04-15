# コンポーネント割当表 — L-2069

## サイト構造
Header / Hero / About / Services / Results / Company / Access / Contact / Footer

## テキストマッピング

| ID | 元テキスト(要約ラベル) | 新コンポーネント | セクション | 処理 |
|----|-----|------|------|------|
| T1 | 税理士法人テルス | ロゴ | Header | そのまま |
| T2 | 会計・税務コンサルタント | サブタイトル | Header | そのまま |
| T3 | 会計・税務の力で地域経済を支える。 | Hero 見出し | Hero | そのまま（分断禁止） |
| T4 | 経営･財務コンサルのガイア･テルスグループ｜福島須賀川 | Hero サブ | Hero | そのまま |
| T5 | 私たちは、お客様とのコミュニケーション…ベストな提案を行います。(2段落) | About 本文 | About | そのまま |
| T6 | 業務案内（6項目リスト: 税務申告書～税務コンサル） | Services カード | Services | そのまま（6カード） |
| T7 | サービス詳細 9項目（月次監査業務～経営改善コンサル） | Services 詳細アコーディオン | Services | そのまま（9アコーディオン） |
| T8 | 実績紹介 A社～O社 15件 | Results カード | Results | そのまま（グリッドカード） |
| T9 | 沿革 4行 | Company 沿革 | Company | そのまま |
| T10 | 代表社員/社員税理士/所属税理士/他スタッフ | Company メンバー | Company | そのまま |
| T11 | アクセス 須賀川/東京/郡山 | Access ブロック | Access | そのまま |
| T12 | TEL 0248-75-2207 | Contact CTA | Contact/Header | tel: リンク |
| T13 | tellus_contact URL | Contact フォームリンク | Contact | 原サイトへリンク |

## 画像マッピング

| # | 元URL / 新処理 | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 1 | /img/common/tellus_logo.png → images/tellus_logo.png | original | text-embedded | — | — | ダウンロード済みだが Header は CSS テキストで表現（汎用性・シャープさ） |
| 2 | /img/page/tellus_top.jpg | original | text-embedded | — | Hero | Unsplash 差替（ビジネス・書類・手） |
| 3 | /img/page/img_tellus.jpg | stock | photo | — | — | 不要 |
| 4 | sukagawaoffice.jpg → images/sukagawaoffice.jpg | original | photo | 須賀川オフィス写真 | Company | **そのまま** 相対パス |
| 5 | tokyooffice2-3.jpg → images/tokyooffice2-3.jpg | original | photo | 東京オフィス写真 | Access | そのまま |
| 6 | koriyamaoffice4.jpg → images/koriyamaoffice4.jpg | original | photo | 郡山オフィス写真 | Access | そのまま |
| - | 業務案内アイコン9種 | — | — | Services カード | Services | SVG 代替 |

## CTA 配置
- Header 右端: TEL + 「お問い合わせ」ボタン
- Hero 下部: 「お問い合わせ」大 CTA
- Mobile 追従バー: TEL + お問い合わせ

## 処理ルール確認
- Hero 背景は Unsplash（ビジネス・書類・会議）
- オフィス写真は「そのまま引き継ぎ」で統一（3枚揃うので混在なし）
- Services カードのアイコンは SVG 統一
