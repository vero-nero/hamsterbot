import discord
from discord.ext import commands
import random
description = '''The Best Hamster'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command()
async def pinging(ctx, member: discord.Member):
        await ctx.send(f'Pinging {member.mention}...')