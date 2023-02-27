import pygame
import sys
from board import Game
from minimax import Minimax
class GameLoop:
    def __init__(self):
        
        pygame.init()
        self.game = Game()
        self.minimax = Minimax()
        self.game_over = False


    
    def game_loop(self):

        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    col = x_pos//self.game.SQUARE_SIZE


                    if self.game.turn == self.game.player:
                        if self.game.is_valid_col(self.game.board, col):
                            row = self.game.get_empty_row(self.game.board, col)
                            self.game.drop_piece(self.game.board, row, col, 1)

                            if self.minimax.is_win(self.game.board, 1):
                                pygame.draw.rect(
                                    self.game.screen, self.game.BLACK, (0, 0, self.game.WIDTH, self.game.SQUARE_SIZE))
                                won_text = self.font.render(
                                    'Player Won !', True, self.game.RED)
                                won_rect = won_text.get_rect(
                                    center=(self.WIDTH//2, won_text.get_height()//2))
                                self.game.screen.blit(won_text, won_rect)
                                self.game_over = True

                            self.game.turn += 1
                            self.game.turn = self.game.turn % 2
                            self.game.draw_board(self.game.board)


            if self.game.turn == self.game.ai and not self.game_over:

                col, value = self.minimax.minimax(self.game.board, 3, True)

                if self.game.is_valid_col(self.game.board, col):
                    row = self.game.get_empty_row(self.game.board, col)
                    self.game.drop_piece(self.game.board, row, col, 2)

                    if self.minimax.is_win(self.game.board, 2):
                        pygame.draw.rect(
                            self.game.screen, self.game.BLACK, (0, 0, self.game.WIDTH, self.game.SQUARE_SIZE))
                        won_text = self.game.font.render(
                            'AI Won !', True, self.game.RED)
                        won_rect = won_text.get_rect(
                            center=(self.game.WIDTH//2, won_text.get_height()//2))
                        self.game.screen.blit(won_text, won_rect)
                        self.game_over = True

                    self.game.draw_board(self.game.board)
                    self.game.turn += 1
                    self.game.turn = self.game.turn % 2

            self.game.draw_board(self.game.board)
            pygame.display.update()
            if self.game_over:
                pygame.time.wait(3000)