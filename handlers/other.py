from aiogram import Router, F
from aiogram.types import Message
from create_bot import bot
from asyncio import sleep
import keyboards.other_keyboards as kb

other_router = Router()


@other_router.message(F.text == "/game")
async def cmd_game(message: Message):
    await message.answer('Choose game: ', reply_markup=kb.game)

# need to add filters

# @other_router.message()
# async def cmd_dice(message: Message):
#     if message.dice.emoji:
#         user_value = message.dice.value
#         user_emoji = message.dice.emoji
#         if message.dice.emoji in '🎰':
#             await sleep(1)
#             await message.answer(f"You number combination {user_value}")
#         if message.dice.emoji in '🎲🎯🏀🎳⚽️':
#             data_bot = await bot.send_dice(emoji=user_emoji, chat_id=message.from_user.id)
#             value_bot = data_bot.dice.value
#             await sleep(4)
#             if user_value == value_bot:
#                 await message.answer("🍀")
#             elif user_value > value_bot:
#                 await message.answer("You win 👍")
#             else:
#                 await message.answer("I win 🤟")
