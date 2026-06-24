from Rules import Rules
class Render:
    def __init__(self):
        self.grid = Rules()

    def display_board(self):
        if not self.grid.game_over:
            print("-" * 20)
            for col in range(3):
                print(f" {col}", end = "  ")
            print()
            for row in range(3):
                print(f"{row}", end = "|")
                for col in range(3):
                    cell = self.grid.board[row][col]
                    if cell is None:
                        print("_ ", end = "|")
                    elif cell:
                        print("O ", end = "|")
                    else:
                        print("X ", end = "|")
                print()
            print()

    @staticmethod
    def instruction():
        print("Enter 'row col' to mark the cell.")

    @staticmethod
    def input_handling():
        while True:
            try:
                user_input = input("Enter your choice: ").strip().split()
                row, col = int(user_input[0]), int(user_input[1])
                if not(0 <= row < 3 and 0 <= col < 3): raise IndexError
                return row, col
            except IndexError:
                print("Invalid Index")
            except ValueError:
                print("Invalid Input")



    def play(self):
        self.display_board()
        while not self.grid.game_over:
            self.instruction()
            row, col = self.input_handling()
            if self.grid.is_cell_empty(row, col):
                self.grid.place_mark(row, col)
                self.display_board()
                if self.grid.is_winner():
                    if self.grid.winner:
                        print("Player 1 won!")
                    elif  not self.grid.winner:
                        print("Player 2 won!")
                elif self.grid.is_full():
                    print("The game has ended in a Draw.")
            else:
                print("Invalid Input")