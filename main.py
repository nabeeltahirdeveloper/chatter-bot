from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot('My ChatterBot')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

from chatterbot.logic import BestMatch

bot.set_trainer(BestMatch())

while True:
    user_input = input("User: ")
    bot_response = bot.get_response(user_input)
    print("Bot: ", bot_response)
