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
        self.game.drop_piece(5, col)
        self.assertEqual(self.game.board[5][col], 1)
        self.game.turn = 1
        self.game.drop_piece(4, col)
        self.assertEqual(self.game.board[4][col], 2)


    def test_horizontal_win(self):
        # Test horizontal win
        self.game.board = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(1))


    def test_vertical_win(self):

        self.game.board = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(1))

    def test_pos_diagonal_win(self):

        self.game.board = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0]])
        self.assertTrue(self.game.is_win(1))

    def test_neg_diagonal_win(self):

        self.game.board = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 0]])
        self.assertTrue(self.game.is_win(1))

    def test_no_win(self):
        self.game.board = np.array([[0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0]])
        self.assertFalse(self.game.is_win(1))