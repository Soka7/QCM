from Extracted_QNA import questions
import pandas as pd

def show_answer(question_index : int) -> int:
    """
    Take the index of the question in argument.
    Return the correct answer of the question.
    """

    assert type(question_index) == int, "The question index must be an intger."

    correct_answer : str = questions.loc[question_index, "Correct Answer"]

    return correct_answer
