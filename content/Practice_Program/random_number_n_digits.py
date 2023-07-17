import random

def generateRandomNumber(x):
    a = 10**(x-1)
    b = 10**(x)
    return random.randint(a,b)

n = int(input("Enter number of digits: "))
print(generateRandomNumber(n))