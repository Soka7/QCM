import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Tk, Label
from PIL import Image, ImageTk

import random

from Extracted_QNA import RecupCorr, RecupCorrComp
from question_displayer import display_q
from BttnAesthetics import _on_hover, _on_default

ToggleEvents = False

def Toggle(Bttn):
    """
    Active les events
    """
    global ToggleEvents
    
    ToggleEvents = True
    Bttn.config(bg = "White")

def Home(ToggleEvents):
    """
    Créer le main menu et permet de lancer le porgramme.
    """
    global Bonus
    Bonus = 0

    global Page
    Page = tk.Tk()

    Frame = tk.Frame(Page, bd = 5, relief = "ridge", bg = "Black")
    Frame.grid(padx=10, pady=10)
    
    # Permet d'afficher la présentation en haut de la page d'accueil

    Titre = tk.Label(Frame, text="LE QCM SUR CHUCK NORRIS (LE GOAT) et d autres trucs.", bg = "White", fg="Red")
    Titre.grid(column=0, row=0)
    
    Welcome = tk.Label(Frame, text="Bonjour chers admirateurs du grand CHUCK NORRIS.", bg = "Black", fg="Green")
    Welcome.grid(column=0, row=1)

    Presentation = tk.Label(Frame, text="Le grand CHUCK NORRIS est sans pareil. Saurez vous vous montrer digne d'exister dans un monde ou CHUCK NORRIS a marche ? Decouvrez le dans ce QCM.",
                            bg = "Black", fg="Green")
    Presentation.grid(column=0, row=2)

    global Destroyed
    Destroyed = 0

    Evts = tk.Button(Frame, text="Toggle Events", bg = "Black", fg="Green", command=lambda:Toggle(Evts)) # Créer le boutton pour activer les events
    Evts.grid(column=0, row=4)

    Diff = tk.Entry(Frame, bg = "Black", fg="Green") # Permet de choisir la difficulté avec un input
    Diff.grid(column=0, row=6)

    global NmPage
    NmPage = 0

    def GetEntree(Entree):
        """
        Permet de récupérer ce que l'utilisateur a écrit et le convertit en nombre
        """
        return(int(Entree.get()))

    def GetDiff():
        """
        Transforme  le nombre en index pour determiner la diffculté
        """
        global NmPage

        NmPage = GetEntree(Diff)
        DiffLabel.config(bg = "White")

    DiffLabel = tk.Button(Frame,text="Difficulte +Haut -> +Plus facile ^", bg = "Black", fg="Green", command=GetDiff) # Permet d'enregistrer la diffculté choisie
    DiffLabel.grid(column=0, row=7)

    Start = tk.Button(Frame, text="Prets ?", bg = "Black", fg="Green", command=lambda: Transit(ToggleEvents, 0)) # créer le boutton pour commencer le qcm
    Start.grid(column=0, row=3)

    Start.bind('<Enter>', lambda e: _on_hover(e, "#040444", ("Comic Sans Ms", 28))) # Permet d'avoir un effet quand la souris passe sur le boutton
    Start.bind('<Leave>', lambda e: _on_default(e, "#A6FF00", ("Comic Sans Ms", 16)))

    GS = G_S() # Crée la page du grand sage ainsi que son boutton pour y accéder
    GrandSage = tk.Button(Frame, text="Grand Sage", bg = "Black", fg="Green", command=GS.CreerPage)
    GrandSage.grid(column=0, row=5)
    
    Page.mainloop()

