import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
from aiogram.types import Message
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
# admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Hi')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
