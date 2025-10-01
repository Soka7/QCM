from tkinter import *
import tkinter as tk
from ui import qcm_display

class Main_Menu():
    def __init__(self):
        """
        Create the main Menu.
        """
        self.root = tk.Tk()
        self.root.title("Multiple Choice Questions")
        self.root.geometry("1200x760")
        self.root.config(background = "Black")

        self.start_button = Button(self.root, text = "Commencer ?", font = ("Comic Sans MS", 24), background = "Black", foreground = "White", command = lambda : self._start_qcm(0, 1))
        self.setting_button = Button(self.root, text = "Paramètres", font = ("Comic Sans Ms", 24), background = "Black", foreground = "White")
        
    def _start_qcm(self, starting_q : int, ending_q : int) -> None:
        """
        Start the QCM at the starting_q until the ending_q.
        """
        # Starting_q - 1 because 1 is added and then the question is displayed.
        # So if it is 0 the first index will be 1 and not 0, resulting in skipping the first question.

        assert type(starting_q) == int, "The index must be an integer."
        assert type(ending_q) == int, "The index must be an integer."

        self.start_button.place_forget()
        self.setting_button.place_forget()

        game = qcm_display(self.root, starting_q - 1, ending_q)
        game.launch()

        return None
    
    def start_game(self) -> None:
        """
        Start the game.
        """

        self.start_button.place(x = 480, y = 410)
        self.setting_button.place(x = 480, y = 510)

        self.root.mainloop()
        return None

d=Main_Menu()
d.start_game()