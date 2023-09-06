class Player:
    """Class used to represent the player."""

    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def add_point(self):
        self.score += 1

    def remove_point(self):
        if self.score > 0:
            self.score -= 1
