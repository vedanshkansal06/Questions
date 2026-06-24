def isPrime(num):
    """
    Find the largest number less than N whose each digit is prime number.
    """
    if num < 2:
        return False
    for i in range(num,2,-1):
        digits = []
        temp = i
        while temp>0:
            digits.append(temp % 10)
            temp //= 10
        if all(digit in [2,3,5,7] for digit in digits):
            return i
num = int(input("Enter a number: "))
print(isPrime(num))