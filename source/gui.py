import pygame
from Game import Game
from Player import Player

# Set the window title and icon.
pygame.display.set_caption("Rock Paper Scissors")
pygame.display.set_icon(pygame.image.load("assets/rock-paper-scissors.png"))


def disable_mouse() -> None:
    """prevents the player from clicking the buttons while the message is displayed"""
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)


def enable_mouse() -> None:
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)


def did_win(
    choice: str,
    player: Player,
    game: Game,
    screen: pygame.surface.Surface,
    clock: pygame.time.Clock,
) -> None:
    """Check if the player won.
    Args:
        choice (str): player's choice - "r", "p", or "s"
    """
    disable_mouse()
    if game.check_for_win(choice):
        player.add_point()
        message_display("You won!", "green", screen, clock)
    elif game.check_for_win(choice) is None:
        message_display("It's a tie!", "yellow", screen, clock)
    else:
        message_display("You lost!", "red", screen, clock)
        player.remove_point()


def text_objects(text: str, font: str, color: str) -> tuple:
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(
    text: str, color: str, screen: pygame.surface.Surface, clock: pygame.time.Clock
) -> None:
    """Display a message on the screen. The message will disappear after 500ms.

    Args:
        text (str): text to display
        color (str): color of the text
    """
    sceneExit = False
    time = 500
    while not sceneExit:
        largeText = pygame.font.Font("freesansbold.ttf", 24)
        TextSurf, TextRect = text_objects(text, largeText, color)
        TextRect.bottomleft = (screen.get_width() / 2, (150))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

        passed_time = clock.tick(60)
        time -= passed_time
        if time <= 0:
            sceneExit = True
            enable_mouse()


def main() -> None:
    """Function used to run the game. Contains the main game loop. \n

    Raises:
        SystemExit: _description_
    """
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))

    # Initialise font
    pygame.font.init()
    font = pygame.font.Font(None, 63)

    # Initialise clock
    clock = pygame.time.Clock()

    # Define button size.
    button_size = (300, 300)

    # Define the screen center.
    screen_center_x = screen.get_width() / 2 - button_size[0] / 2
    screen_center_y = screen.get_height() / 2 - button_size[0] / 2

    # Get images used for the buttons.
    rock_image = pygame.image.load("assets/rock.png").convert_alpha()
    paper_image = pygame.image.load("assets/paper.png").convert_alpha()
    scissors_image = pygame.image.load("assets/scissors.png").convert_alpha()

    player = Player()
    game = Game()
    # Define the buttons.
    scissors = pygame.Rect(
        screen_center_x + button_size[0] + 30,
        screen_center_y,
        button_size[0],
        button_size[1],
    )
    rock = pygame.Rect(
        screen_center_x - button_size[0] - 30,
        screen_center_y,
        button_size[0],
        button_size[1],
    )
    paper = pygame.Rect(
        screen_center_x,
        screen_center_y,
        button_size[0],
        button_size[1],
    )

    while True:
        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                if rock_btn.collidepoint(pos):
                    did_win("r", player, game, screen, clock)
                if paper_btn.collidepoint(pos):
                    did_win("p", player, game, screen, clock)
                if scissors_btn.collidepoint(pos):
                    did_win("s", player, game, screen, clock)
        screen.fill("purple")

        # Display the player's score.
        score_text = font.render(f"Score: {player.get_score()}", True, (255, 255, 255))
        screen.blit(score_text, (screen_center_x, 35))

        # Display the buttons.
        rock_btn = screen.blit(rock_image, rock)
        paper_btn = screen.blit(source=paper_image, dest=paper)
        scissors_btn = screen.blit(scissors_image, scissors)

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)  # wait until next frame (at 60 FPS)
