from math import inf
import random
from board import Game

class Minimax:
    """
    A class representing a player using the Minimax algorithm to play a Connect Four game.
    """
    def __init__(self):
        """
        Initializes a new Minimax player object.
        """
        self.game = Game()
        self.max_score = 1000000000000
        self.min_score = -100000000000

    def rate_possible_move(self, possible_move, piece):
        """
        Rates a possible move based on its value to the current player.

        Args:
            possible_move (list): A list of integers representing a possible move in the game.
            piece (int): An integer representing the current player's piece.

        Returns:
            score (int): An integer representing the score of the possible move.
        """
        score = 0
        self.opponent = 1
        if piece == 1:
            self.opponent = 2
        if possible_move.count(piece) == 4:
            score += 10
        elif possible_move.count(piece) == 3 and possible_move.count(self.game.empty) == 1:
            score += 10
        elif possible_move.count(piece) == 2 and possible_move.count(self.game.empty) == 2:
            score += 4
        if possible_move.count(self.opponent) == 3 and possible_move.count(self.game.empty) == 1:
            score -= 10
        if possible_move.count(self.opponent) == 2 and possible_move.count(self.game.empty) == 2:
            score -= 4

        return score

    def score(self, board, piece):
        """
        Computes the score of the current board position for a given player.

        Args:
            board (numpy.ndarray): A 2D numpy array representing the current board state.
            piece (int): An integer representing the current player's piece.

        Returns:
            value (int): An integer representing the score of the board position for the given player.
        """
        value = 0

        # points for center
        center = [int(i) for i in list(board[:, 3])]
        count = center.count(piece)
        value += count * 3

        # hor
        for row in range(self.game.ROWS):
            r_array = [int(i) for i in list(board[row, :])]
            for col in range(self.game.COLS -3):
                possible_move = r_array[col:col+4]

                value += self.rate_possible_move(possible_move, piece)

        #ver
        for col in range(self.game.COLS):
            c_array = [int(i) for i in list(board[:, col])]
            for row in range(self.game.ROWS-3):
                possible_move = c_array[row:row+4]

                value += self.rate_possible_move(possible_move, piece)

        #positive diag
        for row in range(self.game.ROWS-3):
            for col in range(self.game.COLS-3):
                possible_move = [board[row+i][col+i] for i in range(4)]

                value += self.rate_possible_move(possible_move, piece)

        #negative diag
        for row in range(self.game.ROWS-3):
            for col in range(self.game.COLS-3):
                possible_move = [board[row+3-i][col+i] for i in range(4)]

                value += self.rate_possible_move(possible_move, piece)

        return value

    def valid_location(self, board):
        """
        Returns a list of valid locations on the board where a piece can be placed.

        Parameters:
        board (list): A 2D list representing the current state of the board.

        Returns:
        valid_locations (list): A list of column indices where a piece can be placed.
        """
        valid_locations = []
        for col in range(self.game.COLS):
            if self.game.is_valid_col(board, col):
                valid_locations.append(col)
        return valid_locations


    def game_over(self, board):
        """
        Returns True if the game is over, either due to a player winning or the board being full.

        Parameters:
        board (list): A 2D list representing the current state of the board.

        Returns:
        (bool): True if the game is over, False otherwise.
        """
        return self.game.is_win(board, 1) or self.game.is_win(board, 2) or len(self.valid_location(board)) == 0

    def minimax(self, board, depth, maxPlayer, alpha=-inf, beta=inf):
        """
        Returns the best move for the AI player using the minimax algorithm with alpha-beta pruning.

        Parameters:
        board (list): A 2D list representing the current state of the board.
        depth (int): The depth of the search tree.
        maxPlayer (bool): True if the AI player is making the move, False otherwise.
        alpha (int): The maximum lower bound of possible solutions.
        beta (int): The minimum upper bound of possible solutions.

        Returns:
        column (int): The column index where the AI player should drop a piece.
        max_value/min_value (int): The score associated with the column, indicating how good the move is for the AI player.
        """
        valid_locations = self.valid_location(board)
        game_over = self.game_over(board)

        if self.game.board_is_full(self.game.board):
            return (None, 0)
        
        if not valid_locations:
            return None, 0

        if depth == 0 or game_over:

            if game_over:
                if self.game.is_win(board, 2):
                    return (None, self.max_score)
                if self.game.is_win(board, 1):
                    return (None, self.min_score)
            else:
                return (None, self.score(board, 2))

        if maxPlayer: # ai player
            max_value = -inf
            column = random.choice([i for i in range(self.game.COLS) if self.game.is_valid_col(board, i)])

            for col in valid_locations:
                row = self.game.get_empty_row(board, col)
                copy_board = board.copy()
                self.game.drop_piece(copy_board, row, col, 2)
                new_score = self.minimax(copy_board, depth-1, False, alpha, beta)[1]

                if new_score > max_value:
                    max_value = new_score
                    column = col

                alpha = max(alpha, max_value)
                if alpha >= beta:
                    break

            return column, max_value

        else:
            min_value = inf
            column = random.choice([i for i in range(self.game.COLS) if self.game.is_valid_col(board, i)])

            for col in valid_locations:
                row = self.game.get_empty_row(board, col)
                copy_board = board.copy()
                self.game.drop_piece(copy_board, row, col, 1)
                new_score = self.minimax(copy_board, depth-1, True, alpha, beta)[1]

                if new_score < min_value:
                    min_value = new_score
                    column = col

                beta = min(beta, min_value)
                if alpha >= beta:
                    break

            return column, min_value
