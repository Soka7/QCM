import pandas as pd

questions = pd.read_csv("QNA.csv")
correct_answer_list : list = []

for i in range(len(questions)):
    correct_answer_list.append(int(questions.loc[i, "Correct Answer"]))

sorted_questions : dict = {
    "Fun" : {
        "Easy" : (0, 11),
        "Normal" : (0, 11),
        "Hard" : (0, 11),
        "Lunatic" : (0, 11),
        "Default" : (0, 11)
    },
    "Maths" : {
        "Easy" : (12, 21),
        "Normal" : (22, 31),
        "Hard" : (32, 41),
        "Lunatic" : (42, 51),
        "Default" : (22, 31)
    },
    "Geography" : {
        "Easy" : (52, 61),
        "Normal" : (62, 71),
        "Hard" : (72, 81),
        "Lunatic" : (82, 91),
        "Default" : (62, 71)
    },
    "History" : {
        "Easy" : (92, 101),
        "Normal" : (102, 111),
        "Hard" : (112, 121),
        "Lunatic" : (122, 131),
        "Default" : (102, 111)
    },
    "Video Games" : {
        "Easy" : (132, 141),
        "Normal" : (142, 151),
        "Hard" : (152, 161),
        "Lunatic" : (162, 171),
        "Default" : (142, 151)
    },
    "General Culture" : {
        "Easy" : (172, 181),
        "Normal" : (182, 191),
        "Hard" : (192, 201),
        "Lunatic" : (202, 211),
        "Default" : (182, 191)
    },
}
