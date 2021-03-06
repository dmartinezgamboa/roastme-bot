import os

import discord

from roast import roast_tagged_user

TOKEN = os.environ['DISCORD_ROASTME_TOKEN']


class RoastMeClient(discord.Client):
    def __init__(self, roasts_parts, roasts_full):
        self._roasts_parts = roasts_parts
        self._roasts_full = roasts_full
        super().__init__()

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user in message.mentions:
            user = self.find_tagged_user(message.author, message.mentions)
            roast = roast_tagged_user(
                user_id=user.id, 
                roasts_pieces=self.roasts_parts, 
                roasts_full=self.roasts_full
                )
            await message.channel.send(roast)

    def find_tagged_user(self, message_author, mentions):
        if len(mentions) == 1:
            return message_author
        for user in mentions:
            if user != self.user:
                return user

    @property
    def roasts_parts(self):
        return self._roasts_parts

    @property
    def roasts_full(self):
        return self._roasts_full
