from aiogram import Router, F
from aiogram.types import Message
from create_bot import admin_id  # bot
from aiogram.filters import Filter
# import keyboards.admin_keyboards as kb

admin_router = Router()


class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == int(admin_id)  # admin_id type string


@admin_router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Hello admin!')
