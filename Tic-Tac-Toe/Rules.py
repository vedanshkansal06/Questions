class Rules:
    def __init__(self):
        self.player_1  = True
        self.player_2 = False
        self.game_over = False
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def place_mark(self, row, col):
            if self.is_cell_empty(row, col):
                if self.player_1:
                    self.board[row][col] = True
                    self.player_1 = False
                    self.player_2 = True
                elif self.player_2:
                    self.board[row][col] = False
                    self.player_1 = True
                    self.player_2 = False

    def is_cell_empty(self, row, col):
        cell = self.board[row][col]
        if cell is None:
            return True
        else:
            return False

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        self.game_over = True
        return self.game_over

    def is_winner(self):
        winning_lines =[
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        if ([True, True, True] or [False, False, False]) in winning_lines:
            if [True, True, True] in winning_lines:
                self.player_1 = True
                self.winner = True
                self.game_over = True
                return self.winner, self.game_over
            if [False, False, False] in winning_lines:
                self.player_2 = False
                self.winner = False
                self.game_over = True
                return self.winner, self.game_over
        return self.game_over