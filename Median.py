def userInput():
    array1 = list(map(int, input("Enter the elements in 1st array: ").split()))
    array2 = list(map(int, input("Enter the elements in 2nd array: ").split()))
    return array1,array2

def median(array1, array2):
    merged_array = []
    m, n = len(array1), len(array2)
    i, j = 0, 0
    while i < m and j < n:
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < m:
        merged_array.append(array1[i])
        i += 1

    while j < n:
        merged_array.append(array2[j])
        j += 1

    if (m+n) % 2 == 0:
        return ( merged_array[(m+n) // 2] + merged_array[(m+n) // 2 - 1] ) / 2
    else:
        return merged_array[(m+n) // 2]

array1, array2 = userInput()
print("The median of the given arrays is: ", median(array1, array2))

