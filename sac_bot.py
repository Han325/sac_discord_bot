import discord

from settings import TOKEN


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.reply('Hello!', mention_author=True)

    if message.content.startswith('$greet'):
        await message.reply('Hello, {0.author}!'.format(message), mention_author=True)

    if message.content.startswith('$echo '):
        await message.reply(message.content[1:], mention_author=True)


client.run(TOKEN)
