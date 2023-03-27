# Comparison between three numbers
a, b, c = 10, 12, 7
if a > b > c:
    print("a is greater number")
elif b > c and b > a:
    print("b is greater number")
else:
    print("c is greater number")

# find positive negative number ex-2
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# user input ex-3
a = float(input("Enter first number:"))
b = float(input("Enter first number:"))
c = float(input("Enter first number:"))
if a > b and a > c:
    print(a, " is greater number")
elif b > c and b > a:
    print(b, " is greater number")
else:
    print(c, " is greater number")

# Short Hand if
if b > c: print("b is greater number")

# Short Hand If else Ternary Operators
print("b is greater number") if b > c else print("c is greater number")

# nested if else
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
