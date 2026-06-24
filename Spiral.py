def userInput():
    """Takes input from user."""
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        col = list(map(int, input().split()))
        if len(col) != cols: return False
        matrix.append(col)
    return matrix

def clockwise_spiral(matrix):
    """Reads the matrix in a clockwise spiral manner."""
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

def anticlockwise_spiral(matrix):
    """Reads the matrix in a anti-clockwise spiral manner."""
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while left <= right and top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1
        if top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1
    return result
get_matrix = userInput()
print(" ".join(map(str, clockwise_spiral(get_matrix))))
print(" ".join(map(str, anticlockwise_spiral(get_matrix))))