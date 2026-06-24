def userInput():
    height = list(map(int, input("Enter the heights of vertical lines: ").split(",")))
    return height

# def max_volume(array):
#     max_volume = 0
#     n = len(array)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if array[i] > array[j]:
#                 current_volume = array[j] * (j-i)
#                 max_volume = max(max_volume, current_volume)
#             else:
#                 current_volume = array[i] * (j-i)
#                 max_volume = max(max_volume, current_volume)
#     return max_volume

def max_volume(array):
    max_volume = 0
    left = 0
    right = len(array) - 1
    while left < right:
        current_volume = min(array[left], array[right]) * (right - left)
        max_volume = max(max_volume, current_volume)
        if array[left] < array[right]: left += 1
        else: right -= 1
    return max_volume

height = userInput()
print("The maximum volume is:",max_volume(height))