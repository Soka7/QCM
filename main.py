import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Tk, Label
import random
from PIL import Image, ImageTk
from Extracted_QNA import correct_answer_list

print(correct_answer_list)

ToggleEvents = False
def Toggle():
    global ToggleEvents
    ToggleEvents = True

def Home(ToggleEvents):
    global Bonus
    Bonus = 0
    global Page
    Page = tk.Tk()
    Frame = tk.Frame(Page, bd = 5, relief = "ridge", bg = "Black")
    Frame.grid(padx=10, pady=10)
    
    Titre = tk.Label(Frame, text="LE QCM SUR CHUCK NORRIS (LE GOAT).", bg = "White", fg="Red")
    Titre.grid(column=0, row=0)
    Welcome = tk.Label(Frame, text="Bonjour chers admirateurs du grand CHUCK NORRIS.", bg = "Black", fg="Green")
    Welcome.grid(column=0, row=1)
    Presentation = tk.Label(Frame, text="Le grand CHUCK NORRIS est sans pareil. Saurez vous vous montrer digne d'exister dans un monde ou CHUCK NORRIS a marche ? Decouvrez le dans ce QCM.", bg = "Black", fg="Green")
    Presentation.grid(column=0, row=2)
    global Destroyed
    Destroyed = 0
    Evts = tk.Button(Frame, text="Toggle Events", bg = "Black", fg="Green", command=Toggle)
    Evts.grid(column=0, row=4)
    Start = tk.Button(Frame, text="Prets ?", bg = "Black", fg="Green", command=lambda: Transit(ToggleEvents))
    Start.grid(column=0, row=3)
    
    Page.mainloop()
    
def Event():
    global Fini, NmPage
    Message = messagebox.showinfo("Event !", "Pile ou face.")
    Nmbr = random.randint(1, 3)
    if Nmbr == 1:
        Message1 = messagebox.showinfo("Pile", "RECOMMENCEZ LE QCM !")
        Fini = True
        Transit(ToggleEvents)
    elif Nmbr == 2:
        Message2 = messagebox.showinfo("Face", "+1 !")
        global Bonus
        Bonus = 1
    elif Nmbr == 3:
        Message2 = messagebox.showinfo("Tranche", "BOOM !")
        Fini = True
        NmPage = None
    
def Transit(ToggleEvents):
    global Fini, BonnesReponses, Reponses, NmPage, Destroyed
    NumEvent = random.randint(-5,10)
    if Destroyed == 0:
        Page.destroy()
    Destroyed = 1
    BonnesReponses = correct_answer_list
    Reponses = []
    NmPage = 1
    Fini = False
    while Fini != True:
        if NumEvent == NmPage:
            if ToggleEvents == True:
                Event()
        match NmPage:
            case 1:
                Page1 = CreerPageCustom("Qui est le plus fort, Saitama, Antispiral ou Chuck Norris ?","Saitama","Antispiral","Chuck Norris")
                Page1.CreerPage()
            case 2:
                Page2 = CreerPageCustom("Depuis quand le latin est une langue morte ?", "CN a eu 0","Depuis que les poules ont des dents","???")
                Page2.CreerPage()
            case 3:
                Page3 = CreerPageCustom("Chuck peut-il marcher sur l'eau ?", "Oui","Non","Ptet ben qu'oui ptet ben qu'non")
                Page3.CreerPage()
            case 4:
                Page4 = CreerPageCustom("Que fait Chuck Norris tous les matins ?", "Rien","Il boit sa Heineken reconnaissable a son etoile dans tt la France","Il prouve l'existence de l'anti-matiere dans la 4ieme diemension")
                Page4.CreerPage()
            case 5:
                Page5 = CreerPageCustom("En quoi Hulk se transforme-t-il quand il se met en colere ?", "Bruce Wayne","Franck Leboeuf","Chuck Norris")
                Page5.CreerPage()
            case 6:
                Page6 = CreerPageCustom("Quelle est la couleur du cheval blanc de Chuck Norris ?", "Noir", "Blanc", "Rouge")
                Page6.CreerPage()
            case 7:
                Page7 = CreerPageCustom(
                    "Quel est le nom de la discipline d'arts martiaux que Chuck Norris a créée ?",
                    "Tang Soo Do",
                    "Chun Kuk Do",
                    "Karate Shotokan")
                Page7.CreerPage()

            case 8:
                Page8 = CreerPageCustom(
                    "Dans quel film Chuck Norris a-t-il affronté Bruce Lee ?",
                    "Opération Dragon",
                    "Le Retour du Dragon",
                    "Le Dernier Combat")
                Page8.CreerPage()

            case 9:
                Page9 = CreerPageCustom(
                    "Quel est le nom du personnage interprété par Chuck Norris dans la série 'Walker, Texas Ranger' ?",
                    "Cordell Walker",
                    "John T. Booker",
                    "Jack McCallister")
                Page9.CreerPage()
            case 10:
                Page10 = CreerPageCustom("Quel est le sport préféré de Chuck Norris ?", "Tennis", "Karate", "Dompter des lions")
                Page10.CreerPage()
            case 11:
                Score()
                Fini = True

class CreerPageCustom:
    
    def __init__(self, Tit, C1, C2, C3):
        self.Tit = Tit #Titre
        self.C1 = C1 #Choix 1, 2, 3
        self.C2 = C2
        self.C3 = C3
        
    def CreerPage(self):
        global Pag
        Pag = tk.Tk()
        Fram = tk.Frame(Pag, bd = 5, relief = "ridge", bg = "Black")
        Fram.grid(padx=10, pady=10)
        
        Titr = tk.Label(Fram, text=self.Tit, bg = "Black", fg="Green")
        Titr.grid(column=0, row=0)
        Choix1 = tk.Button(Fram, text=self.C1, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(1))
        Choix1.grid(column=0, row=1)
        Choix2 = tk.Button(Fram, text=self.C2, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(2))
        Choix2.grid(column=0, row=2)
        Choix3 = tk.Button(Fram, text=self.C3, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(3))
        Choix3.grid(column=0, row=3)
        
        Image_ = Image.open("OIP.jpeg")
        Image_ = Image_.resize((100, 100))
        Image_ = ImageTk.PhotoImage(Image_)
        Img = tk.Label(Fram, image=Image_, bg = "Black", fg="Green")
        Img.grid(column=0, row=4)
    
        Pag.mainloop()
        
    def AutoDestruct(self, ReponseAAjouter):
        Reponses.append(ReponseAAjouter)
        global NmPage
        NmPage += 1
        Pag.destroy()
    
def Score():
    Score_ = 0
    if Bonus == 1:
        Score_ += 1
    for Rep_ in range(len(Reponses)):
        if Reponses[Rep_] == BonnesReponses[Rep_]:
            Score_ += 1
    global Pag_
    Pag_ = tk.Tk()
    Fram_ = tk.Frame(Pag_, bd = 5, relief = "ridge", bg = "Black")
    Fram_.grid(padx=10, pady=10)
    
    Titr_ = tk.Label(Fram_, text=f"Votre score ! : {Score_}   ||  Et la correction: {BonnesReponses}", bg = "Black", fg="Red")
    Titr_.grid(column=0, row=0)
    
    def Rej():
        Pag_.destroy()
        Transit(ToggleEvents)
    
    Rejouer = tk.Button(Fram_, text="Rejouer ?", bg = "Black", fg="Green", command=lambda:Rej())
    Rejouer.grid(column=0, row=1)
Home(ToggleEvents)