import asyncio
import logging
import os
from datetime import datetime

class Bot(commands.AutoShardedBot):

    @staticmethod
    def prefix_from(bot, msg):
        # must be an instance of this bot pls dont use anything else
        if not msg.guild:
            return bot.bot_settings.prefix
        return bot.prefix_map.get(msg.guild.id, bot.bot_settings.prefix)

    def __init__(self, bot_settings, **kwargs):
        super().__init__(Bot.prefix_from, **kwargs)
        self.logger = logging.getLogger("bot")
        self.start_time = datetime.now()
        self.bot_settings = bot_settings
        self.prefix_map = {}
        self.mpm = None
        self.ready = False
        
        """Start here"""
