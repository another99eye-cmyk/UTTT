# board.py - game model for small board and meta board
from enum import Enum

class State(Enum):
    ONGOING = 0
    X = 1
    O = 2
    DRAW = 3

class SmallBoard:
    def __init__(self):
        self.cells = [0]*9  # 0 empty, 1 X, 2 O
        self.state = State.ONGOING

    def play(self, idx, player):
        if self.cells[idx] != 0 or self.state != State.ONGOING:
            return False
        self.cells[idx] = player
        self._update_state()
        return True

    def _update_state(self):
        lines = [(0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6)]
        for a,b,c in lines:
            if self.cells[a]==self.cells[b]==self.cells[c]!=0:
                self.state = State.X if self.cells[a]==1 else State.O
                return
        if all(c!=0 for c in self.cells):
            self.state = State.DRAW

    def is_full(self):
        return all(c!=0 for c in self.cells)

class UltimateBoard:
    def __init__(self):
        self.boards = [SmallBoard() for _ in range(9)]
        self.meta_state = State.ONGOING
        self.next_board = None  # None = player may pick any unfinished board

    def play(self, board_idx, cell_idx, player):
        sb = self.boards[board_idx]
        if self.next_board is not None and board_idx != self.next_board:
            # not allowed unless forced board full/finished (caller must check)
            return False
        ok = sb.play(cell_idx, player)
        if not ok:
            return False
        # set next_board
        self.next_board = cell_idx
        if self.boards[self.next_board].state != State.ONGOING:
            self.next_board = None
        self._update_meta_state()
        return True

    def _update_meta_state(self):
        # build meta cells: 0 empty, 1 X, 2 O, 3 draw treated as blocked (0)
        meta = [0]*9
        for i, b in enumerate(self.boards):
            if b.state == State.X: meta[i]=1
            elif b.state == State.O: meta[i]=2
        lines = [(0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6)]
        for a,b,c in lines:
            if meta[a]==meta[b]==meta[c]!=0:
                self.meta_state = State.X if meta[a]==1 else State.O
                return
        if all(b.state != State.ONGOING for b in self.boards):
            self.meta_state = State.DRAW