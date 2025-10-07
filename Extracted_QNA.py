import pandas as pd

global questions
questions = pd.read_csv("QNA.csv")
def RecupCorr(NumPage):
    global questions
    correct_answer_list : list = []

    for i in range(NumPage, len(questions)):
        correct_answer_list.append(int(questions.loc[i, "Correct Answer"]))
    return correct_answer_list