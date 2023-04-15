import discord
from discord.ext import commands
# gambling command
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def sub(ctx, left: int, right: int):
    """subtract two numbers ."""
    await ctx.send(left - right)
@bot.command()
async def mul(ctx, left: int, right: int):
    """multiplies two numbers together."""
    await ctx.send(left * right)
@bot.command()
async def div(ctx, left: int, right: int):
    """divides two numbers together."""
    if left == 0 or right == 0:
        await ctx.send("Hurenshohn")
    else:
        await ctx.send(left / right)