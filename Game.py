from random import choice as random_choice


class Game:
    valid_options = ["r", "p", "s"]  # r = rock, p = paper, s = scissors
    wins_to = {
        "r": {"s"},  # rock wins against scissors
        "p": {"r"},
        "s": {"p"},
    }

    def get_computer_choice(self) -> str:
        """Method used to get the computer's choice \n
        Returns random element from valid_options list"""
        return random_choice(self.valid_options)

    def check_for_win(self, user_choice: str) -> bool:
        """Method used to check if the player won
        Args:
            user_choice (str): User's choice - "r", "p", or "s"
        Returns:
            bool: determines if the player won or not - (True = win, False = lose, None = tie)
        """
        computer_choice = self.get_computer_choice()
        if user_choice not in self.wins_to[computer_choice]:
            return True
        elif user_choice == computer_choice:
            return None
        return False
