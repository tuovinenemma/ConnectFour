import sys
import numpy as np
import pygame
from pygame.locals import *
import random
import math

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
        #return self.board[5][col] == 0
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

    def is_win(self, board, piece):
        """
        Checks if the specified piece has won the game
        :param piece: piece to check (1 or 2)
        :return: True if the piece has won, False otherwise
        """
        # Horizontal
        for col in range(self.COLS - 3):
            for row in range(self.ROWS):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return True

        # Vertical
        for col in range(self.COLS):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return True

        # pos diagonal
        for col in range(self.COLS - 3):
            for row in range(self.ROWS - 3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return True


        # neg diagonal
        for col in range(self.COLS - 3):
            for row in range(3, self.ROWS):
                if board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and board[row - 3][col + 3] == piece:
                    return True
                
    def rate_possible_move(self, possible_move, piece):
        score = 0
        self.opponent = 1
        if piece == 1:
            self.opponent = 2
        if possible_move.count(piece) == 4:
            score += 100
        elif possible_move.count(piece) == 3 and possible_move.count(self.empty) == 1:
            score += 10
        elif possible_move.count(piece) == 2 and possible_move.count(self.empty) == 2:
            score += 5
        if possible_move.count(self.opponent) == 3 and possible_move.count(self.empty) == 1:
            score -= 20
        
        return score


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

    def score(self, board, piece):
        score = 0

        # points for center
        center = [int(i) for i in list(board[:,3])]
        count = center.count(piece)
        score += count * 6
        # hor
        for row in range(self.ROWS):
            r_array = [int(i) for i in list(board[row, :])]
            for col in range(self.COLS -3):
                possible_move = r_array[col:col+4]
                score += self.rate_possible_move(possible_move, piece)

        #ver
        for col in range(self.COLS):
            c_array = [int(i) for i in list(board[:,col])]
            for row in range(self.ROWS-3):
                possible_move = c_array[row:row+4]
                score += self.rate_possible_move(possible_move, piece)

        #diag
        for row in range(self.ROWS-3):
            for col in range(self.COLS-3):
                possible_move = [board[row+i][col+i] for i in range(4)]
                score += self.rate_possible_move(possible_move, piece)

        for row in range(self.ROWS-3):
            for col in range(self.COLS-3):
                possible_move = [board[row+3-i][col+i] for i in range(4)]
                score += self.rate_possible_move(possible_move, piece)



        return score

    def valid_location(self, board):
        valid_locations = []
        for col in range(self.COLS):
            if self.is_valid_col(board, col):
                valid_locations.append(col)
        return valid_locations

    def best_move(self, board, piece):
        valid_locations = self.valid_location(board)
        best_score = -5000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_empty_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score(temp_board, piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col
    def is_terminal(self, board):
        return self.is_win(board, 1) or self.is_win(board, 2) or len(self.valid_location(board)) == 0
    
    def minimax(self, board, depth, maxPlayer):
        valid_locations = self.valid_location(board)
        terminal = self.is_terminal(board)
        if depth == 0 or terminal:
            if terminal:
                if self.is_win(board, 2):
                    return (None, 50000000000000)
                elif self.is_win(board, 1):
                    return (None, -9000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.score(board, 2))
        if maxPlayer:
            value = math.inf
            column = random.choice([i for i in range(self.COLS) if self.is_valid_col(self.board, i)])
            for col in valid_locations:
                row = self.get_empty_row(board, col)
                copy_board = board.copy()
                self.drop_piece(copy_board, row, col, 2)
                new_score = minimax(copy_board, depth-1, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                return column, value
            
        else:
            value = math.inf
            column = random.choice([i for i in range(self.COLS) if self.is_valid_col(self.board, i)])
            for col in valid_locations:
                row = self.get_empty_row(board, col)
                copy_board = board.copy()
                self.drop_piece(copy_board, row, col, 1)
                new_score = minimax(copy_board, depth-1, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                return column, value


    def game_loop(self):

        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    col = x_pos//self.SQUARE_SIZE


                    if self.turn == self.player:
                        if self.is_valid_col(self.board, col):
                            row = self.get_empty_row(self.board, col)
                            self.drop_piece(self.board, row, col, 1)

                            if self.is_win(self.board, 1):
                                pygame.draw.rect(
                                    self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))
                                won_text = self.font.render(
                                    'Player Won !', True, self.RED)
                                won_rect = won_text.get_rect(
                                    center=(self.WIDTH//2, won_text.get_height()//2))
                                self.screen.blit(won_text, won_rect)
                                self.game_over = True

                            self.turn += 1
                            self.turn = self.turn % 2
                            self.draw_board(self.board)


            if self.turn == self.ai and not self.game_over:

                col, minimax_score = self.minimax(self.board, 2, True)

                if self.is_valid_col(self.board, col):
                    pygame.time.wait(600)
                    row = self.get_empty_row(self.board, col)
                    self.drop_piece(self.board, row, col, 2)

                    if self.is_win(self.board, 2):
                        pygame.draw.rect(
                            self.screen, self.BLACK, (0, 0, self.WIDTH, self.SQUARE_SIZE))
                        won_text = self.font.render(
                            'AI Won !', True, self.RED)
                        won_rect = won_text.get_rect(
                            center=(self.WIDTH//2, won_text.get_height()//2))
                        self.screen.blit(won_text, won_rect)
                        self.game_over = True

                    self.draw_board(self.board)
                    self.turn += 1
                    self.turn = self.turn % 2


            self.draw_board(self.board)
            pygame.display.update()
            if self.game_over:
                pygame.time.wait(3000)
