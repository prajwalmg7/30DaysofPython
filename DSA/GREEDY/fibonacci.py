#Getting sum of nth fibanacci sequence

num = int(input("Enter the index:"))

def fibonacci(num):
    assert num >=0 and int(num) == num, 'The number must be a positive integer'  
    if num in [0,1]:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num -2)

print(fibonacci(num))

