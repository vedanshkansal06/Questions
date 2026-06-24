import numpy as np

def user_input():
    """Takes input from user."""
    # print("Enter the positions of enemies (as H ,Q ,C ,and E and king (as K): ")
    # return np.array([[input() for j in range(2)] for i in range(2)], dtype=str)
    pos=[".", ".", ".", "Q", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "E", ".", ".", "."],
    [".", "H", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "C", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "K", ".", ".", "."]
    return pos


def isKingSafe(positions):
    """Takes positions of kings and enemies and checks if the king is safe or not."""
    k_loc = np.argwhere(positions == "K")

    if len(k_loc) == 0: return True
    k_row, k_col = k_loc[0]

    def isPathClear(k_row, k_col,e_row,e_col):
        if k_row == e_row:
            c_start = min(k_col,e_col)+1
            c_end = max(k_col,e_col)
            path = positions[k_row][c_start:c_end]
            return all(p == "." for p in path)
        elif k_col == e_col:
            r_start = min(k_row,e_row)+1
            r_end = max(k_row,e_row)
            path = positions[k_row][r_start:r_end]
            return all(p == "." for p in path)
        elif abs(k_row-e_row) == abs(k_col-e_col):
            step_r = 1 if e_row > k_row else -1
            step_c = 1 if e_col > k_col else -1
            kr = k_row+step_r
            kc = k_col+step_c
            while kr != e_row or kc != e_col:
                if positions[kr][kc] == ".": return False
                kr = k_row+step_r
                kc = k_col+step_c
        else: return True

    # Horse Check
    h_loc = np.argwhere(positions == "H")
    for h in h_loc:
        if (abs(h[0]-k_row) == 1 and abs(h[1]-k_col)==2) or (abs(h[0]-k_row) == 2 and abs(h[1]-k_col) == 1):
            return False

    # Elephant Check
    e_loc = np.argwhere(positions == "E")
    for e in e_loc:
        if (k_row == e[0] or k_col == e[1]) and isPathClear(k_row,k_col,e[0],e[1]): return False

    # Camel Check
    c_loc = np.argwhere(positions == "C")
    for c in c_loc:
        if abs(c[0]-k_row) == abs(c[1]-k_col) and isPathClear(k_row,k_col,c[0],c[1]): return False

    # Queen Check
    q_loc = np.argwhere(positions == "Q")
    for q in q_loc:
        if ((k_row == q[0] or k_col == q[1]) or abs(c[0]-k_row) == abs(c[1]-k_col)) and isPathClear(k_row,k_col,q[0],q[1]): return False

    return True

positions = user_input()
print(isKingSafe(positions))

