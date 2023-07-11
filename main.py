import discord

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

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


def main():
    client.run('ODM3NTEyOTc3NDM4ODY3NDY3.GnKoaT.IWxj5vbTLqYIXEk5V4t7xL36Kywg1F4AZi7jcE')


if __name__ == "__main__":
    main()
