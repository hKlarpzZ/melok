import asyncio
import aioschedule
import os
from idconfig import idConfig
from words import *
from morning_greeting import greeting_message
from aiogram import Bot, Dispatcher, executor, types

# Создание бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# При старте бота
async def on_startup(_):
    data = idConfig.readFile('ids.json')
    asyncio.create_task(on_schedule())



# Запуск расписания
async def on_schedule():
    aioschedule.every().day.at("08:00").do(morning_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

# Функция отправки сообщения утром
async def morning_message():
    data = idConfig.readFile('ids.json')
    for id in data['id']:
        global_message = greeting_message()
        await bot.send_message(id, global_message[0])
        media = types.MediaGroup()
        media.attach_photo(f'http://openweathermap.org/img/wn/{global_message[1]}@2x.png')
        await bot.send_media_group(id, media=media)
        await bot.send_message(id, str(global_message[2]), parse_mode='HTML')

# Команда /start
@dp.message_handler(commands=['start'])
async def id_link(message : types.message):
    try:
        id = message.from_user.id
        data = idConfig.readFile('ids.json')
        if id not in data['id']:
            try:
                await bot.send_message(id, f'Добавляю ваш <b>айди</b> в список!', parse_mode='HTML')
                idConfig.addId('ids.json', id)
                await bot.send_message(id, f'✅ Я успешно добавил ваш айди!')
                await message.delete()
            except Exception as ex:
                await message.answer(f'⛔️ Что-то пошло не так...\n{ex}')
        else:
            await bot.send_message(id, f'⚠️ Я уже добавил ваш айди, нет необходимости делать это ещё раз!')
            await message.delete()
    except:
        await message.reply('⛔️ Я не смог вас добавить! Вы должны прописать команду мне в ЛС: https://t.me/hedricksmelokbot')

# Команда /revoke
@dp.message_handler(commands=['revoke'])
async def id_revoke(message : types.message):
    try:
        id = message.from_user.id
        idConfig.removeId('ids.json', id)
        await bot.send_message(id, f'✅ Я успешно удалил ваш айди! Теперь вам не будут приходить сообщения.')
        await message.delete()
    except Exception as ex:
        await message.reply(f'⛔️ Я не смог вас убрать! Произошла какая-то ошибка:\n{ex}')
        

# Текстовые команды
@dp.message_handler()
async def oclick(message : types.message):
    if message.text.lower() in nicks:
        await message.reply('Слушаю...')
    elif message.text.lower() in morning:
        try:
            id = message.from_user.id
            global_message = greeting_message()
            await bot.send_message(id, global_message[0])
            media = types.MediaGroup()
            media.attach_photo(f'http://openweathermap.org/img/wn/{global_message[1]}@2x.png')
            await bot.send_media_group(id, media=media)
            await bot.send_message(id, str(global_message[2]), parse_mode='HTML')
        except:
            await message.reply('⛔️ Сначала напишите мне в лс. Я не могу отправлять сообщения первым!')

# Запуск исполнителя
def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# Вызов главной функции
if __name__ == '__main__':
    main()