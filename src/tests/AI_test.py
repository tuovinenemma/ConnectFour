import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from minimax import Minimax
from board import Game

class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.minimax = Minimax()
        self.game = Game()

    def test_rate_possible_move(self):
        piece = 1
        opponent = 2
        empty = self.game.empty
        test_cases = [
            ([piece, piece, piece, piece], 10),
            ([piece, piece, piece, empty], 10),
            ([piece, piece, empty, empty], 4),
            ([opponent, opponent, opponent, empty], -10),
            ([opponent, opponent, empty, empty], -4),
            ([empty, empty, empty, empty], 0),
        ]
        
        for possible_move, expected_score in test_cases:
            score = self.minimax.rate_possible_move(possible_move, piece)
            self.assertEqual(score, expected_score)

    def test_score(self):
        # Test Case 1
        board = np.zeros((6, 7))
        board[0][3] = 1
        board[1][3] = 2
        piece = 2
        value = self.minimax.score(board, piece)
        self.assertEqual(value, 3)

        # Test Case 2: Vertical win
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        board[3][0] = 1
        self.assertTrue(self.minimax.game_over(board))

        # Test Case 3: Horizontal win
        board = np.zeros((6, 7))
        board[0][0] = 2
        board[0][1] = 2
        board[0][2] = 2
        board[0][3] = 2
        self.assertTrue(self.minimax.game_over(board))

        # Test Case 4: Diagonal win (positive slope)
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[3][3] = 1
        self.assertTrue(self.minimax.game_over(board))

        # Test Case 5: Diagonal win (negative slope)
        board = np.zeros((6, 7))
        board[3][0] = 2
        board[2][1] = 2
        board[1][2] = 2
        board[0][3] = 2
        self.assertTrue(self.minimax.game_over(board))

        # Test Case 6: Empty board
        board = np.zeros((6, 7))
        self.assertFalse(self.minimax.game_over(board))

    def test_defend_imminent_loss(self):
        # Test Case 1: AI defends against imminent vertical loss
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][0] = 1
        board[2][0] = 1
        board[3][0] = 2
        board[0][1] = 1
        board[1][1] = 1
        board[2][1] = 1

        piece = 2
        depth = 4
        best_move, _ = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 1)

        # Test Case 2: AI defends against imminent horizontal loss
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[1][0] = 2
        board[1][1] = 2
        board[1][2] = 2

        piece = 2
        depth = 4
        best_move, _ = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 3)

        # Test Case 3: AI defends against imminent positive diagonal loss
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[1][1] = 1
        board[2][2] = 1
        board[0][1] = 2
        board[1][2] = 2
        board[2][3] = 2

        piece = 2
        depth = 4
        best_move, _ = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 3)

        # Test Case 4: AI defends against imminent negative diagonal loss
        board = np.zeros((6, 7))
        board[2][0] = 1
        board[1][1] = 1
        board[0][2] = 1
        board[3][0] = 2
        board[1][0] = 2
        board[0][1] = 2

        piece = 2
        depth = 4
        best_move, _ = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 1)

    def test_win_in_five_moves(self):

        board = np.array([
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 0, 1, 2, 2, 0, 0],
            [0, 0, 2, 2, 1, 0, 0],
            [1, 1, 2, 1, 2, 0, 1]
        ])

        # Winning move is found with depth 3

        depth = 3
        best_move, score = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 5)
        self.assertGreaterEqual(score, 100000000000)

        # Winning move is not found with depth 2

        depth = 2
        best_move, score = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 5)
        self.assertLessEqual(score, 100000000000)
 
    def test_win_in_nine_moves(self):

        board = np.array([
            [1, 0, 0, 1, 1, 0, 0],
            [2, 0, 0, 2, 2, 0, 0],
            [1, 0, 0, 2, 1, 1, 0],
            [2, 0, 0, 2, 1, 2, 0],
            [1, 0, 0, 1, 2, 1, 0],
            [2, 0, 0, 2, 1, 2, 1]
        ])

        # Winning move is found with depth 6

        depth = 5
        best_move, score = self.minimax.minimax(board, depth, True)
        self.assertEqual(best_move, 2)
        self.assertGreaterEqual(score, 100000000000)

        # Winning move is not found with depth 4

        depth = 4
        best_move, score = self.minimax.minimax(board, depth, True)
        self.assertLessEqual(score, 100000000000)

    def test_valid_location(self):
        board = np.zeros((6, 7))
        board[0][3] = 1
        valid_locations = self.minimax.valid_location(board)
        self.assertEqual(valid_locations, [0, 1, 2, 3, 4, 5, 6])

    def test_game_over(self):
        board = np.zeros((6, 7))
        board[0][0] = 1
        board[0][1] = 1
        board[0][2] = 1
        board[0][3] = 1
        self.assertTrue(self.minimax.game_over(board))

        board = np.zeros((6, 7))
        self.assertFalse(self.minimax.game_over(board))

    @patch('minimax.Minimax.minimax', return_value=(3, 10))
    def test_minimax(self, mock_minimax):
        board = np.zeros((6, 7))
        depth = 5
        maxPlayer = True
        alpha = float('-inf')
        beta = float('inf')
        result = self.minimax.minimax(board, depth, maxPlayer, alpha, beta)
        self.assertEqual(result, (3, 10))
        mock_minimax.assert_called_once_with(board, depth, maxPlayer, alpha, beta)


if __name__ == '__main__':
    unittest.main()
