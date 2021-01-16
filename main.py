"""
Ceci est le main AntiAlzheimer project
"""

file = open("user.gks", "w")
file.close()
from tkinter import *
from datetime import *
import webbrowser
import random
import os




def help():
    # ouvrir une page web avec de l'aide
    webbrowser.open_new("https://sites.google.com/view/projet-alzheimer/accueil")

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
        try:
            os.mkdir(user_name)
        except:
            pass
        reference_file = open("user.gks", "r")

        user_list = reference_file.readlines


        # création du nom pour le dossier/fichier pour la sauvgarde des connexctions
        dir_name_connexction = str(user_name+"/latest connection.gks")


        # Créer (ou ouvre s'il existe déjà) le fichier de sauvegarde de l'utilisateur
        fichier_conection = open(dir_name_connexction, "a")
        fichier_conection.write("latest connection :\n")
        fichier_conection.write(str(datetime.now()) + "\n")

        # création du nom pour le dossier/fichier pour la sauvgarde du journal
        dir_name_journal = str(user_name + "/journal.gks")


        # Créer (ou ouvre s'il existe déjà) le fichier de sauvegarde du journal de l'utilisateur
        fichier_journal = open(dir_name_journal, "a")


        # fenetre avec les exercices etc...
        windowAl = Tk()
        window.destroy()




        def main_menu():
            for c in windowAl.winfo_children():
                c.destroy()
            windowAl.title(user_name)
            windowAl.geometry("1200x750")
            windowAl.minsize(1200, 750)
            label_Al = Label(windowAl, text="Bonjour " + user_name, font=("Courrier", 40), bg='#808080', fg='black')
            windowAl.config(background="#808080")
            game_button = Button(windowAl, text="Jeu de couleur", font=("courrier", 25), bg='#808080', fg='black', command=color_game)
            game_button.pack()
            game_button.place(x=250, y=200)

            write_button = Button(windowAl, text="J'écris ma journée", font=("courrier", 25), bg='#808080', fg='black', command=write_his_day)
            write_button.pack()
            write_button.place(x=650, y=200)

            # création barre de menu
            menu_bar = Menu(windowAl)
            # créer un menu de navigation
            navigation_menu = Menu(menu_bar, tearoff=0)
            navigation_menu.add_command(label="menu", command=main_menu)
            navigation_menu.add_command(label="journal", command=write_his_day)
            navigation_menu.add_command(label="jeu de couleur", command=color_game)
            menu_bar.add_cascade(label="navigation", menu=navigation_menu)

            # créer un menu d'aide
            help_menu = Menu(menu_bar, tearoff=0)
            help_menu.add_command(label="Aide", command=help)
            help_menu.add_command(label="Quitter", command=windowAl.destroy)
            menu_bar.add_cascade(label="Aide", menu=help_menu)

            # config window pour le menu
            windowAl.config(menu=menu_bar)



            label_Al.pack()
            windowAl.mainloop()


        def write_his_day():
            for c in windowAl.winfo_children():
                c.destroy()

            # créer une zone de texte
            scroll = Scrollbar(windowAl)
            text_zone = Text(windowAl, font=("Arial", 20), yscrollcommand=scroll.set)
            scroll.config(command=text_zone.yview())
            scroll.pack(side=RIGHT, fill=Y)
            text_zone.pack(pady=40, fill=X, padx=5)


            main_button = Button(windowAl, text="<", font=("courrier", 15), bg='#808080', fg='white', command=main_menu)
            main_button.pack()
            main_button.place(x=0, y=0)

            # création barre de menu
            menu_bar = Menu(windowAl)

            # créer un menu d'éditeur de texte
            text_menu = Menu(menu_bar, tearoff=0)
            text_menu.add_command(label="enregistrer")
            menu_bar.add_cascade(label="action", menu=text_menu)

            # créer un menu de navigation
            navigation_menu = Menu(menu_bar, tearoff=0)
            navigation_menu.add_command(label="menu", command=main_menu)
            navigation_menu.add_command(label="journal", command=write_his_day)
            navigation_menu.add_command(label="jeu de couleur", command=color_game)
            menu_bar.add_cascade(label="navigation", menu=navigation_menu)

            # créer un menu d'aide
            help_menu = Menu(menu_bar, tearoff=0)
            help_menu.add_command(label="Aide", command=help)
            help_menu.add_command(label="Quitter", command=windowAl.destroy)
            menu_bar.add_cascade(label="Aide", menu=help_menu)

            # config window pour le menu
            windowAl.config(menu=menu_bar)

            windowAl.mainloop()


        def color_game():
            for c in windowAl.winfo_children():
                c.destroy()

            def start_game():
                level = difficuty.get()

                if level == "1":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    frame_origine = LabelFrame(windowAl, text="Origine", bd=5, labelanchor='n')
                    frame_exercice = LabelFrame(windowAl, text="exercice", bd=5, labelanchor='s')




                    frame_origine.pack(expand=YES)
                    frame_exercice.pack(expand=YES)
                    windowAl.mainloop()


                if level == "2":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "3":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "4":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "5":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "6":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "7":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "8":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

                if level == "9":
                    for c in windowAl.winfo_children():
                        c.destroy()

                    # création barre de menu
                    menu_bar = Menu(windowAl)
                    # créer un menu d'aide
                    help_menu = Menu(menu_bar, tearoff=0)
                    help_menu.add_command(label="Aide", command=help)
                    help_menu.add_command(label="Quitter", command=windowAl.destroy)
                    menu_bar.add_cascade(label="Aide", menu=help_menu)
                    # config window pour le menu
                    windowAl.config(menu=menu_bar)

                    windowAl.mainloop()

            frame1 = Frame(windowAl, bg='#808080')

            main_button = Button(windowAl, text="menu", font=("courrier", 25), bg='#808080', fg='white',command=main_menu)
            main_button.pack()
            main_button.place(x=5, y=5)

            # création barre de menu
            menu_bar = Menu(windowAl)
            # créer un menu de navigation
            navigation_menu = Menu(menu_bar, tearoff=0)
            navigation_menu.add_command(label="menu", command=main_menu)
            navigation_menu.add_command(label="journal", command=write_his_day)
            navigation_menu.add_command(label="jeu de couleur", command=color_game)
            menu_bar.add_cascade(label="navigation", menu=navigation_menu)

            # créer un menu d'aide
            help_menu = Menu(menu_bar, tearoff=0)
            help_menu.add_command(label="Aide", command=help)
            help_menu.add_command(label="Quitter", command=windowAl.destroy)
            menu_bar.add_cascade(label="Aide", menu=help_menu)

            # config window pour le menu
            windowAl.config(menu=menu_bar)

            label_selecteur = Label(frame1, text="Selectionez votre niveau de difficultée", font=("Courrier", 40), bg='#808080', fg='white')
            label_selecteur.pack()

            # selecteur de difficulté du jeu
            difficuty = Spinbox(frame1, font=("courrier", 25), bg='#808080', fg='white', buttonbackground='#FF0000', from_=1, to=9, increment=1)
            difficuty.pack()

            difficulty_button = Button(frame1, text="Choisir", font=("Courrier", 20), bg='#0000FF', fg='#00FF00', command=start_game)
            difficulty_button.pack(pady=10)


            frame1.pack(expand=YES)
            windowAl.mainloop()

        main_menu()# faire apparaitre le main menu

#####################################################################

# créer la fenetre du logeur
window = Tk()

# personaliser fenetre
window.title("Science plus")
window.geometry("1080x720")
window.minsize(480, 360)
window.update()
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
