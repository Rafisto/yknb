"""
YKNB-discordbot
"""
import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


def generateEmbed(filename):
    """
    A function to generate embed from given content filename
    :param filename: Path to a file from which to generate embed message
    :type filename: path
    :return: Message embed
    :rtype: embed
    """
    with open(filename, 'r', encoding='utf-8') as msg:
        embed = discord.Embed(title=f"{filename.replace('.txt', '')} | Group Manifesto",
                              url="https://discord.gg/NcJ6BcfKaz",
                              description=msg.read(),
                              color=0xff0000)
        embed.set_author(name="Rafist0",
                         icon_url="https://cdn.discordapp.com/avatars/352392491078647808/5a55a61e4bddbbf1262684b21ddf75ae.jpg")
        return embed


@client.event
async def on_ready():
    """
    Function to display successful bot login attempt
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    Send a group of manifestos
    :param message: message user has sent
    :type message: msg
    """
    if message.content.startswith('*manifesto'):
        # TODO: replace with a loop that'd browse through each file in the given directory
        await message.channel.send(embed=generateEmbed('🇺🇸manifesto_EN.txt'))
        await message.channel.send(embed=generateEmbed('🇵🇱manifesto_PL.txt'))
        await message.channel.send(embed=generateEmbed('🇷🇺manifesto_RU.txt'))


client.run(os.getenv("CLIENT_TOKEN"))
