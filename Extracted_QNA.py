import pandas as pd

questions = pd.read_csv("QNA.csv")
correct_answer_list : list = []

for i in range(len(questions)):
    correct_answer_list.append(int(questions.loc[i, "Correct Answer"]))
