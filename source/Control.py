import pygame
from utils import disable_mouse, enable_mouse, message_display
from Game import Game
from Player import Player


class Control:
    """
    Control class for entire project. Contains the game loop, and
    the event_loop which passes events to States as needed.
    """

    # Set the window title and icon.
    pygame.display.set_caption("Rock Paper Scissors")
    pygame.display.set_icon(pygame.image.load("assets/rock-paper-scissors.png"))

    # Initialise screen
    pygame.init()

    # Initialise font
    pygame.font.init()

    def __init__(self):
        # Initialise screen
        self.screen = pygame.display.set_mode((1280, 720))

        # Initialise clock
        self.clock = pygame.time.Clock()

        # Initialise font
        self.font = pygame.font.Font(None, 63)

        # Define button size.
        self.button_size = (300, 300)

        # Define player and game objects.
        self.player = Player()
        self.game = Game()

    def did_win(
        self,
        choice: str,
    ) -> None:
        """Check if the player won.
        Args:
            choice (str): player's choice - "r", "p", or "s"
        """
        disable_mouse()
        if self.game.check_for_win(choice):
            self.player.add_point()
            message_display("You won!", "green", self.screen, self.clock)
            enable_mouse()
        elif self.game.check_for_win(choice) is None:
            message_display("It's a tie!", "yellow", self.screen, self.clock)
            enable_mouse()
        else:
            message_display("You lost!", "red", self.screen, self.clock)
            self.player.remove_point()
            enable_mouse()

    def create_button(self, x, y, image) -> pygame.Rect:
        """Create a button.
        Args:
            image (pygame.Surface): image to display on the button

        Returns:
            pygame.Rect: the button
        """
        rect = pygame.Rect(
            x,
            y,
            self.button_size[0],
            self.button_size[1],
        )
        return self.screen.blit(image, rect)

    def event_loop(self, rock_btn, paper_btn, scissors_btn) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                if rock_btn.collidepoint(pos):
                    self.did_win("r")
                if paper_btn.collidepoint(pos):
                    self.did_win("p")
                if scissors_btn.collidepoint(pos):
                    self.did_win("s")

    def run_game(self) -> None:
        """Function used to run the game. Contains the main game loop. \n"""
        # Define the screen center for buttons.
        screen_center_x = self.screen.get_width() / 2 - self.button_size[0] / 2
        screen_center_y = self.screen.get_height() / 2 - self.button_size[0] / 2

        while True:
            # Process player inputs.
            self.screen.fill("purple")

            # Display the buttons.
            rock_btn = self.create_button(
                screen_center_x - self.button_size[0] - 30,
                screen_center_y,
                pygame.image.load("assets/rock.png").convert_alpha(),
            )
            paper_btn = self.create_button(
                screen_center_x,
                screen_center_y,
                pygame.image.load("assets/paper.png").convert_alpha(),
            )
            scissors_btn = self.create_button(
                screen_center_x + self.button_size[0] + 30,
                screen_center_y,
                pygame.image.load("assets/scissors.png").convert_alpha(),
            )

            # Display the player's score
            score_text = self.font.render(
                f"Score: {self.player.get_score()}", True, (255, 255, 255)
            )
            self.screen.blit(score_text, (screen_center_x, 35))

            self.event_loop(rock_btn, paper_btn, scissors_btn)

            # Refresh on-screen display
            pygame.display.flip()

            # wait until next frame (at 60 FPS)
            self.clock.tick(60)
