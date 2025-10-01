import pandas as pd
from Extracted_QNA import questions

def display_q(question_index : int) -> str:
    """
    Take an index for the question to display.
    Return a tuple containing the question and its answer.
    """

    assert type(question_index) == int, "The index must be a whole positive number."

    to_return : list = []

    # Append the question and its answer to then return it.

    to_return.append(questions.loc[question_index, "Question"])
    to_return.append(questions.loc[question_index, "Answer1"])
    to_return.append(questions.loc[question_index, "Answer2"])
    to_return.append(questions.loc[question_index, "Answer3"])

    return to_return