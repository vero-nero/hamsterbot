#!/usr/bin/env python3
import json
import discord
from discord.ext import commands
from modules.Quizzes.general import quizTR
from modules.Quizzes.theoffice import quizTof
from modules.gambling.gambling import gamble
from modules.greets.greets import greet
from modules.greets.newmember import on_member_join
from modules.help.help import listcommands
from modules.calculator.calculator import add, sub, mul, div
from modules.memes.gaydar import gaydar
from modules.memes.racism import cool
from modules.utils.choosestuff import choose, randomize, roll
from modules.utils.pinging import pinging
from modules.utils.spammer import repeat
description = '''The Best Hamster'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready')

bot.add_command(gamble)
bot.add_command(listcommands)
bot.add_command(quizTof)
bot.add_command(quizTR)
bot.add_command(add)
bot.add_command(sub)
bot.add_command(mul)
bot.add_command(div)
bot.add_listener(on_member_join)
bot.add_command(gaydar)
bot.add_command(cool)
bot.add_command(pinging)
bot.add_command(greet)
bot.add_command(roll)
bot.add_command(choose)
bot.add_command(randomize)
bot.add_command(repeat)

#read the token from the bottoken.json and run the bot
with open('bottoken.json') as f:
    bottoken = json.load(f)
bot.run(bottoken['token'])