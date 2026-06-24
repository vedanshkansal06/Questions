def tripletSum(num_list, target_sum):
    """
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.
    Ex:
        target_sum = 6
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = [[1, 2, 3]]
    """
    sorted_nums = sorted(num_list)
    result=[]
    for i in range (len(sorted_nums)-2):
        left = i+1
        right = len(sorted_nums)-1
        current_sum = sorted_nums[i] + sorted_nums[right] +sorted_nums[left]
        if current_sum == target_sum:
            result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
        elif current_sum > target_sum:
            right = right-1
        else :
            left = left+1
        return result
num_list = []
print("Enter the numbers in the list one by one and press 0 to end: ")
while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    num_list.append(user_input)
target_sum = int(input("Enter a target sum: "))
print(tripletSum(num_list, target_sum))