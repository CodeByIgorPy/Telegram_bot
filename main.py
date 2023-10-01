import asyncio
from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv
from aiogram.types import Message
import os

import keyboards as kb

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message,):

    user_info = f"""
ID: {message.from_user.id}
Логин: {message.from_user.username}
Имя: {message.from_user.first_name}
        """
    text = f"""Новый пользователь подключился:\n{user_info}"""

    await bot.send_message(admin_id, text)
    await message.answer(f'Hi {message.from_user.username}' '\nChoose AI command   /select_ai')


@dp.message(F.text == '/select_ai')
async def cmd_select_ai(message: Message,):
    await message.answer('Select AI: ', reply_markup=kb.main)


@dp.message(F.text == 'Chat GPT-4')
async def on_chat_gpt_4(message: Message):
    await message.answer('Select a chat to communicate with the GPT-4 chat', reply_markup=kb.chat_gpt)


@dp.message(F.text == 'links to AI')
async def links_func(message: Message,):
    await message.answer('links to AI:', reply_markup=kb.links)


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

