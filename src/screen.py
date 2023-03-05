import pygame

class Screen:
    """
    A class to represent a Pygame screen for the Connect Four game.
    """
    def __init__(self):
        """
        Initializes a Pygame screen with a set width and height.
        """
        pygame.init()
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))

    def _start_screen(self):
        """
        Displays the starting screen with the game title for 1 second.
        """
        self._start_text()
        pygame.display.update()
        pygame.time.wait(1000)

    def _end_screen(self):
        """
        Displays the ending screen with "Game Over" message for 1 second.
        """
        self._end_text()
        pygame.display.update()
        pygame.time.wait(1000)


    def _text_style(self, words, screen, pos, size, colour, font_name, middle=False):
        """
        Defines the style for Pygame text and renders it on the screen.
        """
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _start_text(self):
        """
        Displays the "Connect Four" game title on the starting screen.
        """
        self._screen.fill((0, 0, 0))
        self._text_style('Connect Four', self._screen, [
                        self._width//2, self._height//2-100], 45, (255, 255, 255), 'arial black', middle=True)


    def _end_text(self):
        """
        Displays the "Game Over" message on the ending screen.
        """
        self._screen.fill((0, 0, 0))
        self._text_style('Game Over', self._screen, [
                        self._width//2, self._height//2-100], 45, (255, 255, 255), 'arial black', middle=True)
