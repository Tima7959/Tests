import os
import asyncio

import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('API'))

from handlers.for_user import rt

logging.basicConfig(level=logging.debug, filename='tgbotlogs.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='utf-8', filemode='w')

ALLOWED_UPDATES = ['message']
dp = Dispatcher()
dp.include_router(rt)

async def main(): 
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == '__main__':
    asyncio.run(main())