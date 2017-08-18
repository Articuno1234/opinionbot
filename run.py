import discord
from discord.ext.commands import Bot
from discord.ext.commands import cooldown
import logging
import sys
import os
import config
import time
import asyncio
import random

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix

@bot.event
async def on_ready():
    print("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))
@bot.command(pass_context=True)
async def opinion(ctx, game, *, rating):
    """What is your opinion of a game?
       !opinion game rating"""
    author = ctx.message.author
    channel = bot.get_channel("348089529707790336")
    em = discord.Embed(color=0x000000)
    em.set_author(name='Opinion')
    em.add_field(name='Opinion by', value=("{} or {}".format(author.mention, author)))
    em.add_field(name='Game', value=(game))
    em.add_field(name='Rating', value=(rating))
    await bot.send_message(channel, embed=em)
    await bot.say("Your Opinion was sent! :thumbsup: ")

@bot.command(name="8ball", pass_context=True)
async def ball(ctx):
    """What is the chance?
       !8ball"""
    aw = ["It will happen", "50/50 Chance", "No it wont happen"]
    await bot.say(random.choice(aw))
bot.run(config.TOKEN)
