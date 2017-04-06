from chatterbot import ChatBot


class MyChatBot(object):

    def __init__(self):
        print("comes here")
        bot = ChatBot(
            'Ron Obvious',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )

        self.chatbot = bot
        print(" chatbot is getting trained")
        # Train based on the english corpus
        self.chatbot.train("chatterbot.corpus.english")

        print(" chatbot is Ready")
        # Get a response to an input statement

    def ask(self, question):
        reply = self.chatbot.get_response(str(question))
        print("chat bot reply" + str(reply))
        return reply


if __name__ =='__main__':
    bot = MyChatBot()
    bot.ask("Good Morning")