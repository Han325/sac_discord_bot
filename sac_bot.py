import discord

from settings import TOKEN
from discord.ext import commands

#day 3 exercises
from day_03.ex_02 import parse_price
from day_03.ex_03 import parse_price_dynamic
from day_03.ex_04 import get_weather
from day_03.bonus import gen_joke

#day 4 exercises
from day_04.ex_01 import get_quote
from day_04.ex_02 import get_crypto_price
from day_04.ex_03 import get_crypto_price_dynamic
from day_04.ex_04 import get_random_malaysia_news
from day_04.ex_05 import get_random_global_news

#day 5 exercises
from day_05.ex_01 import write_to_csv
from day_05.ex_02 import read_from_csv
from day_05.ex_03 import analyze
from day_05.ex_04 import show_restaurants, vote

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

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.reply(quote)

  if message.content.startswith('$bitcoin'):
    price = get_crypto_price()
    await message.reply(price)

  if message.content.startswith('$crypto '):
    price = get_crypto_price_dynamic(message.content[8:])
    await message.reply(price)

  if message.content.startswith('$malaysia_news'):
    news_url = get_random_malaysia_news()
    await message.reply(news_url)

  if message.content.startswith('$news '):
    news_url = get_random_global_news(message.content[6:])
    await message.reply(news_url)

  if message.content.startswith('$write '):
    write_to_csv(message.content[7:])
    await message.reply("Written!")

  if message.content.startswith('$read'):
     reader = read_from_csv()

     for row in reader:
        await message.reply(row[0])

  if message.content.startswith('$analyze'):
     result = analyze()

     await message.reply(result)

  if message.content.startswith('$vote_list'):
     reader = show_restaurants()
     await message.reply("You may choose to vote for")
     for row in reader:
        await message.write(row[0])

  if message.content.startswith('$vote '):
     vote_restaurant = vote(message.content[6:])
     await message.reply("You have voted for " + message.content[6:])


client.run(TOKEN)
