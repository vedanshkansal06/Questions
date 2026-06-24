def remove_duplicates(numbers_list):
    """
    Write a program to remove duplicate values from an array and returns an array of unique values. int[] removeDuplicates(int[]values)
    Ex:
        values = [2, 4, 6, 2, 8, 10, 4, 12, 14, 6]
        result = [2, 4, 6, 8, 10, 12, 14]
    """
    return list(set(num_list))
num_list = []
print("Enter the numbers in the list one by one and press 0 to end: ")
while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    num_list.append(user_input)
print(remove_duplicates(num_list))