class G_S():
    def __init__(self):
        self.Frame_ = None
        self.image = None
        self.imageGS = None
    
    def CreerPage(self):
        """
        Créer la page du grand sage
        """
        global Pagee

        Pagee = tk.Toplevel()
        self.Frame_ = tk.Frame(Pagee, bd = 5, relief = "ridge", bg = "Black") # relief est un style de fenetre
        self.Frame_.grid()
        
        Titr = tk.Label(self.Frame_, text="Si vous devez demander, jamais vous ne saurez. Si vous savez, il suffit de demander.", bg = "Black", fg="Green")
        Titr.grid(column=0, row=0) # présente le Grand sage

        Entree = tk.Entry(self.Frame_, bg = "Black", fg="Green") # créer une ligne permettant d'écrire du texte
        Entree.grid(column=0, row=1)

        GrandSage = tk.Button(self.Frame_, text="Demander au grand sage", bg = "Black", fg="Green", command=self.AfficherImage) # place l'image montré par le grand sage
        GrandSage.grid(column=0, row=2)
        
        Image_GS = Image.open("GrandSage.webp")
        Image_GS = Image_GS.resize((150, 100))
        self.imageGS = ImageTk.PhotoImage(Image_GS) # Ouvre et redimensionne te rend l'image utilisable par tkinter du grand sage

        ImgGS = tk.Label(self.Frame_, image=self.imageGS, bg = "Black", fg="Green")
        ImgGS.grid(column=0, row=4) # place la dite image
        
        Pagee.mainloop()
        
    def AfficherImage(self):
        """
        Permet de montrer l'image détenu par le grand sage
        """
        Image_ = Image.open("Doigt.jpg")
        Image_ = Image_.resize((400, 400))
        self.image = ImageTk.PhotoImage(Image_)
        Img = tk.Label(self.Frame_, image=self.image, bg = "Black", fg="Green")
        Img.grid(column=0, row=4)
    
def Event():
    """
    Permet d edéfinir ce que font les events, la tranche, la pile et la face de la piece
    """
    global Fini, NmPage

    Message = messagebox.showinfo("Event !", "Pile ou face.")
    Nmbr = random.randint(1, 3)

    if Nmbr == 1: # Force le qcm a recommencé
        Message1 = messagebox.showinfo("Pile", "RECOMMENCEZ LE QCM !")
        Fini = True
        Transit(ToggleEvents)

    elif Nmbr == 2: # incrémente le score de 1 
        Message2 = messagebox.showinfo("Face", "+1 !")
        global Bonus
        Bonus = 1

    elif Nmbr == 3: # Fais crash le programme
        Message2 = messagebox.showinfo("Tranche", "BOOM !")
        Fini = True
        NmPage = None
    
def Transit(ToggleEvents, NombreRej):
    """
    E: si les event sont activale ou non
    E: le nombre de fois rejouer
    permet de passer de la page d'acceuil au qcm
    """
    global Fini, BonnesReponses, Reponses, Destroyed, NmPage
    NumEvent = random.randint(-5,10)

    if Destroyed == 0:
        Page.destroy()

    Destroyed = 1
    Reponses = [] # réinitialise les réponses

    if NombreRej == 0:
        NmPage = 2*NmPage
    else:
        NmPage = 0

    BonnesReponses = RecupCorr(NmPage)
    CallPage(NmPage, NumEvent, BonnesReponses)
                
def CallPage(NmPage, NumEvent, BonnesReponses):
    """
    Appelle la page de la question et y affiche les different reponses et questions
    """
    if NumEvent == NmPage:

        if ToggleEvents == True: # Regarde si un event est activable
            Event()

    if NmPage == len(RecupCorrComp()):
        Score1 = Score()
        Score1.LancerPage()

    else:
        #display_q(NmPage)[0] Question
        #display_q(NmPage)[1] Choix
        #display_q(NmPage)[2]
        #display_q(NmPage)[3]
        Page1 = CreerPageCustom(display_q(NmPage)[0],display_q(NmPage)[1],display_q(NmPage)[2],display_q(NmPage)[3], NumEvent)
        Page1.CreerPage()

