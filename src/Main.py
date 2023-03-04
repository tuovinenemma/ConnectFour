
import pygame
from screen import Screen
from game_loop import GameLoop


def main():
    pygame.init()
    screen = Screen()
    game = GameLoop()
    screen._start_screen()
    game.game_loop()
    screen._end_screen()


if __name__ == "__main__":  
    main()