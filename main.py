import time
import schedule
import os
from words import *
from morning_greeting import greeting_message
from aiogram import Bot, Dispatcher, executor, types



# Создание бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def oclick(message : types.Message):
#     # Добавление id чатов
#     if str(message.chat.id) not in config.id:
#         print(f'Нет айди {message.chat.id}')
#         config.id.append(f'{message.chat.id}')
#         Config.write('config.json', config)
    
    # Текстовые команды
    if message.text.lower() in nicks:
        await message.reply('Слушаю...')
    elif message.text.lower() in morning:
        await message.answer(greeting_message())

def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    # Вызов главной функции
    main()