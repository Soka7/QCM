import pandas
from Extracted_QNA import questions

def check_q(question_index : int, answer : int) -> bool:
    """
    Take the index of the question and the answer given.
    Check if the answer given is right or not.
    """

    assert type(question_index) == int, "The index must be an integer."
    assert type(answer) == int, "The answer must be an integer."

    # Add one to the answer since we start from 1 and in python we start from 0.

    if answer == questions.loc[question_index, "Correct Answer"]:
        return True
    else:
        return False
    
