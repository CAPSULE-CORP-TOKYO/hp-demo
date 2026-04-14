# コンポーネント割当表

## サイト構造
- Header / Hero / About / Services / ServiceDetail(accordion) / Staff / CompanyInfo / Contact / Footer

## テキストマッピング

| ID | 元テキスト | 新コンポーネント | セクション | 処理 |
|----|-----------|----------------|-----------|------|
| T1 | 藍税理士法人 | ヘッダーロゴ | Header | そのまま |
| T2 | 深絞りのサービスを！！ | ヒーロー見出し | Hero | そのまま |
| T3 | 営業時間 平日 午前9時～午後5時 (土日祝 定休) | ヘッダー情報バー | Header | そのまま |
| T4 | 029-227-3916 | ヘッダー電話 + CTA | Header/Contact | そのまま |
| T5 | 平成28年6月1日に、税理士横山会計事務所、田崎昇税理士事務所はお互いの豊富な経験を融合し顧客の皆様に〝深絞り″のサービスが提供できるよう藍税理士法人へと法人組織化させて戴きました。 | About本文 | About | そのまま |
| T6 | 社員、職員、質の高いサービスを目指し、一層の努力をする所存でございますので、何卒旧に倍するご愛顧を賜りますようお願い申し上げます。 | About本文 | About | そのまま |
| T7 | 代表社員税理士 横山 哲郎 | About代表名 | About | そのまま |
| T8 | 社員税理士 田崎　昇 | About社員名 | About | そのまま |
| T9 | 中小企業の支援（法人税申告等） | サービスカード1 | Services | カード化 |
| T10 | 適正申告！経営に専念 サクセスストーリーのお手伝い | サービスカード1サブ | Services | そのまま |
| T11 | 相続税の申告・代理 | サービスカード2 | Services | カード化 |
| T12 | 一生の税の精算は相続税‼ 経験豊富、懇切丁寧 | サービスカード2サブ | Services | そのまま |
| T13 | 医療経営と税務 | サービスカード3 | Services | カード化 |
| T14 | 公益法人会計と税務 | サービスカード4 | Services | カード化 |
| T15 | 事業承継と税務 | サービスカード5 | Services | カード化 |
| T16 | プロの二人が知恵を絞る‼ | サービスカード5サブ | Services | そのまま |
| T17 | 中小企業支援詳細テキスト(tyu-syo.html全文) | アコーディオン | ServiceDetail | アコーディオン |
| T18 | 相続税詳細テキスト(so-zoku2.html全文) | アコーディオン | ServiceDetail | アコーディオン |
| T19 | 医療経営詳細テキスト(iryo.html全文) | アコーディオン | ServiceDetail | アコーディオン |
| T20 | 公益法人詳細テキスト(ko-eki.html全文) | アコーディオン | ServiceDetail | アコーディオン |
| T21 | 事業承継詳細テキスト(saiban2.html全文) | アコーディオン | ServiceDetail | アコーディオン |
| T22 | スタッフ紹介全文(recruit.html) | スタッフ一覧 | Staff | カード化 |
| T23 | 法人案内テキスト(company.html: 所在地/設立/取扱ソフト/営業時間等) | 法人概要テーブル | CompanyInfo | そのまま |
| T24 | 連絡先情報(contact.html: 所在地/電話/FAX/MAIL) | コンタクトセクション | Contact | そのまま |
| T25 | プライバシーポリシー全文 | フッターリンク(別ページ扱い) | Footer | 別ページ |
| T26 | Copyright(C) 2016 Ai Tax corporation All Rights Reserved. | フッターコピーライト | Footer | そのまま |
| T27 | 職員旅行テキスト(北海道/箱根/寸又峡) | 法人案内内ギャラリー | CompanyInfo | カード化 |
| T28 | 2016/6/01 藍税理士法人を立ち上げました。今後ともよろしくお願いいたします。 | お知らせ | About | そのまま |

## 画像マッピング

| # | 元URL | 出自 | 適性 | 新コンポーネント | セクション | 処理 |
|---|-------|------|------|----------------|-----------|------|
| 30 | yokoyama.JPG | original | photo | 代表写真 | About | そのまま |
| 31 | tasaki2.JPG | original | photo | 社員写真 | About | そのまま |
| 58 | DSC00482.JPG | original | photo | スタッフ集合写真 | Staff | そのまま |
| 61 | jimusho.JPG | original | photo | 事務所外観 | CompanyInfo | そのまま |
| 62 | kanban.JPG | original | photo | 看板写真 | CompanyInfo | そのまま |
| 41 | annai.PNG | original | diagram | アクセスマップ | Contact | そのまま |
| 65 | souzoku.PNG | original | diagram | 相続税スケジュール図 | ServiceDetail | そのまま |
| - | Unsplash(税務/ビジネス) | - | - | ヒーロー背景 | Hero | Unsplash差替 |

注: 業務案内ページの個別イメージ写真(tyushou.JPG, so-zoku.JPG, iryou.JPG, koeki.JPG, image.jpg)は汎用的なストック風画像が多く、サービスカードでは統一性のためCSS/SVGアイコンで代替する。旅行写真(syugo.JPG, IMG_2778.JPG, m12.JPG等)は法人案内ページのギャラリーとして一部使用するが、トップページの主要セクションには使用しない。
