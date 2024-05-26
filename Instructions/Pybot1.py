from nltk.chat.util import Chat
import time


def Pybot_chat():
   
    print("Voici le nom du fichiers a modifier pour modifier le bot : Pybot1.py")

    time.sleep(3)
    
    pairs = [
        ["Bonjour", ["Bonjour monsieur"]],
        ["Hi", ["Hi mister"]],
        ["Hello", ["Hello mister"]],        
        ["Gifs", ["Ok nous vous mettons un Gifs a dispotisions"]]
    ]

    chat = Chat(pairs)
    chat.converse()