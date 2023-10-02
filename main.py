import asyncio
import logging  # for logging
from create_bot import dp, bot
from handlers.client import my_router, register_handlers_client
from handlers.other import other_router


async def main():
    register_handlers_client()
    dp.include_router(my_router)
    dp.include_router(other_router)
    await dp.start_polling(bot)

# When quickly starting and stopping the bot, the try-except might not catch the error
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # for logging
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')

