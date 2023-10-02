from aiogram import Router, F
from aiogram.types import Message

other_router = Router()


@other_router.message(F.text == "/dice")
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


@other_router.message(F.text == "/bowling")
async def cmd_bowling(message: Message):
    await message.answer_dice(emoji='🎳')
