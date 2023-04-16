import json
import discord
from discord.ext import commands
import requests
from modules.quizes.increase_points import increase_points
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)

async def check(m, ctx, answer):
    return m.author == ctx.author and m.content.lower() == answer.lower() and m.channel == ctx.channel

async def wait_for_answer(ctx, answer):
    try:
        msg = await bot.wait_for('message', timeout=25.0, check=lambda m: check(m, ctx, answer))
    except:
        await ctx.send(f"Time's up! The correct answer was '{answer}'.")
        return False
    else:
        await ctx.send(f'Congratulations {msg.author.mention}, you got it right! 10 points for you.')
        return True

@bot.command()
async def quizTR(ctx):
    response = requests.get("https://opentdb.com/api.php?amount=1")
    json_data = json.loads(response.text)

    if json_data['results'][0]['type'] == 'boolean':
        question = json_data['results'][0]['question']
        answer = json_data['results'][0]['correct_answer']
        await ctx.send(question)
    elif json_data['results'][0]['type'] == 'multiple':
        question = json_data['results'][0]['question']
        answer = json_data['results'][0]['correct_answer']
        possible_answers = json_data['results'][0]['incorrect_answers'] + [answer]
        random.shuffle(possible_answers)
        await ctx.send(question)
        await ctx.send('Choose one of the following answers:')
        for i in range(len(possible_answers)):
            await ctx.send(f'{i+1}. {possible_answers[i]}')

    result = await wait_for_answer(ctx, answer)
    if result:
        await increase_points(10, str(ctx.author.id))