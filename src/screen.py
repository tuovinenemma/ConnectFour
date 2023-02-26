import sys
import pygame

class Start:

    def __init__(self, clock):

        pygame.init()
        self._clock = clock
        self._width = 700
        self._height = 875
        self._screen = pygame.display.set_mode((self._width, self._height))

    def _end_screen(self):        
        self._end_text2()
        pygame.time.wait(600)
        pygame.display.update()
        self._clock.tick(60)

        

    def _end_text1(self, words, screen, pos, size, colour, font_name, middle=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _end_text2(self):
        self._screen.fill((255, 255, 255))
        self._end_text1('Connect Four', self._screen, [
                        self._width//2, self._height//2-50], 45, (0, 0, 0), 'arial black', middle=True)
