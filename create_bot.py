from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()
admin_id = os.getenv('ADMIN_ID')

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()