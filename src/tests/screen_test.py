import unittest
from unittest.mock import MagicMock, patch
import pygame
from screen import Screen

class TestScreen(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = Screen()

    def tearDown(self):
        pygame.quit()

    @patch('pygame.display.update')
    @patch('pygame.time.wait')
    def test_start_screen(self, mock_wait, mock_update):
        self.screen._start_text = MagicMock()
        self.screen._start_screen()
        self.screen._start_text.assert_called_once()
        mock_update.assert_called_once()
        mock_wait.assert_called_once_with(1000)

    @patch('pygame.display.update')
    @patch('pygame.time.wait')
    def test_end_screen(self, mock_wait, mock_update):
        self.screen._end_text = MagicMock()
        self.screen._end_screen()
        self.screen._end_text.assert_called_once()
        mock_update.assert_called_once()
        mock_wait.assert_called_once_with(1000)

    @patch('screen.Screen._text_style')
    def test_start_text(self, mock_text_style):
        self.screen._start_text()
        mock_text_style.assert_called_with(
            'Connect Four',
            self.screen._screen,
            [self.screen._width // 2, self.screen._height // 2 - 100],
            45,
            (255, 255, 255),
            'arial black',
            middle=True
        )

    @patch('screen.Screen._text_style')
    def test_end_text(self, mock_text_style):
        self.screen._end_text()
        mock_text_style.assert_called_with(
            'Game Over',
            self.screen._screen,
            [self.screen._width // 2, self.screen._height // 2 - 100],
            45,
            (255, 255, 255),
            'arial black',
            middle=True
        )

if __name__ == '__main__':
    unittest.main()
