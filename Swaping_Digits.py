def swap(num):
    """
    Write a program (without using inbuilt functions and not using Strings or array) to swap first and last digits of any number.
    """
    if num < 10:
        return num
    else:
        digit = num
        last_digit = digit % 10
        divisor = 1
        while digit >= 10:
            digit = digit // 10
            divisor *= 10
        first_digit = digit
        middle_digit = (num % divisor) // 10
        swapped_num = (last_digit * divisor) + (middle_digit * 10) + (first_digit)
        return swapped_num
int = int(input("Enter a number: "))
print(swap(int))