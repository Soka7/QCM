from tkinter import *
import tkinter as tk

from ui import qcm_display
from Extracted_QNA import sorted_questions

class Main():
    def __init__(self):
        """
        Create the main Menu.
        """

        self.current_menu : list = []

        self.current_difficulty : str = "Default"
        self.current_theme : str = "Fun"

        self.q_to_start : int = sorted_questions[self.current_theme][self.current_difficulty][0]
        self.q_to_end : int = sorted_questions[self.current_theme][self.current_difficulty][1]

        self.root = tk.Tk()
        self.root.title("Multiple Choice Questions")

        # Code from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens until config.
        # "%dx%d+%d+%d" is a format string where each %d take a value of the tuple after %
        # Essentially, it creates a 1200x760 window at the center of the screen.

        self._change_window_size(1200, 760)

        self.root.config(background = "Black")

        self.start_button = Button(self.root, text = "Commencer ?", font = ("Comic Sans MS", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = lambda : self._start_qcm(self.q_to_start, self.q_to_end))
        self.setting_button = Button(self.root, text = "Paramètres", font = ("Comic Sans Ms", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = self._show_settings)
        self.quit_button = Button(self.root, text = "Quitter", font = ("Comic Sans MS", 24), borderwidth = 0, background = "Black",
                                    activebackground = "Black", foreground = "White", command = self.root.quit)
        
    def _change_window_size(self, width : int, height : int) -> None:
        """
        Width and height must be integers.
        Change the window to width by height size.
        """
        
        assert type(width) == int and type(height) == int, "Both arguments must be integers."

        screen_width : int = self.root.winfo_screenwidth()
        screen_height : int = self.root.winfo_screenheight()

        window_x : float = screen_width / 2 - width / 2
        window_y : float = screen_height / 2 - height / 2

        self.root.geometry("%dx%d+%d+%d" % (width, height, window_x, window_y))

        return None
    
    def _change_difficulty(self, difficulty : str) -> None:
        """
        Difficulty is a string.
        Change the difficulty to the set difficulty.
        """
        
        assert type(difficulty) == str, "The difficulty must be a string."

        self.current_difficulty = difficulty

        self.q_to_start = sorted_questions[self.current_theme][difficulty][0]
        self.q_to_end = sorted_questions[self.current_theme][difficulty][1]

        return None
    
    def _change_theme(self, theme : str) -> None:
        """
        Theme is a string.
        Change the theme to the set theme.
        """

        assert type(theme) == str, "The theme argument must be a string."

        self.current_theme = theme

        self.q_to_start = sorted_questions[theme][self.current_difficulty][0]
        self.q_to_end = sorted_questions[theme][self.current_difficulty][1]

        return None
    
    def _go_back(self) -> None:
        """
        Go back to the previous menu.
        """

        if self.current_menu[-1] == "QCM":
            self.game.end_display.place_forget()
            self.game.s_display.place_forget()
            self.game.correct_answers_display.place_forget()
            del self.current_menu[-1]
            self._create_main_menu()

        elif self.current_menu[-1] == "Settings":
            self.difficulty_button.place_forget()
            self.back_button.place_forget()
            self.language_button.place_forget()
            self.theme_button.place_forget()
            del self.current_menu[-1]
            self._create_main_menu()

        elif self.current_menu[-1] == "Difficulties":
            self.easy_button.place_forget()
            self.normal_button.place_forget()
            self.hard_button.place_forget()
            self.lunatic_button.place_forget()
            self.back_button.place_forget()
            del self.current_menu[-1]
            self._show_settings()

        elif self.current_menu[-1] == "Themes":
            self.fun_button.place_forget()
            self.maths_button.place_forget()
            self.chuck_norris_button.place_forget()
            self.geography_button.place_forget()
            self.history_button.place_forget()
            self.video_games_button.place_forget()
            self.general_culture_button.place_forget()
            self.back_button.place_forget()
            del self.current_menu[-1]
            self._show_settings()

        return None 

    def _show_settings(self) -> None:
        """
        Show and make the settings menu.
        """
        # Same as in __init__ but for a 600 by 800 window.

        self.current_menu.append("Settings")

        self._change_window_size(600, 800)

        self.start_button.place_forget()
        self.setting_button.place_forget()
        self.quit_button.place_forget()

        self.difficulty_button = Button(self.root, text = "Difficultés", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White", command = self._show_difficulties)
        self.theme_button = Button(self.root, text = "Thèmes", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White", command = self._show_themes)
        self.language_button = Button(self.root, text = "Langue", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White")
        self.back_button = Button(self.root, text = "Retour", font = ("Comic Sans MS", 24), background = "Black",
                                        activebackground = "Black", borderwidth = 0, foreground = "White", command = self._go_back)
        
        self.difficulty_button.place(relx = 0.5, rely = 0.15, anchor = "center")
        self.theme_button.place(relx = 0.5, rely = 0.35, anchor = "center")
        self.language_button.place(relx = 0.5, rely = 0.55, anchor = "center")
        self.back_button.place(relx = 0.5, rely = 0.85, anchor = "center")

        return None
    
    def _show_difficulties(self) -> None:
        """
        Create and show the difficulty menu.
        """

        self.difficulty_button.place_forget()
        self.back_button.place_forget()
        self.theme_button.place_forget()
        self.language_button.place_forget()

        self.current_menu.append("Difficulties")

        self.easy_button = Button(self.root, text = "Facile", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_difficulty("Easy"))
        self.normal_button = Button(self.root, text = "Normal", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_difficulty("Normal"))
        self.hard_button = Button(self.root, text = "Difficile", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_difficulty("Hard"))
        self.lunatic_button = Button(self.root, text = "Lunatique", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_difficulty("Lunatic"))
        
        self.easy_button.place(relx = 0.5, rely = 0.1, anchor = "center")
        self.normal_button.place(relx = 0.5, rely = 0.25, anchor = "center")
        self.hard_button.place(relx = 0.5, rely = 0.4, anchor = "center")
        self.lunatic_button.place(relx = 0.5, rely = 0.55, anchor = "center")
        self.back_button.place(relx = 0.5, rely = 0.75, anchor = "center")

        return None
    
    def _show_themes(self) -> None:
        """
        Show and create the themes menu.
        """
        self.difficulty_button.place_forget()
        self.back_button.place_forget()
        self.theme_button.place_forget()
        self.language_button.place_forget()

        self.current_menu.append("Themes")

        self.fun_button = Button(self.root, text = "Fun", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("Fun"))
        self.maths_button = Button(self.root, text = "Maths", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("Maths"))
        self.chuck_norris_button = Button(self.root, text = "Chuck Norris", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("Chuck Norris"))
        self.geography_button = Button(self.root, text = "Géographie", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("Geography"))
        self.history_button = Button(self.root, text = "Histoire", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("History"))
        self.video_games_button = Button(self.root, text = "Jeux vidéos", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("Video Games"))
        self.general_culture_button = Button(self.root, text = "Culture générale", font = ("Comic Sans MS", 24), background = "Black",
                                activebackground = "Blue", borderwidth = 0, foreground = "White", command = lambda : self._change_theme("General Culture"))
        
        self.fun_button.place(relx = 0.25, rely = 0.1, anchor = "center")
        self.maths_button.place(relx = 0.75, rely = 0.1, anchor = "center")
        self.chuck_norris_button.place(relx = 0.25, rely = 0.25, anchor = "center")
        self.geography_button.place(relx = 0.75, rely = 0.25, anchor = "center")
        self.history_button.place(relx = 0.25, rely = 0.4, anchor = "center")
        self.video_games_button.place(relx = 0.75, rely = 0.4, anchor = "center")
        self.general_culture_button.place(relx = 0.5, rely = 0.55, anchor = "center")
        self.back_button.place(relx = 0.5, rely = 0.75, anchor = "center")

        return None

    def _start_qcm(self, starting_q : int, ending_q : int) -> None:
        """
        Start the QCM at the starting_q until the ending_q.
        """
        # Starting_q - 1 because 1 is added and then the question is displayed.
        # So if it is 0 the first index will be 1 and not 0, resulting in skipping the first question.

        assert type(starting_q) == int, "The index must be an integer."
        assert type(ending_q) == int, "The index must be an integer."

        self.current_menu.append("QCM")

        self.start_button.place_forget()
        self.setting_button.place_forget()
        self.quit_button.place_forget()

        self.game = qcm_display(self.root, starting_q - 1, ending_q, self._go_back)
        self.game.launch()

        return None
    
    def _create_main_menu(self) -> None:
        """
        Place the main menu.
        """

        self.current_menu.append("Main_menu")

        self._change_window_size(1200, 760)

        self.start_button.place(x = 480, y = 410)
        self.setting_button.place(x = 480, y = 510)
        self.quit_button.place(x = 480, y = 610)

        return None

    def start_game(self) -> None:
        """
        Start the game.
        """

        self._create_main_menu()
        self.root.mainloop()

        return None

d=Main()
d.start_game()