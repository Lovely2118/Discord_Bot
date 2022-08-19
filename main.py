import discord
import json
from discord.ext import commands

# file = open('config.json', 'r')
# config = json.load(file)
intents = discord.Intents().all()

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def taked(ctx):
    await ctx.send(f'{ctx.author.mention}take!')

bot.run('MTAxMDIxOTIxMDk5MzA2MTkxOA.GVuN_Y.P14jnCJSe129l3xs5uUKjRhaKv4B-uCYhcqhbc')
