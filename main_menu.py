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

        # Code from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens until config.
        # "%dx%d+%d+%d" is a format string where each %d take a value of the tuple after %
        # Essentially, it creates a 1200x760 window at the center of the screen.

        width : int = 1200
        height : int = 760
        screen_width : int = self.root.winfo_screenwidth()
        screen_height : int = self.root.winfo_screenheight()

        window_x : float = screen_width / 2 - width / 2
        window_y : float = screen_height / 2 - height / 2

        self.root.geometry("%dx%d+%d+%d" % (width, height, window_x, window_y))
        self.root.config(background = "Black")

        self.start_button = Button(self.root, text = "Commencer ?", font = ("Comic Sans MS", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = lambda : self._start_qcm(0, 1))
        self.setting_button = Button(self.root, text = "Paramètres", font = ("Comic Sans Ms", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = self._show_settings)
        self.quit_button = Button(self.root, text = "Quitter", font = ("Comic Sans MS", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = self.root.quit)

    def _show_settings(self) -> None:
        """
        Show and make the settings menu.
        """
        # Same as in __init__ but for a 600 by 800 window.
        width : int = 600
        height : int = 800

        screen_width : int = self.root.winfo_screenwidth()
        screen_height : int = self.root.winfo_screenheight()

        window_x : float = screen_width / 2 - width / 2
        window_y : float = screen_height / 2 - height / 2

        self.root.geometry("%dx%d+%d+%d" % (width, height, window_x, window_y))

        self.start_button.place_forget()
        self.setting_button.place_forget()
        self.quit_button.place_forget()

        self.difficulty_button = Button(self.root, text = "Difficultés", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White")
        self.theme_button = Button(self.root, text = "Thèmes", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White")
        self.language_button = Button(self.root, text = "Langue", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White")
        self.back_button = Button(self.root, text = "Retour", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White")
        
        self.difficulty_button.place(relx = 0.5, rely = 0.15, anchor = "center")
        self.theme_button.place(relx = 0.5, rely = 0.35, anchor = "center")
        self.language_button.place(relx = 0.5, rely = 0.55, anchor = "center")
        self.back_button.place(relx = 0.5, rely = 0.85, anchor = "center")

        return None

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
        self.quit_button.place_forget()

        game = qcm_display(self.root, starting_q - 1, ending_q)
        game.launch()

        return None
    
    def start_game(self) -> None:
        """
        Start the game.
        """

        self.start_button.place(x = 480, y = 410)
        self.setting_button.place(x = 480, y = 510)
        self.quit_button.place(x = 480, y = 610)

        self.root.mainloop()
        return None

d=Main_Menu()
d.start_game()