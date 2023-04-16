import json
import random
import json
import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)
# gambling command
@bot.command()
async def gamble(ctx, amount: int):
    # check in the gambling.json if the user has ever gambled before
    with open('modules\gambling\gambling.json') as f:
        gamblingJson = json.load(f)
        if str(ctx.author.id) in gamblingJson["users"]:
            # if the user has gambled before check if they have enough money
            if gamblingJson["users"][str(ctx.author.id)]["balance"] >= amount:
                # if they have enough money check if they win
                if random.randint(0, 100) > 50:
                    # if they win add the amount to their balance
                    gamblingJson["users"][str(ctx.author.id)]["balance"] += amount
                    with open('modules\gambling\gambling.json', 'w') as outfile:
                        json.dump(gamblingJson, outfile)
                    await ctx.send(f"You won {amount}!")
                else:
                    # if they lose remove the amount from their balance
                    gamblingJson["users"][str(ctx.author.id)]["balance"] -= amount
                    with open('modules\gambling\gambling.json', 'w') as outfile:
                        json.dump(gamblingJson, outfile)
                    await ctx.send(f"You lost {amount}!")
            else:
                # if they don't have enough money tell them
                await ctx.send(f"You don't have enough money!")
        else:
            # if the user hasn't gambled before add them to the json with a balance of 100
            gamblingJson["users"][str(ctx.author.id)] = {"balance": 100}
            with open('modules\gambling\gambling.json', 'w') as outfile:
                json.dump(gamblingJson, outfile)
            await ctx.send(f"Welcome, your balance is at 100!")