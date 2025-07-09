# 🎮 Splatoon Random Weapon Bot

スプラトゥーン3向けの Discord Bot です。  
ブキ分類の表示や、チーム編成の自動生成をスラッシュコマンドで提供します。

このリポジトリは、**Koyeb上で常時稼働するクラウドBot**として構成されています。

---

## 📁 プロジェクト構成

```

splatoon-bot/
├── app/
│   ├── bot.py                  # Bot本体（スラッシュコマンド対応）
│   ├── requirements.txt        # 必要なPythonパッケージ一覧
│   ├── weapon\_to\_groups.json   # ブキとロール・タイプの定義ファイル
│   ├── team\_patterns.json      # チーム編成のパターン定義ファイル
│   └── .env.example            # トークン定義テンプレート（Gitには含めない）
├── .gitignore                  # .envやvenvなど除外対象
├── Dockerfile                  # Koyebでのビルド用Dockerファイル

````

---

## ✅ 機能コマンド一覧

### `/splatoon_team [pattern]`
- 指定したパターンに基づいてチームごとにブキを編成します
- パターンを省略すると `default` が使用されます
- 入力補完に対応

### `/splatoon_weapon <ブキ名>`
- ブキのロールとタイプを表示
- 入力補完あり

### `/splatoon_role <ロール名>`
- 指定ロールに該当するブキ一覧を表示
- 入力補完あり

### `/splatoon_help`
- 上記すべての使い方を表示

---

## ☁️ Koyeb でのデプロイ手順（GitHubブラウザ操作のみ）

### 1. GitHubにアップロード（コマンド不要）

1. [GitHub](https://github.com) で新規リポジトリを作成（例：`splatoon-bot`）
2. `.env` を除いたすべてのファイルをブラウザからアップロード
3. `.env.example` はトークンのテンプレとして含めること

### 2. Koyebにログイン・連携

1. [https://www.koyeb.com/](https://www.koyeb.com/) にアクセス
2. GitHubと連携してアプリを作成

### 3. アプリ設定

| 設定項目            | 設定内容                      |
|---------------------|-------------------------------|
| Builder             | Dockerfile                    |
| プラン              | Free + CPU Eco（無料枠）     |
| Environment Variable| `DISCORD_TOKEN=xxx` を追加   |

> `.env` ファイルはGitHubに含めず、**Koyebの環境変数セクション**で手動設定します。

### 4. デプロイ完了後

- URL（例：`https://splatoon-bot-xxxx.koyeb.app`）が表示される
- Discord Botがオンラインになる

---

## 🔁 常時稼働のための設定（UptimeRobot）

Koyebの無料プランではBotが一定時間でスリープします。  
[UptimeRobot](https://uptimerobot.com/) を使って、BotのURLに5分おきにアクセスすることで常時起動を維持できます。

---

## 🧩 カスタマイズ方法

### ブキ情報の追加・修正

`app/weapon_to_groups.json` にて編集可能：

```json
{
  "スプラシューター": [
    "role:前衛キル特化ブキ",
    "type:シューター"
  ]
}
````

### チーム編成パターンの追加

`app/team_patterns.json` にて自由に定義可能：

```json
{
  "default": [
    "role:前衛キル特化ブキ",
    "role:前衛キル特化ブキ",
    "role:オールラウンダーブキ",
    "role:後衛ブキ"
  ]
}
```

---

## 👤 開発者情報

* Author: ichiken
* Language: Python + discord.py
* Hosting: [Koyeb.com](https://www.koyeb.com/)

---

## 🔐 セキュリティ・補足事項

* `.env` は**GitHubにpushしないように注意**（`.gitignore`に設定済）
* トークンは `.env.example` を参考に、**KoyebのWeb UIで直接登録**

---

## 🎉 使用上の注意

* コマンドはすべて `/splatoon_` 接頭辞で統一
* ご自身のサーバーにBotを招待して使用してください
* トークン管理は自己責任でお願いします

```