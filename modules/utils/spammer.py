import discord
from discord.ext import commands
import random
description = '''The Best Hamster'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 10:
        await ctx.send('Too many times!')
        return
    for i in range(times):
        await ctx.send(content)