rows=int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(rows):
        if j == rows-1-i:
            print("/",end="")
        elif j == i:
            print("\\",end="")
        else:
            print("*",end="")
    print("")