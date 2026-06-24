def userInput():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1, str2

def interleaving(str1, str2):
    result = []
    def backtrack(i, j, current_path):
        if i == len(str1) and j == len(str2):
            result.append(" ".join(current_path))
            return
        if i< len(str1):
            current_path.append(str1[i])
            backtrack(i+1, j, current_path)
            current_path.pop()
        if j < len(str2):
            current_path.append(str2[j])
            backtrack(i, j+1, current_path)
            current_path.pop()

    backtrack(0, 0, [])
    return result

str1, str2 = userInput()
print(interleaving(str1, str2))
