"""
Ceci les le main AntiAlzheimer project
"""
file = open("user.gks", "w")
file.close()

"""
Ceci les le main AntiAlzheimer project
"""
file = open("user.gks", "w")
file.close()
from tkinter import *


def admin_interface():
    windowAl = Tk()

    # variable pour la boucle du programme
    run = True

    """
    Boucle du programme :
    Avantage d'un "while":
    - on peut la casser à tout moment si on a besoin
    Inconvénients:
    - Plus il y a d'instruction, plus la boucle et longue et donc plus il y a de laggs potentiels
    """
    while run:
        label_Al = Label(windowAl, text="Interface administrateur", font=("Courrier", 40), bg='#395D67',fg='#FFAA00')
        windowAl.title("ADMIN MODE")
        windowAl.geometry("1200x750")
        windowAl.minsize(1200, 750)
        """
        menu_mode est la variable qui permet de choisir le menu où on veut aller, comme si-dessous :
        0 = main menu
        1 = ...
        """
        menu_mode = 0

        if menu_mode == 0:
            label_Al = Label(windowAl, text="Interface administrateur", font=("Courrier", 40), bg='#395D67',fg='#FFAA00')
            windowAl.config(background="#395D67")
            label_Al.pack()


        main_button = Button(windowAl, text="menu", font=("courrier", 25), bg='#395D67', fg='#FFAA00')
        main_button.pack()
        main_button.place(x=5, y=5)


        windowAl.mainloop()


def co():
    user_name = co_txt_entry.get()
    admin_name = user_name
    admin_name = admin_name.upper()
    if admin_name == "ADMIN":
        admin_interface()

    else:
        reference_file = open("user.gks", "r")
        # Créer (ou ouvre s'il existe déjà) le fichier de sauvegarde de l'utilisateur
        fichier = open(user_name + ".gks", "a")
        # fenetre avec les exercices etc...
        windowAl = Tk()

        # variable pour la boucle du programme
        run = True

        """
        Boucle du programme :
        Avantage d'un "while":
        - on peut la casser à tout moment si on a besoin
        Inconvénients:
        - Plus il y a d'instruction, plus la boucle et longue et donc plus il y a de laggs potentiels
        """
        while run:

            """
            menu_mode est la variable qui permet de choisir le menu où on veut aller, comme si-dessous :
            0 = main menu
            1 = ...
            """
            menu_mode = 0
            windowAl.title(user_name)
            windowAl.geometry("1200x750")
            windowAl.minsize(1200, 750)
            if menu_mode == 0:
                label_Al = Label(windowAl, text="Bonjour " + user_name, font=("Courrier", 40), bg='#ffd100', fg='white')
                windowAl.config(background="#ffd100")

                label_Al.pack()
                windowAl.mainloop()


            elif menu_mode == 1:
                main_button = Button(windowAl, text="menu", font=("courrier", 25), bg='#ffd100', fg='white')
                main_button.pack()
                main_button.place(x=5, y=5)

                windowAl.mainloop()







# créer la fenetre du logeur
window = Tk()

# personaliser fenetre
window.title("Science plus ( par Henry Legrand )")
window.geometry("1080x720")
window.minsize(480, 360)
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
