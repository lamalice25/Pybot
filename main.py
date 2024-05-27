# From and import

from Instructions import Pybot2
from Instructions import Pybot1
from Instructions.voice import droid
# Import

import webbrowser
import messagebox


exec_code = input("quel code voulais vous executer  : ")

if "pybot1" in exec_code:
    Pybot1.Pybot_chat()

elif "pybot2" in exec_code:
    Pybot2.pybot2()
    

else:
    messagebox.showerror("Erreur de choix", "Une erreur a été détecter")
    webbrowser.open("https://sites.google.com/view/pybot2-0/wiki/home")