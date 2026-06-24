import random

from Cell import Cell

class Rules:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)] # Defines The Board
        self.isFirstMove = True # Game-state
        self.game_over = False  # Game-state
        self.game_won = False   # Game-state
        self.safe_cells = rows * cols - mines

    def mine_placement(self, row, col):
        if self.mines < self.rows * self.cols:
            if self.isFirstMove:
                self.isFirstMove = False
                # mine_placed = 0
                # while mine_placed < self.mines:
                #     r = random.randint(0, self.rows - 1)
                #     c = random.randint(0, self.cols - 1)
                #     if (r != row or c != col) and not self.board[r][c].is_mine:
                #         self.board[r][c].is_mine = True
                #         mine_placed += 1
                available_spaces = [(r, c) for r in range(self.rows) for c in range(self.cols) if (r, c) != (row, col)]
                mine_locations = random.sample(available_spaces, self.mines)
                for r, c in mine_locations:
                    self.board[r][c].is_mine = True
            self._count_all_adjacent_mines()

    def _adjacent_mines(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if ((0 <= row + i < self.rows and 0 <= col + j < self.cols)
                        and self.board[row + i][col + j].is_mine):
                    count += 1
        return count

    def _count_all_adjacent_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.board[row][col].is_mine:
                    self.board[row][col].adj_mine = self._adjacent_mines(row, col)

    def reveal(self, row, col):
        if self.game_over or not (0 <= row < self.rows) or not (0 <= col < self.cols):
            return True
        if self.isFirstMove:
            self.mine_placement(row, col)
            self.isFirstMove = False
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            cell = self.board[r][c]
            if cell.is_revealed or cell.is_flagged:
                continue
            cell.is_revealed = True
            if cell.is_mine:
                self.game_over = True
                return False
            if cell.adj_mine == 0:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= r+ i < self.rows and 0 <= c + j < self.cols:
                            stack.append((r + i, c + j))
            if not cell.is_mine: self.safe_cells -= 1
        self.win_condition()
        return True

    def mark_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            cell = self.board[row][col]
            if not cell.is_revealed and not cell.is_flagged:
                cell.is_flagged = True
            elif cell.is_flagged and not cell.is_revealed:
                cell.is_flagged = False

    def win_condition(self):
        # for r in range(self.rows):
        #     for c in range(self.cols):
        #         cell = self.board[r][c]
        #         if not cell.is_mine and not cell.is_revealed:
        #             return True
        if self.safe_cells == 0:
            self.game_over = True
            self.game_won = True