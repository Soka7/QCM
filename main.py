import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Tk, Label
import random
from PIL import Image, ImageTk
from Extracted_QNA import correct_answer_list
from question_displayer import display_q

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

    GS = G_S()
    GrandSage = tk.Button(Frame, text="Grand Sage", bg = "Black", fg="Green", command=GS.CreerPage)
    GrandSage.grid(column=0, row=5)
    
    Page.mainloop()

class G_S():
    def __init__(self):
        self.Frame_ = None
        self.image = None
        self.imageGS = None
    
    def CreerPage(self):
        global Pagee
        Pagee = tk.Toplevel()
        self.Frame_ = tk.Frame(Pagee, bd = 5, relief = "ridge", bg = "Black")
        self.Frame_.grid()
        
        Titr = tk.Label(self.Frame_, text="Si vous devez demander, jamais vous ne saurez. Si vous savez, il suffit de demander.", bg = "Black", fg="Green")
        Titr.grid(column=0, row=0)
        Entree = tk.Entry(self.Frame_, bg = "Black", fg="Green")
        Entree.grid(column=0, row=1)
        GrandSage = tk.Button(self.Frame_, text="Demander au grand sage", bg = "Black", fg="Green", command=self.AfficherImage)
        GrandSage.grid(column=0, row=2)
        
        Image_GS = Image.open("GrandSage.webp")
        Image_GS = Image_GS.resize((150, 100))
        self.imageGS = ImageTk.PhotoImage(Image_GS)
        ImgGS = tk.Label(self.Frame_, image=self.imageGS, bg = "Black", fg="Green")
        ImgGS.grid(column=0, row=4)
        
        Pagee.mainloop()
        
    def AfficherImage(self):
        Image_ = Image.open("Doigt.jpg")
        Image_ = Image_.resize((400, 400))
        self.image = ImageTk.PhotoImage(Image_)
        Img = tk.Label(self.Frame_, image=self.image, bg = "Black", fg="Green")
        Img.grid(column=0, row=4)
    
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
    NmPage = 0
    CallPage(NmPage, NumEvent, BonnesReponses)
                
def CallPage(NmPage, NumEvent, BonnesReponses):
    
    if NumEvent == NmPage:
        if ToggleEvents == True:
            Event()
    if NmPage == len(BonnesReponses):
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
        CallPage(NmPage, self.NumEvent, BonnesReponses) #Ici on a de la recursivité.
    
class Score:
    def __init__(self):
        self.ImgRef = None
        self.page = None
        self.Frame = None
        
    def LancerPage(self):
        Score_ = 0
        if Bonus == 1:
            Score_ += 1
        for Rep_ in range(len(Reponses)):
            if Reponses[Rep_] == BonnesReponses[Rep_]:
                Score_ += 1

        self.page = tk.Tk()
        self.Frame = tk.Frame(self.page, bd = 5, relief = "ridge", bg = "Black")
        self.Frame.grid(padx=10, pady=10)
        
        Titr_ = tk.Label(self.Frame, text=f"Votre score ! : {Score_}   ||  Et la correction: {BonnesReponses}", bg = "Black", fg="Red")
        Titr_.grid(column=0, row=0)

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
        
        Comm = tk.Label(self.Frame, text=comment, bg = "Black", fg="Red")
        Comm.grid(column=0, row=1)
        
        Image_Man = Image.open("Man.jpg")
        Image_Man = Image_Man.resize((800, 800))
        self.ImgRef = ImageTk.PhotoImage(Image_Man)
        Img = tk.Label(self.Frame, image=self.ImgRef, bg = "Black", fg="Green")
        Img.grid(column=0, row=4)
        
        Rejouer = tk.Button(self.Frame, text="Rejouer ?", bg = "Black", fg="Green", command=self.Rej)
        Rejouer.grid(column=0, row=2)
    
    def Rej(self):
        self.page.destroy()
        Transit(ToggleEvents)

Home(ToggleEvents)