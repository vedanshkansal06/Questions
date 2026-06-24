def user_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        col = list(map(int, input().split()))
        if len(col) != cols: return False
        for j in col:
            if j == 0 or j == 1: pass
            else: return False
        matrix.append(col)
    return matrix

def Island_Number(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    def isIsland(row,col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] == 0: return False
        matrix[row][col] = 0
        isIsland(row-1,col)
        isIsland(row+1,col)
        isIsland(row,col-1)
        isIsland(row,col+1)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
                isIsland(i,j)
    return count

area = user_input()
print(area)
print(Island_Number(area))

