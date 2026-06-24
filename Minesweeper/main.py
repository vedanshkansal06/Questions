from Renderer import Renderer

def main():
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            mines = int(input("Enter the number of mines: "))
            if mines >= rows * cols: raise ValueError("Too many mines")
            game = Renderer(rows, cols, mines)
            game.play()
            try:
                replay = input("Do you want to play again? (y/n): ")
                if replay == "n":
                    print("Thank you for playing!")
                    break
            except ValueError:
                print("Please enter 'y' or 'n'.")

        except ValueError:
            print("Please enter a valid integer")

if __name__ == "__main__":
    main()