def user_Input():
    # array_size = int(input("Enter the size of array: "))
    # array = []
    # for i in range(array_size):
    #     array.append(int(input(f"Enter the element {i+1}: ")))
    array = list(map(int, input("Enter the array:").split(",")))
    window_size = int(input("Enter the size of window: "))
    return array, window_size

def Sliding_Window(array, window_size):
    result = []
    for i in range(len(array) - window_size):
        result.append(max(array[i:i + window_size]))
    return result

arr, window_size = user_Input()
print(Sliding_Window(arr, window_size))
