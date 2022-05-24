from email.mime import audio
import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'aidar' # aidar, baya, kseniya, xenia, random 
put_accent = True
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "Я тут!"

voice_model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_tts', language=language, speaker=model_id)
voice_model.to(device)

def program_start():
    audio = voice_model.apply_tts(text=text, speaker=speaker, sample_rate=sample_rate, put_accent=put_accent, put_yo=put_yo)

    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate + 1)
    sd.stop()

def say(text):
    audio = voice_model.apply_tts(text=text, speaker=speaker, sample_rate=sample_rate, put_accent=put_accent, put_yo=put_yo)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate + 1)
    sd.stop()