import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
#print(BOT_TOKEN)


# Configure Logging
logging.basicConfig(level = logging.INFO)


# Initialize bot and dispatcher
myBot = Bot(token= BOT_TOKEN)
dp = Dispatcher()              #   processes the message updates


@dp.message(Command(commands=["start", "help"]))
async def command_start_handler(message: types.Message):
    await message.reply("Hi Monika!\nI am your Echo Bot!\nPowered by Aiogram 3")

@dp.message()
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)


async def main():
    await dp.start_polling(myBot)

if __name__ == "__main__":
    asyncio.run(main())