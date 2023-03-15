import unittest
from unittest.mock import MagicMock, patch
import pygame
from game_loop import GameLoop
from board import Game
from minimax import Minimax

class TestGameLoop(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game_loop = GameLoop()

    def tearDown(self):
        pygame.quit()

    def test_handle_player_move(self):
        # Test valid move
        self.game_loop.game.turn = self.game_loop.game.player
        self.game_loop.game.is_valid_col = MagicMock(return_value=True)
        self.game_loop.game.get_empty_row = MagicMock(return_value=0)
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock(return_value=True)
        self.game_loop.show_winner = MagicMock()
        self.game_loop.handle_player_move(0)
        self.assertTrue(self.game_loop.game_over)
        self.game_loop.show_winner.assert_called_once_with('Player Won !')

    def test_handle_player_move_invalid_move(self):
        # Test invalid move
        self.game_loop.game.turn = self.game_loop.game.player
        self.game_loop.game.is_valid_col = MagicMock(return_value=False)
        self.game_loop.game.get_empty_row = MagicMock()
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock()
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_player_move(0)
        self.assertFalse(self.game_loop.game_over)
        self.game_loop.game.get_empty_row.assert_not_called()
        self.game_loop.game.drop_piece.assert_not_called()
        self.game_loop.game.is_win.assert_not_called()
        self.game_loop.show_winner.assert_not_called()

    def test_handle_player_move_not_players_turn(self):
        # Test not player's turn
        self.game_loop.game.turn = self.game_loop.game.ai
        self.game_loop.game.is_valid_col = MagicMock()
        self.game_loop.game.get_empty_row = MagicMock()
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock()
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_player_move(0)
        self.assertFalse(self.game_loop.game_over)
        self.game_loop.game.is_valid_col.assert_not_called()
        self.game_loop.game.get_empty_row.assert_not_called()
        self.game_loop.game.drop_piece.assert_not_called()
        self.game_loop.game.is_win.assert_not_called()
        self.game_loop.show_winner.assert_not_called()

    def test_handle_player_move_tie(self):
        # Test tie
        self.game_loop.game.turn = self.game_loop.game.player
        self.game_loop.game.is_valid_col = MagicMock(return_value=True)
        self.game_loop.game.get_empty_row = MagicMock(return_value=0)
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock(return_value=False)
        self.game_loop.game.board_is_full = MagicMock(return_value=True)
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_player_move(0)
        self.assertTrue(self.game_loop.game_over)
        self.game_loop.show_winner.assert_called_once_with("It's a tie !")

    def test_handle_player_move_no_win_no_tie(self):
        # Test no win and no tie
        self.game_loop.game.turn = self.game_loop.game.player
        self.game_loop.game.is_valid_col = MagicMock(return_value=True)
        self.game_loop.game.get_empty_row = MagicMock(return_value=0)
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock(return_value=False)
        self.game_loop.game.board_is_full = MagicMock(return_value=False)
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_player_move(0)
        self.assertFalse(self.game_loop.game_over)
        self.game_loop.show_winner.assert_not_called()

    def test_handle_ai_move(self):
        # Test AI move
        self.game_loop.handle_ai_move()
        self.assertTrue(self.game_loop.game.turn == self.game_loop.game.player or self.game_loop.game_over)

    def test_handle_ai_move_invalid_move(self):
        # Test invalid AI move
        self.game_loop.game.turn = self.game_loop.game.ai
        self.game_loop.minimax.minimax = MagicMock(return_value=(0, 0))
        self.game_loop.game.is_valid_col = MagicMock(return_value=False)
        self.game_loop.game.get_empty_row = MagicMock()
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock()
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_ai_move()

        self.game_loop.game.get_empty_row.assert_not_called()
        self.game_loop.game.drop_piece.assert_not_called()
        self.game_loop.game.is_win.assert_not_called()
        self.game_loop.show_winner.assert_not_called()

    def test_handle_ai_move_win(self):
        # Test AI win
        self.game_loop.game.turn = self.game_loop.game.ai
        self.game_loop.minimax.minimax = MagicMock(return_value=(0, 0))
        self.game_loop.game.is_valid_col = MagicMock(return_value=True)
        self.game_loop.game.get_empty_row = MagicMock(return_value=0)
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock(return_value=True)
        self.game_loop.game.board_is_full = MagicMock()
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_ai_move()

        self.assertTrue(self.game_loop.game_over)
        self.game_loop.show_winner.assert_called_once_with('AI Won !')

    def test_handle_ai_move_tie(self):
        # Test AI move results in a tie
        self.game_loop.game.turn = self.game_loop.game.ai
        self.game_loop.minimax.minimax = MagicMock(return_value=(0, 0))
        self.game_loop.game.is_valid_col = MagicMock(return_value=True)
        self.game_loop.game.get_empty_row = MagicMock(return_value=0)
        self.game_loop.game.drop_piece = MagicMock()
        self.game_loop.game.is_win = MagicMock(return_value=False)
        self.game_loop.game.board_is_full = MagicMock(return_value=True)
        self.game_loop.show_winner = MagicMock()

        self.game_loop.handle_ai_move()

        self.assertTrue(self.game_loop.game_over)
        self.game_loop.show_winner.assert_called_once_with("It's a tie !")


    def test_show_winner(self):
        # Test show winner message
        pygame.init()
        game_loop = GameLoop()
        game_loop.game_over = True
        message = "Test Message"
        result = game_loop.show_winner(message)
        assert type(result) == pygame.Rect

    @patch("sys.exit")
    @patch("pygame.event.get")
    def test_handle_events_quit(self, event_get_mock, sys_exit_mock):
        event = pygame.event.Event(pygame.QUIT)
        event_get_mock.return_value = [event]

        self.game_loop.handle_events()

        sys_exit_mock.assert_called_once()

    @patch("pygame.event.get")
    def test_handle_events_mousebuttondown(self, event_get_mock):
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(100, 100))
        event_get_mock.return_value = [event]

        with patch.object(self.game_loop, "handle_player_move") as handle_player_move_mock:
            self.game_loop.handle_events()

            handle_player_move_mock.assert_called_once_with(1)

    @patch("pygame.event.get")
    def test_handle_events_no_mousebuttondown(self, event_get_mock):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        event_get_mock.return_value = [event]

        with patch.object(self.game_loop, "handle_player_move") as handle_player_move_mock:
            self.game_loop.handle_events()

            handle_player_move_mock.assert_not_called()


if __name__ == '__main__':
    unittest.main()
