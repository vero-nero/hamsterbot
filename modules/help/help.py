import discord
from discord.ext import commands
# gambling command
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)
@bot.command()
async def listcommands(ctx):
    commands = '''Commands with syntax:
    >add [number] [number]
    >sub [number] [number]
    >mult [number] [number]
    >div [number] [number]
    >roll [number]d[number]
    >choose [option] [option] [option] ...
    >randomize [option] [option] [option] ...
    >gaydar [option] [option] [option] ...
    >greet
    >listcommands
    >help
    >ping
    >repeat [message] [number]
    >repeat [message] [number] [number]
    >quote
    '''
    await ctx.send(commands)