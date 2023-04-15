import json
import discord
from discord.ext import commands
import requests

from modules.Quizzes.increase_points import increase_points

description = '''The Best Hamster'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready')

@bot.command()
async def quizTR(ctx):
    response = requests.get("https://opentdb.com/api.php?amount=1")
    json_data = json.loads(response.text)
    if 'results' in json_data and 'question' in json_data['results'][0]:
        question = json_data['results'][0]['question']
        answer = json_data["results"][0]["correct_answer"]
        await ctx.send(question)
        await ctx.send("You have unlimited tries for 15 seconds I'll tell you if you got it right or not.")
    else:
        print("Error: Could not retrieve question")

    async def wait_for_answer():
        def check(m):
            return m.content == answer and m.channel == ctx.channel

        try:
            msg = await bot.wait_for('message', timeout=15.0, check=check)
        except:
            await ctx.send('You took too long. The answer was ' + answer)
            return False
        else:
            await ctx.send('10 Points for you!')
            return True

    result = await wait_for_answer()

    if result:
        increase_points(10, ctx.author.id)

#read the token from the bottoken.json and run the bot
with open('bottoken.json') as f:
    bottoken = json.load(f)
bot.run(bottoken['token'])