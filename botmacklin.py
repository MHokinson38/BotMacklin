# bot.py
import os
import random
from pickle import NONE

import discord
from dotenv import load_dotenv
from WordleWrecker.wordle_wrecker import *

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
VECTOR_COMMAND = '!vector'
GRUSSY_COMMAND = "!grussy"
BEN_COMMAND = "!ben"
ERROR_MESSAGE = "Sorry, something went wrong. It's probably Fang's Fault."
DEBUG = True 

def debug(debug_message):
    if DEBUG: 
        print(debug_message)

def passes_chance(percentage_pass):
    value = random.randint(1,100)

    return percentage_pass >= value

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
        * !vector - Get Vectored [deepfried]
        * !grussy - You get a special treat if you are lucky 
        * !ben - What a cutie

        Wordle Help! Send a dm to me with the following format:
        * for unknown, grey letters. Caps for green, lowercase for yellow. 
        Following the guess, put a comma followed by the greyed out letters for that guess. 
        Put each guess on a new line. 

        Ex. If I guess trace then prion, I might have: 
        \*R\*\*\*,tce
        PR\*o\*,in
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

async def vector_meme(message):
    with open('Attachments\Vector.jpg', 'rb') as vector_f:
        vector = discord.File(vector_f)
        await message.channel.send(file=vector)

async def grussy(message):
    if passes_chance(25):
        with open('Attachments\HoHoHo.jpg', 'rb') as grussy_f:
            grussy = discord.File(grussy_f)
            await message.channel.send(file=grussy)
    else:
        with open('Attachments\Grussy.png', 'rb') as grussy_f:
            grussy = discord.File(grussy_f)
            await message.channel.send(file=grussy)

async def ben_ten(message):
    ben_image = random.randint(1,7)

    image_path = "Attachments\\ben" + str(ben_image) + ".jpg"
    with open(image_path, 'rb') as image_f:
            image = discord.File(image_f)
            await message.channel.send(file=image)

async def verry_interesting(message):
    await message.channel.send('Verrry interesting')

async def wordle_wrecker_call(message):
    message_content = str(message.content)
    # Generate the model 
    with open("WordleWrecker\data\\five_letter_words.txt", "r") as word_list_f:
        word_list = word_list_f.readlines()
        word_list = [word[:-1] for word in word_list]
    model = generate_model(word_list)

    white_list = None
    black_list = None
    for guess in message_content.split("\n"):
        clue_string, white_list, black_list = parse_input(guess, white_list, black_list)
        debug(f"Parsed input. Clue: {clue_string}, White List: {white_list}, Black List: {black_list}")

    matches = sort_through_clues(word_list, clue_string, white_list, black_list)
    best_matches = rank_matches(model, matches, 10)
        
    await message.author.send(f"""Here are the best matches (the higher the number (smaller absolute value because negative) are the best guesses.
                                  But, many of these are likely very close in magnitude, so pick your favorite. 
                                  Best 10 words: {best_matches}""") 


# Message Response 
@client.event
async def on_message(message):
    command = message.content
    if str(message.author) == BOT_MACKLIN:
        return

    debug(f"Message content: {message.content} from {message.author}. It was {message.channel.type}")

    if (str(message.channel.type) == "private"):
        try:
            await wordle_wrecker_call(message)
        except Exception as e:
            debug(f"{e}")
            debug(f"Weird thing went wrong but it's probably ok lol")
            await message.author.send(ERROR_MESSAGE) 

    try:
        if SUSSY_COMMAND in command:
            await sussy_response(message)
        elif HELP_COMMAND in command or HELP_COMMAND_SHORT in command:
            await help_response(message)
        elif SAY_IT_TO_MY_FACE_COMMAND in command:
            await say_it_to_my_face(message)
        elif VERY_INTERESTING_COMMAND in command:
            await verry_interesting(message)
        elif VECTOR_COMMAND in command:
            await vector_meme(message)
        if GRUSSY_COMMAND in command:
            await grussy(message)
        if BEN_COMMAND in command:
            await ben_ten(message)
    except NotImplemented:
        message.channel.send(ERROR_MESSAGE)

client.run(TOKEN)
