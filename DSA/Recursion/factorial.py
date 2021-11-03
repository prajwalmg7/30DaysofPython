#Finding the factorial of a given number using recursive method.

num = int(input ("Enter number: "))

def factorial(num):
    assert num >=0 and int(num) == num, 'The number must be a positive integer'
    if num in [0,1]:
        return 1
    else:
        return ((num) * factorial(num-1))

print(factorial(num))
