import asyncio
import logging

import discord
import inspirobot
import requests
from discord.ext import tasks
from redbot.core import commands

log = logging.getLogger("red.cbd-cogs.tube")

class PTZ(commands.Cog):
	"""My custom cog"""

    def __init__(self, bot):
        self.bot = bot
	
	@commands.command()
	async def lookUp():
		requests.get('http://10.10.0.19:8888/press/bank/1/3')