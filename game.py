# game.py - glue between model and view (very small)
import pygame
from board import UltimateBoard, State

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.board = UltimateBoard()
        self.current_player = 1  # 1 = X, 2 = O
        self.font = pygame.font.SysFont(None, 36)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx,my = event.pos
            b_idx, c_idx = self.pixel_to_cell(mx,my)
            if b_idx is not None:
                if self.board.play(b_idx, c_idx, self.current_player):
                    # switch player
                    self.current_player = 2 if self.current_player == 1 else 1

    def pixel_to_cell(self, x, y):
        # map pixel to (board_index, cell_index)
        margin = 20
        board_size = min(self.width, self.height) - margin*2
        cell_size = board_size / 3
        small_cell = cell_size / 3
        bx = int((x - margin) // cell_size)
        by = int((y - margin) // cell_size)
        if bx < 0 or bx > 2 or by < 0 or by > 2:
            return None, None
        board_index = by*3 + bx
        # inside small board coordinates
        local_x = (x - margin - bx * cell_size)
        local_y = (y - margin - by * cell_size)
        cx = int(local_x // small_cell)
        cy = int(local_y // small_cell)
        cell_index = cy*3 + cx
        return board_index, cell_index

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((30,30,40))
        # draw boards (VERY minimal)
        margin = 20
        board_size = min(self.width, self.height) - margin*2
        cell_size = board_size / 3
        small_cell = cell_size / 3
        for bi in range(9):
            bx = bi % 3
            by = bi // 3
            ox = margin + bx*cell_size
            oy = margin + by*cell_size
            # board background
            pygame.draw.rect(self.screen, (50,50,70), (ox,oy,cell_size,cell_size))
            # small cells
            sb = self.board.boards[bi]
            for ci in range(9):
                cx = ci % 3
                cy = ci // 3
                sx = ox + cx*small_cell
                sy = oy + cy*small_cell
                rect = pygame.Rect(sx+2, sy+2, small_cell-4, small_cell-4)
                pygame.draw.rect(self.screen, (20,20,30), rect)
                val = sb.cells[ci]
                if val != 0:
                    text = "X" if val==1 else "O"
                    surf = self.font.render(text, True, (220,220,220))
                    self.screen.blit(surf, surf.get_rect(center=rect.center))
        # status
        if self.board.meta_state != State.ONGOING:
            s = "Draw" if self.board.meta_state.name=="DRAW" else f"{self.board.meta_state.name} wins!"
            surf = self.font.render(s, True, (255,200,100))
            self.screen.blit(surf, (10,10))