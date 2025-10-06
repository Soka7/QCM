class Score:
    def __init__(self) -> None:
        self.score : int = 0
        self.max_score : int = 0

    def update_score(self, validity : bool) -> None:
        """
        Take a bool being true if the answer is right wrong otherwise.
        Increment max score by one and score by one if validity is true.
        """

        assert type(validity) == bool, "The argument must be a boolean."

        self.max_score += 1

        if validity:
            self.score +=1
        
        return None