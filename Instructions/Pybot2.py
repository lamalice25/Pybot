from tkinter import*
import datetime
from tkinter import filedialog
import webbrowser
from tkinter import messagebox
import time
from Instructions.voice import droid






def pybot2():
    
    root = Tk()


    droid.say("Nous initialisons le démmarage de l'aplications")
    droid.runAndWait()


    droid.say("Initialisations de l'aplications terminer démmarage en cours d'éxécutions")
    droid.runAndWait()


    def envoie(event=None):
        envoie = "Moi : " +e.get()
        txt.insert(END, "\n"+envoie)

        if 'bonjour' in e.get():
            txt.insert(END, "\n"+"multibot : Bonjour comment puise-je vous aider?")
        elif 'heure' in e.get():
            heure = datetime.datetime.now().strftime("%H:%M:%S")
            txt.insert(END, "\n" + "multibot: il est "+heure)
        
        elif 'salut' in e.get():
            txt.insert(END, "\n"+"multibot : Bonjour comment puise-je vous aider?")

        elif 'Aurevoir' in e.get():
            txt.insert(END, "\n"+"multibot : Aurevoir")
            
            time.sleep(2)
            
            root.destroy()
            quit()       
        
        
        
        else: 
            txt.insert(END, "\n" + "multibot : cette phrase n'est pas dans ma base de donné.")
        



        e.delete(0, END)
    
    def save_conversation():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(txt.get("1.0", END))

    menu_bar = Menu(root)
    root.config(menu=menu_bar)


    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    file_menu.add_command(label="Enregistrer la conversation", command=save_conversation)

    txt = Text(root)
    txt.grid(row=0, column=0, columnspan=2)
    e = Entry(root, width=100)
    e.grid(row=1, column=0)

    e.bind('<Return>', envoie)
    envoyer = Button(root, text="Envoyer", command=envoie).grid(row=1, column=1)


    root.title('multibot')
    root.mainloop()