
#*  This module consists of functions for mathematical operation

def do_addition(x, z):
    sum_res = x + z
    return sum_res

def do_multiplication(x, z):
    print("The multiplication of given two number: ", x * z)


def do_subtraction(x, z):
    print("The subtraction of given two number: ", x - z)


def do_division(x, z):
    print("The division of given two number: ", x // z)

def do_calculation():
    print("List of operations:-")
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")
    n = int(input("Please enter your choice: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    def try_more():
        print("**Do you want to try more?**")
        print("0 - exit")
        print("10 - try more")
        num = int(input("Please enter your choice: "))
        if num == 10:
            do_calculation()        # when a function call itself- recurssion
        elif num == 0:
            exit()

    if n == 1:
        res = do_addition(a, b)
        print("The addition of given two number: ", res)
        try_more()
    elif n == 2:
        do_subtraction(a, b)
        try_more()
    elif n == 3:
        do_multiplication(a, b)
        try_more()
    elif n == 4:
        do_division(a, b)
        try_more()


print("-------Calculator-------")
# do_calculation()