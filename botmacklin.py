# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

FANG_USER = 'fang#2211'
B_MACKLIN_USER = 'Burt_Macklin38#1600'
FANGS_BOT = 'hahaxd#1567'
BOT_MACKLIN = 'BotMacklin#1562'

HELP_COMMAND = '!help'
HELP_COMMAND_SHORT = '!h'
SUSSY_COMMAND = '!sussy'
SAY_IT_TO_MY_FACE_COMMAND = '!sayittomyface'
VERY_INTERESTING_COMMAND = '!veryinteresting'
DEBUG = True 

def debug(debug_message):
    if DEBUG: 
        print(debug_message)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f"User guilds: {client.guilds}")

    for guild in client.guilds:
        print(f'{client.user} is connected to the following guild:\n')
        print(f'{guild.name}(id: {guild.id})')

# Commands 
async def help_response(message):
    await message.channel.send("""
    BotMacklin Help Menu:
        * !help [!h] - Help Menu 
        * !sussy - Kinda sus tbh 
        * !sayittomyface - What do you think 
        * !veryinteresting - Interesting
    """)

async def sussy_response(message):
    with open('Attachments\sussy_thicc.gif', 'rb') as sussy_f:
        await message.channel.send('P(M)EGASUS')
        sus = discord.File(sussy_f)
        await message.channel.send(file=sus) 

async def say_it_to_my_face(message):
    with open('Attachments\say_it_to_my_face.gif', 'rb') as milo_f:
        milo = discord.File(milo_f)
        await message.channel.send(file=milo)

async def verry_interesting(message):
    await message.channel.send('Verrry interesting') 


# Message Response 
@client.event
async def on_message(message):
    command = message.content
    debug(f"Message content: {message.content} from {message.author}")

    if str(message.author) == BOT_MACKLIN:
        return

    try:
        if SUSSY_COMMAND in command:
            await sussy_response(message)
        elif HELP_COMMAND in command or HELP_COMMAND_SHORT in command:
            await help_response(message)
        elif SAY_IT_TO_MY_FACE_COMMAND in command:
            await say_it_to_my_face(message)
        elif VERY_INTERESTING_COMMAND in command:
            await verry_interesting(message)
    except NotImplemented:
        message.channel.send("Sorry that command is unavailable, it's Fangs fault")

client.run(TOKEN)
