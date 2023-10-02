from aiogram import Router, F
from aiogram.types import Message
from create_bot import bot, admin_id
import keyboards as kb

my_router = Router()


async def cmd_start(message: Message,):

    user_info = f"""
ID: {message.from_user.id}
Логин: {message.from_user.username}
Имя: {message.from_user.first_name}
        """
    text = f"""Новый пользователь подключился:\n{user_info}"""

    await bot.send_message(admin_id, text)
    await message.answer(f'Hi {message.from_user.username}' '\nChoose AI command   /select_ai')


async def cmd_select_ai(message: Message,):
    await message.answer('Select AI: ', reply_markup=kb.main)


async def on_chat_gpt_4(message: Message):
    await message.answer('Select a chat to communicate with the GPT-4 chat', reply_markup=kb.chat_gpt)


async def links_func(message: Message,):
    await message.answer('links to AI:', reply_markup=kb.links)


async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')


# By observer method - router.<event_type>.register(handler, <filters, ...>)
# decorator - @router.<event_type>(<filters, ...>)


def register_handlers_client():
    my_router.message.register(cmd_start, F.text == '/start')
    my_router.message.register(cmd_select_ai, F.text == '/select_ai')
    my_router.message.register(on_chat_gpt_4, F.text == 'Chat GPT-4')
    my_router.message.register(links_func, F.text == 'links to AI')
    my_router.message.register(cmd_my_id, F.text == '/my_id')
