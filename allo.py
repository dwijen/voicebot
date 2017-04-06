import s2t
import t2s
import chatbot


class Allo(object):
    def askChatBot(self, text):
        pass



if __name__ =='__main__':
    chatbot = chatbot.MyChatBot()
    s2t = s2t.S2T()
    t2s = t2s.T2S()

    while True:
        print("Tell Something")
        t2s.test2Speech("Tell Something")
        speechText = s2t.startListening()
        botReply = chatbot.ask(speechText)
        t2s.test2Speech(botReply)