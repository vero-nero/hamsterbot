#!/usr/bin/env python3
import json
import discord
from discord.ext import commands
import random
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

#@bot.event
#async def on_ready():
#    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
#    print('------')

@bot.event
async def on_member_joined(ctx, member = discord.Member):
    """Says when a member joined."""
    #sus⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
    amongsus ='''   
        ⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀ ⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀  
        ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ Welcome''' + f'{member.mention}'+ ''' ⠀⠀ 
        ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀ ⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ 
        ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ 
        ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ 
        ⠀⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀ ⠀⠀ 
        ⠀⠀⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⣿'''
    await ctx.send(amongsus)

@bot.command()
async def greet(ctx):
    """says hello."""
    await ctx.send("Hello!")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def sub(ctx, left: int, right: int):
    """subs two numbers together."""
    await ctx.send(left - right)
@bot.command()
async def mult(ctx, left: int, right: int):
    """mults two numbers together."""
    await ctx.send(left * right)
@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    if left == 0 or right == 0:
        await ctx.send("Hurenshohn")
    else:
        await ctx.send(left / right)


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

@bot.command(description='gaydar')
async def gaydar(ctx, *choices: str):
    """Chooses between multiple options."""
    #check if "r6" is in the list
    if "simon" in choices:
        await ctx.send("simon")
    elif random.randint(0, 100) > 70:
        await ctx.send(random.choice(choices))
    else:
        await ctx.send("none of the above")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    if times > 10:
        await ctx.send('Too many times!')
        return
    for i in range(times):
        await ctx.send(content)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='racism')
async def isracism(ctx):
    """Is racism cool?"""
    await ctx.send('Yes, racism is cool.')

@bot.command()
async def pinging(ctx, member: discord.Member):
        await ctx.send(f'Pinging {member.mention}...')

#read the token from the bottoken.json and run the bot
with open('bottoken.json') as f:
    bottoken = json.load(f)
bot.run(bottoken['token'])