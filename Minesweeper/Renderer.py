from Rules import Rules

class Renderer:
    def __init__(self, rows, cols, mines):
        self.grid = Rules(rows, cols, mines)

    def display_board(self):
        print("-" * 20)
        for col in range(self.grid.cols):
            print(f"  {col}", end = "")
        print()
        for i in self.grid.board:
            print(self.grid.board.index(i), end = " ")
            for j in i:
                if not j.is_revealed:
                    if j.is_flagged:
                        print("F ", end=" ")
                    else:
                        print("* ", end=" ")
                else:
                    if j.is_mine:
                        print("M ", end=" ")
                    elif j.adj_mine == 0:
                        print("  ", end=" ")
                    else:
                        print(j.adj_mine, end="  ")
            print()
        print()

    def play(self):
        self.display_board()
        while not self.grid.game_over:
            try:
                self.instruction()
                userinput = input("Enter Command:").strip().split(" ")
                action, row, col = userinput[0], int(userinput[1]), int(userinput[2])
                if not (0 <= row < self.grid.rows and 0 <= col < self.grid.cols): raise IndexError
                if action == "r":
                    self.grid.reveal(row, col)
                if action == "f":
                    self.grid.mark_cell(row, col)
                self.display_board()
            except IndexError:
                print("Invalid Row or Column")
            except ValueError:
                print("Invalid Format")
        if self.grid.game_won:
            print("Congratulations! You won!")
        else:
            print("Game Over!! You lose!")
    @staticmethod
    def instruction():
        print("For Reveal, Enter 'r row col'.\nFor Flag/Unflag, Enter 'f row col'.")