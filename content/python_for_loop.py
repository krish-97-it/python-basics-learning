# For loop is one of the iterative loop using for keyword.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# ***** Syntax *****
# for i in range(a,b,c):
# Here a is starting point, b is limit or length or iteration of the loop, c is the increment value.
# range() function returns a sequence of numbers, starting from 0 by default, and increments by 1.
# range() requires minimum one parameter that is length.

# ***** Example-1 stop the current interation and skip to next using "continue" statement*****
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# ***** Pass statement *****
# If we have a for loop with no content, put in the 'pass' statement to avoid getting an error.
for x in [0, 1, 2]:
    pass

# ***** Example-2 Program to get a multiplication table of a number *****
num = int(input("Enter the number:\n"))
for k in range(1, 11):  # range(i=0,i<6) # increase by 2 but by default range function automatically increment by 1
    print("=> " + (str(int(num))) + "X" + str(k), "=", int(num * k))
else:
    print("Multiplication Done")

# "break" statement is used to exit the loop immediately
num = int(input("Enter the number:\n"))
for k in range(1, 6, 2):  # range(i=0,i<6) # increase by 2 but by default range function automatically increment by 1
    print("=> " + (str(int(num))) + "X" + str(k), "=", int(num * k))
    break  # after first iteration loop will be terminated
else:
    print("Multiplication Done")  # due to using break it will not enter in else part

# ***** Nested Loops *****
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
# Example-3 Write a program to assign subjects to each student.
student = ["Ram", "Laxman", "Gita"]
subjects = ["Math", "English", "Geography"]

for x in student:
    for y in subjects:
        print(x, y)

# OUTPUT:
# Ram Math
# Ram English
# Ram Geography
# Laxman Math
# Laxman English
# Laxman Geography
# Gita Math
# Gita English
# Gita Geography
