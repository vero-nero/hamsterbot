import json
import discord
from discord.ext import commands
import requests
from modules.quizes.increase_points import increase_points

description = '''The Best Hamster'''
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.command()
async def quizTof(ctx):
    response = requests.get("https://officeapi.dev/api/quotes/random")
    json_data = json.loads(response.text)
    if 'data' in json_data and 'content' in json_data['data']:
        quote = json_data['data']['content']
        character = json_data['data']['character']['firstname'] + " " + json_data['data']['character']['lastname']
        await ctx.send(quote)
        await ctx.send("Who said this? You have unlimited tries for 10 seconds. I'll tell you if you got it right or not.")
    else:
        print("Error: Could not retrieve quote")

    async def wait_for_answer():
        def check(m):
            return m.content == character and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=10.0, check=check)
        except:
            await ctx.send(f'You took too long. The answer was {character}')
            return False
        else:
            await ctx.send(f'You got it, {msg.author.mention}!')
            return True    

    result = await wait_for_answer()

    if result:
        increase_points(10, ctx.author.id)