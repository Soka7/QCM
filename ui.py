from tkinter import *
import tkinter as tk

from Extracted_QNA import correct_answer_list
from question_checker import check_q
from question_displayer import display_q
from CorrectAnswerDisplayer import show_answer
from Score_handler import Score

class qcm_display():
    def __init__(self, starting_q : int, ending_q : int):

        assert type(starting_q) == int, "The index must be an integer."
        assert type(ending_q) == int, "The index must be an integer."

        self.q_current : float = starting_q
        self.starting_q : int = starting_q
        self.ending_q : int = ending_q

        self.to_display : list = []
        self.score = Score()
        self.answers : list = correct_answer_list

        self.root = tk.Tk()
        self.root.title("Multiple Choice Questions")
        self.root.geometry("800x400")
        self.root.config(background = "Black")

        self.q_display = Label(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
        self.a1_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = lambda : self.next_question(1), state = "normal")
        self.a2_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = lambda : self.next_question(2), state = "normal")
        self.a3_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = lambda : self.next_question(3), state = "normal")
        self.ca_display = Label(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
        self.s_display = Label(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
    
    # The 3 following functions do the same thing, just each one is used fo its appropriate button.

    def button_disabler(self) -> None:
        """
        Disable the buttons.
        """
        # Source from Stack Overflow
        self.a1_display["state"] = "disabled"
        self.a2_display["state"] = "disabled"
        self.a3_display["state"] = "disabled"

        return None

    def next_question(self, answer : int) -> None:
        """
        Show the answer of the question and move to the next one.
        Wait 0.8 second.
        """
        assert type(answer) == int, "The answer must be an integer."

        if check_q(self.q_current, answer):
            self.ca_display["text"] = "Bonne réponse : "
            self.score.update_score(True)
        else:
            self.ca_display["text"] = "Mauvaise réponse ! "
            self.score.update_score(False)

        self.ca_display["text"] += self.to_display[show_answer(self.q_current)]

        self.button_disabler()

        self.ca_display.after(800, self.move_to_next_question)

        return None
    
    def move_to_next_question(self) -> None:
        """
        Move to the next question and erase the answer.
        """
        # Idea to separate the function by ChatGPT

        self.update_question()
        self.ca_display["text"] = ""

        self.a1_display["state"] = "normal"
        self.a2_display["state"] = "normal"
        self.a3_display["state"] = "normal"

        return None


    def update_question(self) -> None:
        """
        Update the question displayed.
        """
        if self.q_current == self.ending_q:
            self.end_screen()
            return None

        self.q_current += 1

        self.to_display : list = display_q(self.q_current)

        self.q_display["text"] = self.to_display[0]
        self.a1_display["text"] = self.to_display[1]
        self.a2_display["text"] = self.to_display[2]
        self.a3_display["text"] = self.to_display[3]
        self.s_display["text"] = "Score : " + str(self.score.score) + " / " + str(self.score.max_score)

        return None

    def end_screen(self) -> None:
        """
        Create and show the ending srceen.
        """
        # Found place_forget() in stack overflow
        self.a1_display.place_forget()
        self.a2_display.place_forget()
        self.a3_display.place_forget()
        self.q_display.place_forget()
        self.ca_display.place_forget()

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

        end_display = Label(self.root, text = "Vous venez d'atteindre la fin de ce QCM." + comment, font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
        end_display.place(x = 380, y = 80, anchor = "center")

        self.s_display["text"] = str(self.score.score) + " sur " + str(self.score.max_score)
        self.s_display.place(x = 380, y = 145, anchor = "center")

        correct_answers_display = Label(self.root, text = "Les bonnes réponses étaient: \n" + str(self.answers), font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
        correct_answers_display.place(x = 380, y = 200, anchor = "center")
        return None

    def _launch(self) -> None :
        """
        Ask for teh first and last question.
        Create the UI and start the Multiple Choice Questions.
        """

        self.update_question()

        self.q_display.place(x = 100, y = 0)
        self.a1_display.place(x = 160, y = 50)
        self.a2_display.place(x = 160, y = 100)
        self.a3_display.place(x = 160, y = 150)
        self.ca_display.place(x = 100, y = 200)
        self.s_display.place(x = 300, y = 300)

        self.root.mainloop()

        return None

# La premiere question commence a -1 et la derniere a nombre de question - 1
p = qcm_display(-1, 9)
p._launch()