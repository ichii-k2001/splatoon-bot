# Splatoon Discord Bot (Koyeb Deployment)

## 🎯 概要

- Python製のDiscord BotをGitHubにアップロード
- Koyebにデプロイして24時間稼働
- `.env` はGitHubに含めず、Koyeb Web UIで管理

---

## 📁 プロジェクト構成

```
splatoon-bot/
├── app/
│   └── bot.py               # Discord Bot ロジック
├── server.py                # FastAPI + Bot起動エントリーポイント
├── requirements.txt         # ライブラリ定義
├── Dockerfile               # デプロイ用設定
├── weapon_to_groups.json    # ブキデータ（中身要編集）
├── team_patterns.json       # 編成パターン（中身要編集）
├── .env                     # ローカル用（Gitには含めない）
├── .env.example             # 共有用テンプレ
└── .gitignore               # 除外ファイル指定
```

---

## ✅ ローカル開発手順

1. `.env` ファイル作成

```
DISCORD_TOKEN=your_discord_token
```

2. 仮想環境を使って依存をインストール

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. サーバー起動

```bash
uvicorn server:app --host 0.0.0.0 --port 8080
```

4. 動作確認

- http://localhost:8080/ にアクセス → `{"message": "Bot is running!"}`
- Discordで `/splatoon_help` などのスラッシュコマンドが動作

---

## ✅ GitHubへのアップロード

1. `.env` は `.gitignore` によって除外
2. `.env.example`, `requirements.txt`, `Dockerfile` 等を含めてアップロード

---

## ✅ Koyebへのデプロイ

1. GitHub連携でリポジトリを選択
2. Dockerfile により自動ビルド
3. 環境変数 `DISCORD_TOKEN` を設定
4. ビルド成功後、公開URLが発行される（例：`https://splatoon-bot-xxxx.koyeb.app`）

---

## ✅ UptimeRobotで常時稼働

1. https://uptimerobot.com に登録
2. 「Add New Monitor」で Koyeb URL を5分間隔で監視

---

## ✅ JSONファイル例

### weapon_to_groups.json

```json
{
  "スプラシューター": ["role:汎用", "type:シューター"],
  "ローラー": ["role:前衛", "type:ローラー"],
  "チャージャー": ["role:後衛", "type:チャージャー"]
}
```

### team_patterns.json

```json
{
  "default": ["role:前衛", "role:後衛", "role:汎用", "role:汎用"]
}
```

---

## ✅ 利用可能なコマンド

- `/splatoon_help`
- `/splatoon_team [pattern]`
- `/splatoon_weapon <武器名>`
- `/splatoon_role <ロール名>`
- `/splatoon_pattern [パターン名]`

---

## ✅ トラブルシュート

| 症状 | 対策 |
|------|------|
| `KeyError: DISCORD_TOKEN` | Koyebで環境変数が未設定 |
| Botがスリープする | UptimeRobotで監視追加 |
| コマンドが補完されない | `/splatoon_help` で確認、同期に時間がかかることも |

---

## 🧩 補足

- FastAPIを使っているため、将来的に `/metrics` や `/status` などのAPIも追加しやすい構成です。
