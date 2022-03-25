import asyncio
import aioschedule
import os
from words import *
from morning_greeting import greeting_message
from aiogram import Bot, Dispatcher, executor, types

# Создание бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# При старте бота
async def on_startup(_):
    asyncio.create_task(on_schedule())



# Запуск расписания
async def on_schedule():
    aioschedule.every().day.at("08:00").do(morning_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

# Функция отправки сообщения утром
@dp.message_handler()
async def morning_message():
    await bot.send_message(920189870, greeting_message())

# Команда /start
@dp.message_handler(commands=['start'])
async def id_link(message : types.message):
    try:
        await bot.send_message(message.from_user.id, f'✅ Я успешно добавил ваш айди ({message.from_user.id})!')
        await message.delete()
    except:
        await message.reply('⛔️ Я не смог вас добавить! Вы должны прописать команду мне в ЛС: https://t.me/hedricksmelokbot')

# Текстовые команды
@dp.message_handler()
async def oclick(message : types.message):
    if message.text.lower() in nicks:
        await message.reply('Слушаю...')
    elif message.text.lower() in morning:
        await message.answer(greeting_message())

# Запуск исполнителя
def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

if __name__ == '__main__':
    # Вызов главной функции
    main()