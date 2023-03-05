import random
import numpy as np
import pygame
from pygame.locals import *

class Game:
    """
    Class that represents the Connect Four game board
    """
    def __init__(self):
        """
        Initializes the game instance with attributes:
        """
        pygame.init()
        self.ROWS = 6
        self.COLS = 7
        self.square_size = 100
        self.WIDTH = self.COLS * self.square_size
        self.HEIGHT = (self.ROWS + 1) * self.square_size
        self.board = self.create_board(self.ROWS, self.COLS)
        self.turn = random.randint(0, 1)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Connect Four")
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.radius = self.square_size//2 - 5
        self.font = pygame.font.SysFont("arial black", 50)
        self.player = 1
        self.ai = 0
        self.empty = 0

    def create_board(self, rows, cols):
        """
        Creates a numpy array of shape (rows, cols) filled with zeros
        :param rows: number of rows
        :param cols: number of columns
        :return: numpy array with shape (rows, cols) filled with zeros
        """
        board = np.zeros((rows, cols))
        return board


    def reset_board(self):
        self.board = self.create_board(self.ROWS, self.COLS)

    def drop_piece(self, board, row, col, piece):
        """
        Drops a piece of the current player (1 or 2) at the specified row and column
        """
        board[row][col] = piece

    def is_valid_col(self, board, col):
        """
        Checks if a column is a valid move
        """
        return board[self.ROWS-1][col] == 0


    def get_empty_row(self, board, col):
        """
        Finds the first empty row in a specified column
        """
        for row in range(self.ROWS):
            if board[row][col] == 0:
                return row

    def print_board(self):
        self.board = np.flip(self.board, 0)
        print(self.board)


    def draw_board(self, board):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                pygame.draw.rect(self.screen, self.blue, (col*self.square_size, row*self.square_size+self.square_size, self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.black, (col*self.square_size+self.square_size//2, row*self.square_size+self.square_size+self.square_size//2), self.radius)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.red, (col*self.square_size+self.square_size//2, self.HEIGHT- (row*self.square_size+self.square_size//2)), self.radius)

                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.yellow, (col*self.square_size+self.square_size//2, self.HEIGHT- (row*self.square_size+self.square_size//2)), self.radius)


    def board_is_full(self):
        """
        Determines whether the game board is full.

        Iterates through each column in the game board, and if any column is not
        full (i.e., has an empty cell), returns False. If all columns are full,
        returns True.
        """
        for col in range(self.COLS):
            if self.is_valid_col(self.board, col):
                return False
        return True


    def is_win(self, board, piece):
        """
        Determines whether a player has won the game.

        Checks for a win by calling helper functions to check for horizontal,
        vertical, positive diagonal, and negative diagonal wins. Returns True
        if any of those functions return True, and False otherwise.
        """
        return self.check_horizontal_win(board, piece) \
            or self.check_vertical_win(board, piece) \
            or self.check_positive_diagonal_win(board, piece) \
            or self.check_negative_diagonal_win(board, piece)

    def check_horizontal_win(self, board, piece):
        """
        Determines whether a player has won with a horizontal line of pieces.

        Iterates through each row and column on the game board, and checks if
        there are four consecutive pieces of the same type in a line.
        Returns True if such a line is found, and False otherwise.
        """

        for col in range(self.COLS - 3):
            for row in range(self.ROWS):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return True

    def check_vertical_win(self, board, piece):
        """
        Determines whether a player has won with a vertical line of pieces.
        """

        for col in range(self.COLS):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return True

    def check_positive_diagonal_win(self, board, piece):
        """
        Determines whether a player has won with a positive diagonal line of pieces.
        """
        for col in range(self.COLS - 3):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return True

    def check_negative_diagonal_win(self, board, piece):
        """
        Determines whether a player has won with a negative diagonal line of pieces.    
        """

        for col in range(self.COLS - 3):
            for row in range(3, self.ROWS):
                if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                    return True
