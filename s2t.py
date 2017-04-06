import speech_recognition

class S2T(object):
    def listen(self):
            recognizer = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)

            try:
                    #return recognizer.recognize_sphinx(audio)
                    return recognizer.recognize_google(audio)
            except speech_recognition.UnknownValueError:
                    print("Could not understand audio")
            except speech_recognition.RequestError as e:
                    print("Recog Error; {0}".format(e))

            return ""

    def startListening(self):
        #print("Listening...")
        app = self.listen()
        #print("End of Listening..")
        print("What I heard:-" + str(app))
        return str(app)

if __name__ =='__main__':
    s2t = S2T()
    s2t.startListening()