class CreerPageCustom:
    
    def __init__(self, Tit, C1, C2, C3, NumEvent):
        self.Tit = Tit #Titre
        self.C1 = C1 #Choix 1, 2, 3
        self.C2 = C2
        self.C3 = C3
        self.NumEvent = NumEvent
        
    def CreerPage(self):
        """
        Créer la page contenant la question et ses réponses ainsi que l'image
        """
        global Pag
        Pag = tk.Tk()
        Fram = tk.Frame(Pag, bd = 5, relief = "ridge", bg = "Black")
        Fram.grid(padx=10, pady=10)
        
        Titr = tk.Label(Fram, text=self.Tit, bg = "Black", fg="Green")
        Titr.grid(column=0, row=0)

        # Chaque choix correspond a une réponse de l'utilisateur grace a lambda qui passe l'argument

        Choix1 = tk.Button(Fram, text=self.C1, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(1))
        Choix1.grid(column=0, row=1)

        Choix2 = tk.Button(Fram, text=self.C2, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(2))
        Choix2.grid(column=0, row=2)

        Choix3 = tk.Button(Fram, text=self.C3, bg = "Black", fg="Green", command=lambda:self.AutoDestruct(3))
        Choix3.grid(column=0, row=3)
        
        Image_ = Image.open("OIP.jpeg")
        Image_ = Image_.resize((100, 100))
        Image_ = ImageTk.PhotoImage(Image_) # Redimensionne oure et rend l'image utilisable par tkinter

        Img = tk.Label(Fram, image=Image_, bg = "Black", fg="Green") # montre l'image
        Img.grid(column=0, row=4)
    
        Pag.mainloop()
        
    def AutoDestruct(self, ReponseAAjouter):
        """
        E: La réponse de l'utilisateur
        detruit la page et ajoute la reponse de la choisie
        """
        Reponses.append(ReponseAAjouter)
        global NmPage
        NmPage += 1
        Pag.destroy()
        CallPage(NmPage, self.NumEvent, BonnesReponses) #Ici on a de la recursivité.
    
class Score:
    def __init__(self):
        self.ImgRef = None
        self.page = None
        self.Frame = None
        
    def LancerPage(self):
        """
        Lance la page de fin du qcm
        """
        Score_ = 0
        if Bonus == 1:
            Score_ += 1 # incrémente le score de 1 si l'event adéquat a été résussit

        for Rep_ in range(len(Reponses)):
            if Reponses[Rep_] == BonnesReponses[Rep_]:
                Score_ += 1 # compte les bonnes réponses en comparant chaque réponse avec la bonne réponse

        self.page = tk.Tk()
        self.Frame = tk.Frame(self.page, bd = 5, relief = "ridge", bg = "Black")
        self.Frame.grid(padx=10, pady=10)
        
        Titr_ = tk.Label(self.Frame, text=f"Votre score ! : {Score_}   ||  Et la correction: {BonnesReponses}", bg = "Black", fg="Red")
        Titr_.grid(column=0, row=0) # Présentation  en haut de la page

        if Score_/len(BonnesReponses) <= 0.1:
            comment = "\n Vous etes lamentable, insecte. "

        elif Score_/len(BonnesReponses) < 0.5:
            comment = "\n Vous etes faible, miserable etre humain. "

        elif Score_/len(BonnesReponses) < 0.7:
            comment = "\n Vous avez eu un score passable. "
        elif Score_/len(BonnesReponses) < 1:
            comment = "\n Vous avez eu un score remarquable ! "
        else:
            comment = "\n Vous avez eu un score parfait, Chuck Norris est tres fier de vous. Good boy."
        
        # Montre un commentaire en fonction du score obtenu

        Comm = tk.Label(self.Frame, text=comment, bg = "Black", fg="Red")
        Comm.grid(column=0, row=1)

        # montre le commentaire
        
        Image_Man = Image.open("Man.jpg")
        Image_Man = Image_Man.resize((400, 400))
        self.ImgRef = ImageTk.PhotoImage(Image_Man) # ouvre, redimensionne et rend l'image utilisable pour tkinter

        Img = tk.Label(self.Frame, image=self.ImgRef, bg = "Black", fg="Green")# montre l'image
        Img.grid(column=0, row=4)
        
        Rejouer = tk.Button(self.Frame, text="Rejouer ?", bg = "Black", fg="Green", command=self.Rej)
        Rejouer.grid(column=0, row=2) # créer le boutton rejouer
    
    def Rej(self):
        """
        Permet de rejouer en recommencant le qcm a 0 et désactivant les events a cause de quelques soucis
        """
        self.page.destroy()
        global ToggleEvents
        ToggleEvents = False
        Transit(ToggleEvents, 1)

Home(ToggleEvents)