# QQ Hello Bot

基于 NoneBot2 和 OneBot V11 的 QQ 机器人。指定 QQ 号发消息时，机器人回复 `hello` 加上消息前两个字符。

## 本地运行

1. 安装依赖：`pip install -r requirements.txt`
2. 复制 `.env.example` 为 `.env`，设置 `TARGET_QQ` 和 `ONEBOT_ACCESS_TOKEN`。
3. 启动：`python bot.py`

## Render Web Service

Render 会使用 `Procfile` 启动服务，并自动注入 `PORT`。在 Render 的环境变量中设置：

- `DRIVER=~fastapi`
- `TARGET_QQ=要响应的 QQ 号`
- `ONEBOT_ACCESS_TOKEN=与 OneBot 协议端一致的令牌`

将协议端的 Webhook 地址设置为：

```text
https://你的服务名.onrender.com/onebot/v11/webhook
```
