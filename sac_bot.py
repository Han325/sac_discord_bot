import discord

from settings import TOKEN
from day_03.ex_02 import parse_price
from day_03.ex_03 import parse_price_dynamic
from day_03.ex_04 import get_weather
from day_03.bonus import gen_joke

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("The secret TOKEN is correct!")
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.reply('Hello!', mention_author=True)

  if message.content.startswith('$greet'):
    await message.reply('Hello, {0.author}!'.format(message),
                        mention_author=True)

  if message.content.startswith('$echo '):
    await message.reply(message.content[1:], mention_author=True)

  if message.content.startswith('$s&p'):
    price = parse_price()
    await message.reply(price)

  if message.content.startswith('$stock '):
    price = parse_price_dynamic(message.content[7:])
    await message.reply(price)

  if message.content.startswith('$weather'):
    weather = get_weather()
    await message.reply(weather)

  if message.content.startswith('$joke'):
    joke = gen_joke()
    await message.reply(joke)


client.run(TOKEN)
