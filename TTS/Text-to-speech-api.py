from gtts import gTTS
import subprocess

#Text to speech API
#Used static text because used in another module of other member
tts = gTTS(text=' world', lang='en')
tts.save("hello.mp3")
subprocess.call(["afplay", "hello.mp3"])