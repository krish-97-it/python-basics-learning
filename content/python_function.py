
#   ****************** Function in Python ******************
#   A function is a block of code which only runs when it is called.
#   You can pass data, known as parameters, into a function.
#   A function can return data as a result.
#   A function in python is defined by 'def' keyword followed by function name and parenthesis.

#   *Example-

def do_addition(x,z):      # do_addition is the function name, there are two parameter/argument
    sum_res = x + z         # inside function body/task/calculation
    return sum_res          # return data/result
do_addition(5,6)            # function will not work until it is called properly. take care of no. of parameter you need to pass.


#   *------Function argument/Parameter------*
#   A parameter is the variable listed inside the parentheses in the function definition. Argument defines values.
#   The terms parameter and argument can be used for the same thing that is passing data/information
#   By default, a function must be called with the correct number of arguments.
#   if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.


#   *------ No argument/parameter ------*
#   function can has argument or no argument, in that case during function call no parameter or argument is passed.
#   *EXample-
def welcomee():
    print("Hello World!!")
welcomee()


# *------- Default parameter/argument -------*
def register_data(car3="OLA"):          # here car3 is a default parameter with a default value
    print("Your new car is - " + car3)
z = "Hero"
register_data() #case1: if the function has default parameter,so incase during function call if we dont pass any parameter it will use default parameter.
register_data("honda") #case2: in this case as parameter is given with function call, So, function will use "honda".
register_data(z) #case3: here also function will use the value of z


#   *------- Arbitrary Arguments -------*
#   If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def register_data(*car):
    print("Your new car is - " + car[1])
register_data("honda", "hero", "tvs", "royal")
register_data("honda", "hero")

#   *------- Keyword Arguments -------*
#   You can also send arguments with the key = value syntax.
#   This way the order of the arguments does not matter.
def register_data(car1, car2, car3="OLA"):          # three parameter, one has default value
    print("Your new car is - " + car1)
    print("Your new car is - " + car2)
    print("Your new car is - " + car3)
register_data(car2="honda", car1="hero")            # As one of the among three parameter is default, you can pass it function call or not.


#   *------- List as argument --------*
def final_cal(users):
    for i in users:
        print(i)
nam = str(input("Enter first name:"))
roll = int(input("Enter first roll:"))
city = str(input("Enter first city:"))
details = [nam, roll, city]                         # The list
final_cal(details)                                  # complete list we passed as parameter


#   *Example - Wap to make a calculator using python. it is a example of python switch case-also 
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
do_calculation()        #   calling the main function
