import pygame


def disable_mouse() -> None:
    """prevents the player from clicking the mouse buttons, used when displaying a message on the screen"""
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)


def enable_mouse() -> None:
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)


def text_objects(text: str, font: str, color: str) -> tuple:
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(
    text: str, color: str, screen: pygame.surface.Surface, clock: pygame.time.Clock
) -> None:
    """Display a message on the screen. The message will disappear after 500ms.\n
    Function will also block the player from clicking the buttons while the message is displayed using the disable_mouse() function. \n
    It's needed because game would continue to run while the message is displayed, and the player could click the buttons and change the score while the message is displayed which led to a bug.

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
