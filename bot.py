import discord
import responses
from discord.ext import commands
from ignored import ignoredAPI
import os


async def send_message(message, user_message, is_private):

    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():

    TOKEN = ignoredAPI

    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='*', intents=discord.Intents.all())

    @client.event
    async def on_ready():

        await client.tree.sync()

        print(f'{client.user} is working.')

    @client.tree.command(name='gpt', description='this is for fun')
    async def nofweakingway(interaction: discord.Interaction):
        await interaction.response.send_message('Hello')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} at {channel} ')

        if user_message[0] == '*':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

        if user_message:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
