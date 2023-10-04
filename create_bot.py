from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
admin_id = os.getenv('ADMIN_ID')
bot_token = os.getenv('TOKEN')
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

ngrok_tunel_url = os.getenv('NGROK_TUNEL_URL')
app = FastAPI()
WEBHOOK_PATH = f"/bot/{bot_token}"
WEBHOOK_URL = f"{ngrok_tunel_url}{WEBHOOK_PATH}"


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)

if __name__ == '__main__':
    app.on_startup.append(on_startup)
