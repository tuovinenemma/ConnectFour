import numpy as np
import pygame
from pygame.locals import *
import random

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
        self.turn = random.randint(0, 1)
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

    def board_is_full(self):
        for col in range(self.COLS):
            if self.is_valid_col(col):
                return False
        return True


    def draw_board(self, board):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                pygame.draw.rect(self.screen, self.BLUE, (col*self.SQUARE_SIZE, row*self.SQUARE_SIZE+self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                pygame.draw.circle(self.screen, self.BLACK, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, row*self.SQUARE_SIZE+self.SQUARE_SIZE+self.SQUARE_SIZE//2), self.RADIUS)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.RED, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, self.HEIGHT- (row*self.SQUARE_SIZE+self.SQUARE_SIZE//2)), self.RADIUS)

                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.YELLOW, (col*self.SQUARE_SIZE+self.SQUARE_SIZE//2, self.HEIGHT- (row*self.SQUARE_SIZE+self.SQUARE_SIZE//2)), self.RADIUS)

    
    def is_win(self, board, piece):
        return self.check_horizontal_win(board, piece) \
            or self.check_vertical_win(board, piece) \
            or self.check_positive_diagonal_win(board, piece) \
            or self.check_negative_diagonal_win(board, piece)
    
    def check_horizontal_win(self, board, piece):
        """
        Checks if the specified piece has won the game
        :param piece: piece to check (1 or 2)
        :return: True if the piece has won, False otherwise
        """
        for col in range(self.COLS - 3):
            for row in range(self.ROWS):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return True

    def check_vertical_win(self, board, piece):

        for col in range(self.COLS):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return True

    def check_positive_diagonal_win(self, board, piece):

        for col in range(self.COLS - 3):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return True

    def check_negative_diagonal_win(self, board, piece):

        for col in range(self.COLS - 3):
            for row in range(3, self.ROWS):
                if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                    return True