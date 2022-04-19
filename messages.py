from idconfig import idConfig
import botcreate
from aiogram import types
from morning_greeting import greeting_message

bot = botcreate.bot

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