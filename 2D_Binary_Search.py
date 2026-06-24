def userInput():
        """Takes input from user."""
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        matrix = []
        for i in range(rows):
            row = list(map(int, input().split()))
            if len(row) != cols: return False
            matrix.append(row)
        target = int(input("Enter target: "))
        return matrix, target

def search_matrix(matrix, target):
    """Searches the matrix for target using binary search"""
    rows = len(matrix)
    cols = len(matrix[0])
    low,high = 0,rows*cols-1
    while low < high:
        mid = (low+high)//2
        m,n = divmod(mid,cols)
        if matrix[m][n] == target: return True
        elif matrix[m][n] < target: low += 1
        elif matrix[m][n] > target: high -= 1
        else: return False

matrix, target = userInput()
print(search_matrix(matrix, target))
