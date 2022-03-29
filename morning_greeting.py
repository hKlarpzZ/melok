from urllib import response
from googletrans import Translator
import requests
import time

tran = Translator()
date = ''
course = ''
course_prev = ''
open_weather_token = 'c49fac1e9306db2d04c7d7b61dfbc5ab'
icon_id = ''
weather_message = ''
course_message = ''


def dollar_course():
    global date, course, course_prev, course_message
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date = f'{time.localtime()[2]} {months[time.localtime()[1] - 1]} {time.localtime()[0]} года'
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()# Оригинальное api: https://cdn.cur.su/api/cbr.json
    course = data['Valute']['USD']['Value']
    course_prev = data['Valute']['USD']['Previous']
    course_message = f'Доброе утро!\n\n⏱ Сегодня {date},\n💰 Доллар сегодня стоит {course},\n💸 Хотя вчера стоил {course_prev}.'
    return course_message

def greeting_message():
    global course_message, icon_id, weather_message
    dollar_course()
    current_weather()
    return course_message + '\n\nПогода:', icon_id, weather_message

def current_weather():
    global tran, icon_id, weather_message
    data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q=Moscow&limit=1&appid={open_weather_token}').json()[0]
    lat = data['lat']
    lon = data['lon']
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}').json()
    weather = data['weather'][0]
    icon_id = weather['icon']
    main_translation = tran.translate(weather["main"], dest='ru')
    desc_translation = tran.translate(weather["description"], dest='ru')
    weather_message = f'<b>{main_translation.text}</b>\n{desc_translation.text}\nТемпература: <b>{round(data["main"]["temp"] - 273.15, 1)}</b>, но ощущается как <b>{round(data["main"]["feels_like"] - 273.15, 1)}</b>\n\nВлажность: {data["main"]["humidity"]} %,\nДавление: {data["main"]["pressure"]} гПа,\nСкорость ветра: {data["wind"]["speed"]} м/с,\nВидимость: {data["visibility"]/1000} км.'
    return icon_id, weather_message

current_weather()
    # icon: http://openweathermap.org/img/wn/{icon_id}@2x.png