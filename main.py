# Summary:
# Created by Thomas Tramp
# Date of initional creation: 9/19/2021

# Comments
# first draft of discord bot


# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
from datetime import datetime
import discord

# IMPORT THE OS MODULE.
import os

# Custom imports
from WritingToFile import filewriting
from WeaponDeaths import Weapons

import re

# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# initalize model
weapons = Weapons()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.

# initalization startup


@bot.event
async def on_ready():
    print('We have logged in as \"{0.user}\"'.format(bot))

    from datetime import time
    currentTime = datetime.now()
    print("Current time: ", currentTime.strftime("%H:%M:%S"))

    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.

# Generic String catch


def getGenericKappaEmoji():
    print("The first attempted failed. Trying again with generic string search.")
    for emoji in bot.guild.emojis:
        if emoji.name.find("kappa") != -1:
            return emoji


def getDiscordKappa(message):
    return discord.utils.get(message.guild.emojis, name='kappa')


def sendFriendlyResponse(message):
    try:
        returnedEmoji = getDiscordKappa(message)
    except:
        returnedEmoji = getGenericKappaEmoji()
    finally:
        result = "Hey Shithead " + "<:" + returnedEmoji.name + \
            ":" + str(returnedEmoji.id) + ">"

    return result


@bot.event
async def on_ready():
    print('Hello, I am online.')

async def on_message(message):
    msg = message.content
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if msg == "Hello":
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        msgSent = await message.channel.send(sendFriendlyResponse(message))

        # Add reaction to the end of the message
        await msgSent.add_reaction(getDiscordKappa(msgSent))

    if msg.startswith('$online'):
        await message.channel.send('Hello, I am online.')

    if msg == "$savefile":
        # TODO: Generate content to write out
        content = ''
        msgSent = await message.channel(filewriting.writeToFile(content))

    # Old idea, instead just use bottoms as active updates to the count.
    if msg.startswith('$') and msg.endswith('$'):
        # check model property for name
        x = getattr(weapons, msg, 0)
        if(x != 0):
            #TODO: write regular expression statement that will ignore the model name, and instead grab the int value passed in the string
            expression = ''
            value = re.search(expression, msg)
            setattr(weapons, msg, value)

    #New idea, add all weapons into a long list and an associated button to them as such
    """
    Weapon1
    Weapon2
    Weapon3

    Then their associated reactions
    Smile, Sad, Happy
    """
    #Then add code so that everytime that button is hit, it adds one to the count.


bot.run(DISCORD_TOKEN)


# TestMethods
