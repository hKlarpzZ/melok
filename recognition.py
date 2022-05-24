import vosk
import pyaudio
import json
import speech
import requests
from discord_token import token

model = vosk.Model("model_small")
rec = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

speech.program_start()

for text in listen():
    print(text)
    headers = {
            'authorization':f'{token}'
        }
    namings = ['мелок', 'белок', 'милок']
    if text in namings:
        speech.say('слушаю')
        continue
    for name in namings:
        if text.startswith(name):
            text = text.lstrip(name+' ')
            if text.startswith('скажи'):
                text = text.lstrip('скажи ')
                speech.say(text)
                continue
            if text.startswith('поставь на паузу') or text.startswith('пауза'):
                payload = {
                    'content': "`stop"
                }
                r = requests.post("https://discord.com/api/v9/channels/707594847720177777/messages?limit=50", data=payload, headers=headers)
                continue
            if text.startswith('плэй') or text.startswith('продолжить проигрывание') or text.startswith('продолжи проигрывание'):
                payload = {
                    'content': "`play"
                }
                r = requests.post("https://discord.com/api/v9/channels/707594847720177777/messages?limit=50", data=payload, headers=headers)
                continue
    if text.startswith('системный вызов тишина'):
        speech.say('Мьючу всех!')
        payload = {
            'content': "`muteall"
        }
        r = requests.post("https://discord.com/api/v9/channels/707594847720177777/messages?limit=50", data=payload, headers=headers)
        continue
    if text.startswith('системный вызов можно говорить'):
        speech.say('Размьючу всех!')
        payload = {
            'content': "`unmuteall"
        }
        r = requests.post("https://discord.com/api/v9/channels/707594847720177777/messages?limit=50", data=payload, headers=headers)
        continue
