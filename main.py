import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = open('data/token.txt').readline()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


def main():
    client.run(token)


if __name__ == "__main__":
    main()
