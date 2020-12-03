"""Ceci les le main AntiAlzheimer project"""

from tkinter import *



def co():
    user_name = co_txt_entry.get()

    if user_name == "Jay":
        fichier = open(user_name + ".gks", "a")
        windowAl = Tk()
        label_Al = Label(windowAl, text="Bonjour" + user_name, font=("Courrier", 40), bg='#ffd100', fg='white')
        windowAl.title(user_name)
        windowAl.geometry("1200x750")
        windowAl.minsize(480, 360)
        windowAl.config(background="#ffd100")

        label_Al.pack()
        windowAl.mainloop()




# créer la fenetre
window = Tk()

#personaliser fenetre
window.title("Science plus ( par Henry Legrand )")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("logo-atom_355-543.ico")
window.config(background='#ffd100')

# frame
frame = Frame(window, bg='#ffd100')

# texte
label_titel = Label(frame, text="BIENVENUE", font=("Courrier", 40), bg='#ffd100', fg='white')
label_connexion = Label(frame, text="Connectez vous", font=("Courrier", 30), bg='#ffd100', fg='white')

# logeur
co_txt_entry = Entry(frame, text="mot de passe", font=("Courrier", 20), bg='white')

# bouton
co_button = Button(frame, text="Connexion", font=("Courrier", 20), bg='white', fg='black', command=co)

    
# tout afficher
label_titel.pack()
label_connexion.pack()
co_txt_entry.pack()
co_button.pack(pady=25, fill=X)
frame.pack(expand=YES)
window.mainloop()


        




