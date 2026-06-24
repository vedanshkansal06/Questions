def userInput():
    """Takes input from user."""
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    if rows != cols: return False
    for i in range(rows):
        col = list(map(int, input().split()))
        if len(col) != cols: return False
        matrix.append(col)
    return matrix

def rotate_image(image):
    for i in range(len(image)):
        for j in range(i+1,len(image[i])):
            image[i][j],image[j][i] = image[j][i],image[i][j]
    for i in range(len(image)):
        image[i].reverse()

matrix = userInput()
print(matrix)
rotate_image(matrix)
print(matrix)