from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")
conversation = [
    "Hello",
    "Hi there!",
    "I need to book a flight?",
    "Which city you are going to?",
    "New Delhi",
    "Which city are you leaving from?",
    "Banglore",
    "what is the travel date",
    "10 jan",
    "thanks. your flight details will be shared soon",
    "i need to book a Hotel",
    "Which city you are going to",
    "Gujrat",
    "what is the travel date?",
    "10 jan",
    "what is travel duration",
    "3 days",
    "thanks. your Hotel details will be shared soon",
    "i need to book a cab",
    "Which city you are going to?",
    "Agra",
    "Which city are you leaving from?",
    "New delhi",
    "what is the travel date?",
    "10 jan",
    "what is travel duration",
    "3 days",
    "thanks. your Hotel details will be shared soon"
]
trainer = ListTrainer(chatbot)
trainer.train(conversation)