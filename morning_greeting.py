from urllib import response
import requests
import time

date = ''
course = ''
course_prev = ''

def dollar_course():
    global date, course, course_prev
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date = f'{time.localtime()[2]} {months[time.localtime()[1] - 1]} {time.localtime()[0]} года'
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    course = data['Valute']['USD']['Value']
    course_prev = data['Valute']['USD']['Previous']

def greeting_message():
    global date, course, course_prev
    dollar_course()
    return f'Доброе утро!\n\n⏱ Сегодня {date},\n💰 Доллар сегодня стоит {course},\n💸 Хотя вчера стоил {course_prev}.'