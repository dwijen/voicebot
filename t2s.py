from gtts import gTTS
import os

class T2S(object):
    def test2Speech(self, text):
        tts = gTTS(text=str(text), lang='en')
        tts.save("hello.mp3")

        os.system("mpg321 hello.mp3")


if __name__ =='__main__':
    t2s = T2S()
    t2s.test2Speech("Good Morning")