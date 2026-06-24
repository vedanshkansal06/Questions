import numpy as np

def user_input():
    """Takes input from user."""
    # digits = np.empty((9,9), dtype=str)
    # for i in range(9):
    #     for j in range(9):
    #         digits[i][j] = input("Enter digit " + str(i) + "/" + str(j) + " = ")
    # return digits
    test_case = np.array([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ])

    # print(condition_check(test_board)) # This will instantly print True
    return test_case

def condition_check(sudoku_grid: np.ndarray):
    """Checks if a sudoku grid is valid."""
    # Condition 1
    for i in range(9):
        seen_num = set()
        for j in range(9):
            if sudoku_grid[i][j] == "." or sudoku_grid[i][j] == "":
                continue
            counter = sudoku_grid[i][j]
            # for k in range(9-j):
            #     if k+j+1 != 9:
            #         if sudoku_grid[i][k+j+1] == counter:
            #             return False
            if counter in seen_num: return False
            seen_num.add(counter)
    # Condition 2
    for i in range(9):
        seen_num = set()
        for j in range(9):
            if sudoku_grid[j][i] == "." or sudoku_grid[j][i] == "":
                continue
            counter = sudoku_grid[j][i]
            # for k in range(9-j):
            #     if k+j+1 != 9:
            #         if sudoku_grid[k+j+1][i] == counter:
            #             return False
            if counter in seen_num: return False
            seen_num.add(counter)
    # Condition 3
    for row in range( 0, 9, 3):
        for col in range( 0, 9, 3):
            seen_num = set()
            for i in range(3):
                for j in range(3):
                    if sudoku_grid[row+i][col+j] == "." or sudoku_grid[row+i][col+j] == "": continue
                    counter = sudoku_grid[row+i][col+j]
                    if counter in seen_num: return False
                    seen_num.add(counter)
    return True

digit = user_input()
print(digit)
print(condition_check(digit))