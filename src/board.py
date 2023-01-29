import sys
import numpy as np
import pygame
from pygame.locals import *

class Game:
    """
    Class that represents the Connect Four game
    """
    def __init__(self):
        """
        Initializes the game instance with attributes:
        """
        pygame.init()
        self.ROWS = 6
        self.COLS = 7
        self.board = self.create_board(self.ROWS, self.COLS)
        self.turn = 0
        self.game_over = False
        self.SQUARE_SIZE = 100
        self.WIDTH = self.COLS * self.SQUARE_SIZE
        self.HEIGHT = (self.ROWS + 1) * self.SQUARE_SIZE
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Connect Four")
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.RADIUS = self.SQUARE_SIZE//2 - 5
        self.font = pygame.font.SysFont("arial black", 50)

    def create_board(self, rows, cols):
        """
        Creates a numpy array of shape (rows, cols) filled with zeros
        :param rows: number of rows
        :param cols: number of columns
        :return: numpy array with shape (rows, cols) filled with zeros
        """
        board = np.zeros((rows, cols))
        return board

    def drop_piece(self, row, col):
        """
        Drops a piece of the current player (1 or 2) at the specified row and column
        """
        self.board[row][col] = self.turn + 1

    def is_valid_col(self, col):
        """
        Checks if a column is a valid move
        """
        return self.board[5][col] == 0

    def get_empty_row(self, col):
        """
        Finds the first empty row in a specified column
        """
        for row in range(self.ROWS):
            if self.board[row][col] == 0:
                return row

    def print_board(self):
        self.board = np.flip(self.board, 0)
        print(self.board)

    def is_win(self, piece):
        """
        Checks if the specified piece has won the game
        :param piece: piece to check (1 or 2)
        :return: True if the piece has won, False otherwise
        """
        # Horizontal
        for row in range(self.ROWS):
            for col in range(self.COLS - 3):
                if self.board[row][col] == piece and self.board[row][col+1] == piece and self.board[row][col+2] == piece and self.board[row][col+3] == piece:
                    return True

        # Vertical
        for row in range(self.ROWS - 3):
            for col in range(self.COLS):
                if self.board[row][col] == piece and self.board[row+1][col] == piece and self.board[row+2][col] == piece and self.board[row+3][col] == piece:
                    return True

        # pos diagonal
        for row in range(self.ROWS - 3):
            for col in range(self.COLS - 3):
                if self.board[row][col] == piece and self.board[row+1][col+1] == piece and self.board[row+2][col+2] == piece and self.board[row+3][col+3] == piece:
                    return True


        # neg diagonal
        for row in range(3, self.ROWS):
            for col in range(self.COLS - 3):
                if self.board[row][col] == piece and self.board[row - 1][col + 1] == piece and self.board[row - 2][col + 2] == piece and self.board[row - 3][col + 3] == piece:
                    return True

    def draw_board(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                pygame.draw.rect(self.screen, self.BLUE, (col*self.SQUARE_SIZE, row*self.SQUARE_SIZE+self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                pygame.draw.circle(self.screen, self.BLACK, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, row*self.SQUARE_SIZE+self.SQUARE_SIZE+self.SQUARE_SIZE//2), self.RADIUS)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.RED, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, self.HEIGHT- (row*self.SQUARE_SIZE+self.SQUARE_SIZE//2)), self.RADIUS)

                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.YELLOW, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, self.HEIGHT- (row*self.SQUARE_SIZE+self.SQUARE_SIZE//2)), self.RADIUS)


    def game_loop(self):

        while not self.game_over:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    col = x_pos//self.SQUARE_SIZE


                    if self.turn == 0:
                        if self.is_valid_col(col):
                            row = self.get_empty_row(col)
                            self.drop_piece(row, col)

                            if self.is_win(1):
                                pygame.draw.rect(
                                    self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))
                                won_text = self.font.render(
                                    'Player 1 Won !', True, self.RED)
                                won_rect = won_text.get_rect(
                                    center=(self.WIDTH//2, won_text.get_height()//2))
                                self.screen.blit(won_text, won_rect)
                                self.game_over = True

                            self.turn = 1

                    else:
                        if self.is_valid_col(col):
                            row = self.get_empty_row(col)
                            self.drop_piece(row, col)

                            if self.is_win(2):
                                pygame.draw.rect(
                                    self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))
                                won_text = self.font.render(
                                    'Player 1 Won !', True, self.RED)
                                won_rect = won_text.get_rect(
                                    center=(self.WIDTH//2, won_text.get_height()//2))
                                self.screen.blit(won_text, won_rect)
                                self.game_over = True


                            self.turn = 0


            self.draw_board()
            pygame.display.update()
