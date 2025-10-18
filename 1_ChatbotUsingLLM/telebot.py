import openai
import os, sys
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")
BOT_TOKEN = os.getenv("TOKEN")

# model name 
MODEL_NAME = "gpt-3.5-turbo"

# Initialize bot and dispatcher
myBot = Bot(token= BOT_TOKEN)
dp = Dispatcher()              #   processes the message updates


class memReference:
    '''
    A class to store previous response from the chatGPT API
    '''
    def __init__(self) -> None:
        self.response = ""


refObj = memReference()



def clear_past_memory():
    '''
    A function to clear the previous conversation and context
    '''
    refObj.response = ""


@dp.message(Command(commands=["start"]))
async def welcome(message: types.Message):
    '''
    This handler receives messages with '/start' and '/help' command
    '''
    await message.reply("Hi Monika!\nI am second Echo Bot!\nPowered by Aiogram 3")


@dp.message(Command(commands=["clear"]))
async def clear(message: types.Message):
    '''
    This handler receives '/clear' command and clear all the previous conversation and context
    '''
    clear_past_memory()
    await message.reply("I have cleared all the past conversation and context for you.")


@dp.message(Command(commands=["help"]))
async def display_help_menu(message: types.Message):
    '''
    This handler receives '/help' command and display the help menu options
    '''
    help_command = '''
    Relax boss!!! Please follow the following commands:
    /start - To start the conversation
    /clear - To clear the past conversations and context
    /help - To get this help menu
    I hope this helps you buddy. :)
    '''
    await message.reply(help_command)


@dp.message()
async def chatgpt(message: types.Message):
    '''
    This handler process the user's input and generate a response using ChatGPT API.
    '''
    print(f">>> USER: \n\t{message.text}")
    
    # Refer openAPI docs to get this code snippet
    response = openai.ChatCompletion.create(
        model = MODEL_NAME,
        messages = [
            {'role': 'assistant', 'content': refObj.response},      # our bot           Output
            {'role': 'user', 'content': message.text}               # our query         Input
        ]
    )
    
    refObj.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{refObj.response}")
    await myBot.send_message(chat_id = message.chat.id, text = refObj.response)


async def main():
    await dp.start_polling(myBot)

if __name__ == "__main__":
    asyncio.run(main())