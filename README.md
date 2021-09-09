# Discord Telegram Notifier

Notifies you on incoming Discord messages using Telegram.

Useful in case you don't have Google Push services on your phone.

## Docker

```bash
$ docker run --name discord-notifier --restart unless-stopped -d -e DISCORD_TOKEN=<DISCORD TOKEN HERE - steal from browsers authorization header> -e TG_TOKEN=<TG BOT TOKEN HERE> -e TG_CHAT_ID=<TG CHAT ID HERE> -e TG_MESSAGE="Check your Discord :)" -e COOLDOWN_SECONDS=10 sekkr1/discord-tg-notifier
```
