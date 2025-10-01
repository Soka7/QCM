from Extracted_QNA import questions
import pandas as pd

correct_answer_list : list = []

def show_answer(question_index : int) -> int:
    """
    Take the index of the question in argument.
    Return the correct answer of the question.
    """

    assert type(question_index) == int, "The question index must be an intger."

    correct_answer : str = questions.loc[question_index, "Correct Answer"]
    correct_answer_list.append(int(correct_answer))

    return correct_answer