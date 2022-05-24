import os
import asyncio
from sched import scheduler
import aioschedule
from idconfig import idConfig
from aiogram import Bot, Dispatcher, executor
import bot_storage

#  Создание бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
bot_storage.Storage.init(bot, dp)

import scheduler
import commands
import recognition

def main():
    # Запуск исполнителя
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# При старте бота
async def on_startup(_):
    data = idConfig.readFile('ids.json')
    asyncio.create_task(on_schedule())

# Запуск расписания
async def on_schedule():
    scheduler.Schedule()
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

# Вызов главной функции
if __name__ == '__main__':
    main()