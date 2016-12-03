from gtts import gTTS
import subprocess

#Text to speech API

def speak(sentence):
    tts = gTTS(text=sentence, lang='en')
    tts.save("hello.mp3")
    subprocess.call(["afplay", "hello.mp3"])
    return