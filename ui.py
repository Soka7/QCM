from tkinter import *
import tkinter as tk

from Extracted_QNA import correct_answer_list
from question_checker import check_q
from question_displayer import display_q
from CorrectAnswerDisplayer import show_answer
from Score_handler import Score

class Ui():
    def __init__(self):
        self.q_current : float = -1
        self.to_display : list = []
        self.score = Score()
        self.answers : list = correct_answer_list

        self.root = tk.Tk()
        self.root.title("Multiple Choice Questions")
        self.root.geometry("800x400")
        self.root.config(background = "Black")

        self.q_display = Label(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White")
        self.a1_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = self.next_question1, state = "normal")
        self.a2_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = self.next_question2, state = "normal")
        self.a3_display = Button(self.root, text = "", font = ("Comic Sans MS", 16), background = "Black", foreground = "White", command = self.next_question3, state = "normal")
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

    def next_question1(self) -> None:
        """
        Show the answer of the question and move to the next one.
        Wait 0.8 second.
        """

        answer : int = 1

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
    
    def next_question2(self) -> None:
        """
        Show the answer of the question and move to the next one.
        Wait 0.8 second.
        """

        answer : int = 2

        if check_q(self.q_current, answer):
            self.ca_display["text"] = "Bonne réponse : "
            self.score.update_score(True)
        else:
            self.ca_display["text"] = "Mauvaise réponse ! "
            self.score.update_score(False)

        self.button_disabler()

        self.ca_display["text"] += self.to_display[show_answer(self.q_current)]

        self.ca_display.after(800, self.move_to_next_question)

        return None
    
    def next_question3(self) -> None:
        """
        Show the answer of the question and move to the next one.
        Wait 0.8 second.
        """

        answer : int = 3

        if check_q(self.q_current, answer):
            self.ca_display["text"] = "Bonne réponse : "
            self.score.update_score(True)
        else:
            self.ca_display["text"] = "Mauvaise réponse ! "
            self.score.update_score(False)

        self.button_disabler()

        self.ca_display["text"] += self.to_display[show_answer(self.q_current)]

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
        self.q_current += 1

        self.to_display : list = display_q(self.q_current)

        self.q_display["text"] = self.to_display[0]
        self.a1_display["text"] = self.to_display[1]
        self.a2_display["text"] = self.to_display[2]
        self.a3_display["text"] = self.to_display[3]
        self.s_display["text"] = "Score : " + str(self.score.score) + " / " + str(self.score.max_score)

        return None

    def _launch(self) -> None :
        """
        Create the UI and start the Multiple Choice Questions.
        """

        self.update_question()

        self.q_display.place(x = 100, y = 0)
        self.a1_display.place(x = 120, y = 50)
        self.a2_display.place(x = 120, y = 100)
        self.a3_display.place(x = 120, y = 150)
        self.ca_display.place(x = 100, y = 200)
        self.s_display.place(x = 300, y = 300)

        self.root.mainloop()

        return None

p = Ui()
p._launch()