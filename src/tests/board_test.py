import unittest
import numpy as np
from board import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        
    def test_create_board(self):
        rows, cols = 6, 7
        board = self.game.create_board(rows, cols)
        self.assertIsInstance(board, np.ndarray)
        self.assertEqual(board.shape, (rows, cols))
        self.assertTrue((board == 0).all())

    def test_drop_piece(self):
        col = 3
        row = 4
        piece = 1
        board = self.game.board
        self.game.drop_piece(board, row, col, piece)
        self.assertEqual(self.game.board[row][col], 1)
        new_col = 1
        new_row = 4
        new_piece = 2
        self.game.drop_piece(board, new_row, new_col, new_piece)
        self.assertEqual(self.game.board[new_row][new_col], 2)


    def test_horizontal_win(self):
        # Test horizontal win for player 1
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 1))
        # Test horizontal win for player 2
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 2, 2, 2],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 2))



    def test_vertical_win(self):
        # Test vertical win for player 1
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 1))
        # Test vertical win for player 2
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 2))

    def test_pos_diagonal_win(self):
        # Test diagonal win for player 1
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0]])
        self.assertTrue(self.game.is_win(board, 1))
        # Test diagonal win for player 2
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0]])
        self.assertTrue(self.game.is_win(board, 2))

    def test_neg_diagonal_win(self):
        # Test diagonal win for player 1
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 1))
        # Test diagonal win for player 2
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0],
                    [0, 2, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(board, 2))

    def test_no_win(self):
        # Test no-win situation
        board = np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 2, 0, 0, 0],
                    [0, 0, 1, 2, 0, 0, 0],
                    [0, 0, 2, 1, 0, 0, 0]])
        self.assertFalse(self.game.is_win(board, 1))
        self.assertFalse(self.game.is_win(board, 2))

    def test_find_empty_row(self):
        # Test finding first empty row in col 1, 3 and 7
        board = np.array([[0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 2, 0, 0, 0],
                    [0, 0, 2, 1, 0, 0, 0],
                    [0, 1, 1, 2, 0, 0, 0],
                    [1, 2, 1, 2, 0, 0, 0],
                    [2, 2, 2, 1, 0, 0, 0]])
        self.assertEqual(self.game.get_empty_row(board, 0), 0)
        self.assertEqual(self.game.get_empty_row(board, 3), None)
        self.assertEqual(self.game.get_empty_row(board, 6), 0)

    def test_drop_piece_full_column(self):
        # Test dropping a piece in a full column
        col = 3
        row = 0
        piece = 1
        board = np.array([[1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0]])
        board_copy = board.copy()
        self.game.drop_piece(board, row, col, piece)
        self.assertFalse(np.array_equal(board, board_copy))


    def test_draw_board(self):
        # create mock game board
        rows, cols = 6, 7
        self.game.create_board(rows, cols)
        self.game.drop_piece(self.game.board, 5, 3, 1)
        self.game.drop_piece(self.game.board, 4, 3, 2)
        self.game.drop_piece(self.game.board, 3, 3, 1)
        self.game.drop_piece(self.game.board, 2, 3, 1)
        self.game.drop_piece(self.game.board, 5, 2, 2)
        self.game.drop_piece(self.game.board, 4, 2, 2)

        # call draw_board method
        screen = self.game.draw_board(self.game.board)
        game = self.game

        # assert that shapes are drawn on the screen as expected
        self.assertTrue(screen.get_at((0, game.HEIGHT - game.square_size)) == game.blue)
        self.assertTrue(screen.get_at((game.square_size // 2, game.HEIGHT - game.square_size // 2)) == game.black)
        self.assertTrue(screen.get_at((0, game.HEIGHT - 2 * game.square_size)) == (0, 0, 255, 255))

        # assert that red and yellow circles are drawn at the correct positions
        self.assertEqual(screen.get_at((game.square_size // 2, game.HEIGHT - 4 * game.square_size // 2)), game.red)  # check for red circle
        self.assertTrue(screen.get_at((2 * game.square_size // 2, game.HEIGHT - 5 * game.square_size // 2)) == game.yellow)  # check for yellow circle
 
    def test_is_valid_col(self):
        # Create an instance of the game board
        board = np.array([[1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0]])
        
        # Test a valid column
        col = 3
        self.assertTrue(self.game.is_valid_col(board, col))
        
        # Test an invalid column (already filled)
        col = 0
        self.assertFalse(self.game.is_valid_col(board, col))

    def test_is_board_full(self):
        # Test if board is full when board is not full
        rows, cols = 6, 7
        self.game.create_board(rows, cols)

        # Almost fill the board

        for i in range(rows-3):
            for j in range(cols):
                self.game.drop_piece(self.game.board, i, j, 1)
        self.assertFalse(self.game.board_is_full(self.game.board))
        # Fill the board
        for i in range(rows):
            for j in range(cols):
                self.game.drop_piece(self.game.board, i, j, 1)
        self.assertTrue(self.game.board_is_full(self.game.board))

