import discord
from discord.ext import commands
import random
description = '''The Best Hamster'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command(description='gaydar')
async def gaydar(ctx, *choices: str):
    """Chooses between multiple options."""
    if "simon" in choices:
        await ctx.send("simon")
    elif random.randint(0, 100) > 70:
        await ctx.send(random.choice(choices))
    else:
        await ctx.send("none of the above")