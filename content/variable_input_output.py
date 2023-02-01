#  ********** What is variable?? **********
#  Variables are containers for storing data values. But Python has no command for declaring a variable.
#  A variable is created the moment you first assign a value to it.
#  Variables are case-sensitive.
#  in python String variables can be declared either by using single or double quotes:

#  Example-
a = 10
b = 'Hello world!!'
c = "My address is: 1/b,Wb-765578"
# a is integer type variable as it holds integer, b is string type as it holds a string

# ****** How to display a variable? *******
print(a)    # display the value of a
print(b)    # display the value of b

# ********* we can also define a variable with specific datatype during initialization *********
c = float(5)
d = str(5)
e = int(5)
f = bool(5)

print("c is :", type(c))
print("d is :", type(d))
print("e is :", type(e))
print("f is :", type(f))

#  **************** How to take user input ******************
# we can use input(). And always try to define the type of input you want from user
# by default if you don't specify any datatype it will treat as string
x = input("Enter a number:")  # variable value will treat as string by default
y = str(input("Enter your name:"))
z = int(input("Enter the second number:"))  # variable will accept only integer value

print(type(x))
print(type(y))


