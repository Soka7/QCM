from tkinter import *
import tkinter as tk

from Extracted_QNA import correct_answer_list
from question_displayer import display_q
from CorrectAnswerDisplayer import show_answer
from Score_handler import Score

class qcm_display():
    def __init__(self, root, starting_q : int, ending_q : int, on_finish = None):
        """
        Take the first and last question of the QCM in arguments.
        """

        # The on_finish idea was made by Chatgpt, I thought of it but I couldn't make it work myself.

        assert type(starting_q) == int, "The index must be an integer."
        assert type(ending_q) == int, "The index must be an integer."

        self.root = root

        self.q_current : float = starting_q
        self.starting_q : int = starting_q
        self.ending_q : int = ending_q
        self.on_finish = on_finish

        self.to_display : list = []
        self.score = Score()
        self.answers : list = correct_answer_list

        self.q_display = Label(self.root, text = "", font = ("Comic Sans MS", 20), background = "Black", foreground = "White", wraplength = 800)
        self.a1_display = Button(self.root, text = "", font = ("Comic Sans MS", 20), background = "Black", borderwidth = 0,
                                 activebackground = "Black", foreground = "White", wraplength = 600,
                                 command = lambda : self._next_question(1), state = "normal")
        self.a2_display = Button(self.root, text = "", font = ("Comic Sans MS", 20), background = "Black", borderwidth = 0,
                                 activebackground = "Black", foreground = "White", wraplength = 600,
                                 command = lambda : self._next_question(2), state = "normal")
        self.a3_display = Button(self.root, text = "", font = ("Comic Sans MS", 20), background = "Black", borderwidth = 0,
                                 activebackground = "Black", foreground = "White", wraplength = 600, 
                                 command = lambda : self._next_question(3), state = "normal")
        self.ca_display = Label(self.root, text = "", font = ("Comic Sans MS", 20), background = "Black", foreground = "White", wraplength = 800)
        self.s_display = Label(self.root, text = "", font = ("Comic Sans MS", 24), background = "Black", foreground = "White")

    def _button_disabler(self) -> None:
        """
        Disable the buttons.
        """
        # Source from Stack Overflow
        self.a1_display["state"] = "disabled"
        self.a2_display["state"] = "disabled"
        self.a3_display["state"] = "disabled"

        return None

    def _next_question(self, answer : int) -> None:
        """
        Show the answer of the question and move to the next one.
        Wait 0.8 second.
        """
        assert type(answer) == int, "The answer must be an integer."

        if answer == self.answers[self.q_current]:
            self.ca_display["text"] = "Bonne réponse : "
            self.score.update_score(True)
        else:
            self.ca_display["text"] = "Mauvaise réponse ! "
            self.score.update_score(False)

        self.ca_display["text"] += self.to_display[show_answer(self.q_current)]

        self._button_disabler()

        self.ca_display.after(800, self._move_to_next_question)

        return None
    
    def _move_to_next_question(self) -> None:
        """
        Move to the next question and erase the answer.
        """
        # Idea to separate the function by ChatGPT

        self._update_question()
        self.ca_display["text"] = ""

        self.a1_display["state"] = "normal"
        self.a2_display["state"] = "normal"
        self.a3_display["state"] = "normal"

        return None


    def _update_question(self) -> None:
        """
        Update the question displayed.
        """
        if self.q_current == self.ending_q:
            self._end_screen()
            return None
        
        self.q_current += 1

        self.to_display : list = display_q(self.q_current)

        self.q_display["text"] = self.to_display[0]
        self.a1_display["text"] = self.to_display[1]
        self.a2_display["text"] = self.to_display[2]
        self.a3_display["text"] = self.to_display[3]
        self.s_display["text"] = "Score : " + str(self.score.score) + " / " + str(self.score.max_score)

        return None

    def _end_screen(self) -> None:
        """
        Create and show the ending srceen.
        """
        # Found place_forget() in stack overflow
        self.a1_display.place_forget()
        self.a2_display.place_forget()
        self.a3_display.place_forget()
        self.q_display.place_forget()
        self.ca_display.place_forget()

        self.on_end_sceen : bool = True

        comment : str = ""

        if self.score.score / self.score.max_score <= 0.1:
            comment = "\n Vous avez eu le score lamentable de : "

        elif self.score.score / self.score.max_score < 0.5:
            comment = "\n Vous avez eu le faible score de : "

        elif self.score.score / self.score.max_score < 0.7:
            comment = "\n Vous avez eu un score passable de : "
        elif self.score.score / self.score.max_score < 1:
            comment = "\n Vous avez eu un score remarquable de : "
        else:
            comment = "\n Vous avez eu un score parfait, Chuck Norris vous en félicite."

        self.end_display = Label(self.root, text = "Vous venez d'atteindre la fin de ce QCM." + comment, font = ("Comic Sans MS", 22),
                            background = "Black", foreground = "White")
        self.end_display.place(relx = 0.5, rely = 0.4, anchor = "center")

        self.s_display["text"] = str(self.score.score) + " sur " + str(self.score.max_score)
        self.s_display.place(relx = 0.5, rely = -0.1, anchor = "center")

        # Add 1 to both because otherwise the last element isn't show and if the start is -1 which is the right start, it will be 0 and not the last element.
        self.correct_answers_display = Label(self.root, text = "Les bonnes réponses étaient: \n" + str(self.answers[self.starting_q + 1 : self.ending_q + 1]),
                                        font = ("Comic Sans MS", 20), background = "Black", foreground = "White")
        self.correct_answers_display.place(relx = 0.5, rely = 0.6, anchor = "center")
        self.correct_answers_display.after(3000, self.on_finish)

        return None

    def launch(self) -> None :
        """
        Ask for teh first and last question.
        Create the UI and start the Multiple Choice Questions.
        """

        self._update_question()

        self.q_display.place(relx = 0.5, y = 50, anchor = "center")
        self.a1_display.place(relx = 0.1, y = 100, anchor = "nw")
        self.a2_display.place(relx = 0.1, y = 200, anchor = "nw")
        self.a3_display.place(relx = 0.1, y = 300, anchor = "nw")
        self.ca_display.place(relx = 0.5, y = 525, anchor = "center")
        self.s_display.place(relx = 0.5, y = 450, anchor = "center")

        return None

# La premiere question commence a -1 et la derniere a nombre de question - 1
