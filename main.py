import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
from aiogram.types import Message
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):

    user_info = f"""
ID: {message.from_user.id}
Логин: {message.from_user.username}
Имя: {message.from_user.first_name}
        """
    text = f"""Новый пользователь подключился:\n{user_info}"""

    await bot.send_message(admin_id, text)
    await message.answer(f'Hi {message.from_user.username}')


@dp.message(F.text == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')


async def main():
    await dp.start_polling(bot)

# When quickly starting and stopping the bot, the try-except might not catch the error
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')

