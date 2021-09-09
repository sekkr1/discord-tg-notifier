import discord
import requests
from os import environ
from datetime import datetime, timedelta

TG_API_URL = f"https://api.telegram.org/bot{environ['TG_TOKEN']}/"


class DiscordTelegramNotifierClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_update = datetime.fromtimestamp(0)
        self.notify_message_id = None

    def clear_notification(self):
        if self.notify_message_id is None:
            return
        requests.post(
            TG_API_URL + "deleteMessage",
            data={
                "chat_id": environ["TG_CHAT_ID"],
                "message_id": self.notify_message_id,
            },
        )
        self.notify_message_id = None

    def notify(self):
        if self.notify_message_id is not None:
            return
        self.notify_message_id = requests.post(
            TG_API_URL + "sendMessage",
            data={"chat_id": environ["TG_CHAT_ID"], "text": environ["TG_MESSAGE"]},
        ).json()["result"]["message_id"]
        self.last_update = datetime.now()

    async def on_message(self, message: discord.Message):
        if not isinstance(message.channel, discord.DMChannel):
            return
        if self.user == message.author:
            self.last_update = datetime.now()
            self.clear_notification()
            return
        if datetime.now() - self.last_update < timedelta(
            seconds=int(environ["COOLDOWN_SECONDS"])
        ):
            return
        self.notify()


client = DiscordTelegramNotifierClient()
client.run(
    environ["DISCORD_TOKEN"],
    bot=False,
)
