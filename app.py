#!/usr/bin/env python3
import asyncio
import json
import discord
from discord.ext import commands
import random
import requests
description = '''The Best Hamster'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_member_join(member):
    """Says when a member joined."""
    amongsus ='''   
        ⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀ ⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀  
        ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ Welcome''' + f'{discord.Member}'+ ''' ⠀⠀ 
        ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀ ⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ 
        ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ 
        ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ 
        ⠀⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀ 
        ⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀ ⠀⠀ 
        ⠀⠀⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿'''
    with open('serverID.json') as f:
        serverJson = json.load(f)
        serverID = serverJson['id']
    print(serverID)
    channel = await bot.fetch_channel(serverID) 
    print(channel)
    await channel.send(amongsus)

@bot.command()
async def greet(ctx):
    """says hello."""
    await ctx.send("Hello!")

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

@bot.command()
async def quizzMe(ctx):
    response = requests.get("https://officeapi.dev/api/quotes/random")
    json_data = json.loads(response.text)
    if 'data' in json_data and 'content' in json_data['data']:
        quote = json_data['data']['content']
        character = json_data['data']['character']['firstname'] + " " + json_data['data']['character']['lastname']
        await ctx.send(quote)
        await ctx.send("Who said this? You have unlimited tries for 10 seconds ill")
    else:
        print("Error: Could not retrieve quote")
#wait for the next message and compare it to character
    def check(m):
        return m.content == character and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', timeout=10.0, check=check)
        #catch any exceptions
    except:
        await ctx.send('You took too long.')
    else:
        await ctx.send('You got it!')
@bot.command()
#gambling command
async def gamble(ctx, amount: int):
    #check if the user has enough money
    if amount > money[ctx.author.id]:
        await ctx.send("You don't have enough money")
    else:
        #check if the user wins
        if random.randint(0, 100) > 50:
            money[ctx.author.id] += amount
            await ctx.send("You won!")
        else:
            money[ctx.author.id] -= amount
            await ctx.send("You lost!")

#read the token from the bottoken.json and run the bot
with open('bottoken.json') as f:
    bottoken = json.load(f)
bot.run(bottoken['token'])