import sys
import pygame
from board import Game
from minimax import Minimax

class GameLoop:
    """
    A class that manages the game loop and game logic for Connect Four game.
    """
    def __init__(self):
        """
        Initializes the Pygame library, game board, and AI.
        """
        pygame.init()
        self.game = Game()
        self.minimax = Minimax()
        self.game_over = False

    def handle_events(self):
        """
        Handles Pygame events such as quitting the game and player moves.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos = event.pos[0]
                col = x_pos // self.game.square_size
                self.handle_player_move(col)

    def handle_player_move(self, col):
        """
        Updates the game board with the player move and checks for player win or tie.

        Args:
        col (int): the column of the player move.
        """
        if self.game.turn == self.game.player and self.game.is_valid_col(self.game.board, col):
            row = self.game.get_empty_row(self.game.board, col)
            self.game.drop_piece(self.game.board, row, col, 1)
            if self.game.is_win(self.game.board, 1):
                self.game_over = True
                self.show_winner('Player Won !')

            elif self.game.board_is_full(self.game.board):
                self.game_over = True
                self.show_winner("It's a tie !")

            self.game.turn += 1
            self.game.turn = self.game.turn % 2
            self.game.draw_board(self.game.board)

    def handle_ai_move(self):
        """
        Updates the game board with the AI move and checks for AI win or tie.
        """
        if self.game.turn == self.game.ai and not self.game_over:
            col, value = self.minimax.minimax(self.game.board, 5, True)
            if self.game.is_valid_col(self.game.board, col):
                row = self.game.get_empty_row(self.game.board, col)
                self.game.drop_piece(self.game.board, row, col, 2)
                if self.game.is_win(self.game.board, 2):
                    self.game_over = True
                    self.show_winner('AI Won !')

                elif self.game.board_is_full(self.game.board):
                    self.game_over = True
                    self.show_winner("It's a tie !")

                self.game.turn += 1
                self.game.turn = self.game.turn % 2
                self.game.draw_board(self.game.board)

    def show_winner(self, message):
        """
        Shows the winning message on the screen.

        Args:
        message (str): the winning message to be displayed.
        """
        pygame.draw.rect(self.game.screen, self.game.black, (0, 0, self.game.WIDTH, self.game.square_size))
        won_text = self.game.font.render(message, True, self.game.red)
        won_rect = won_text.get_rect(center=(self.game.WIDTH // 2, won_text.get_height() // 2))
        self.game.screen.blit(won_text, won_rect)

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.handle_ai_move()
            self.game.draw_board(self.game.board)
            pygame.display.update()

        pygame.time.wait(3000)
