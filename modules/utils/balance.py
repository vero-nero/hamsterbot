import discord
from discord.ext import commands
import json
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)
#get the balance of the account out of the modules\gambling\gambling.json
def getBalance(user):
    with open('modules\gambling\gambling.json') as f:
        gamblingJson = json.load(f)
        return gamblingJson["users"][str(user.id)]["balance"]
# Compare this snippet from modules\utils\balance.py:

@bot.command()
async def balance(ctx):
     # get the balance of the user
     balance = getBalance(ctx.author)
     # send the balance to the user
     await ctx.send(f"Your balance is {balance}!")
