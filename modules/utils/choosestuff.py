import discord
from discord.ext import commands
import random
description = '''The Best Hamster'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(description='For when you wanna settle the score some other way')
async def randomize(ctx, *choices: str):
    """Chooses between multiple choices."""
    #check if "r6" is in the list
    if "r6" in choices:
        await ctx.send("r6")
    else:
        await ctx.send(random.choice(choices))