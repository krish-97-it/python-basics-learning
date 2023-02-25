
# ******************** Defination Of Tuples *******************
# Tuple  is denoted by "()"
# Tuple allow duplicate values
# Tuple is ordered and supports indexing
# Tuple is unchangeable that means we cant add or remove or modify a value in tuple
# To Modify a tuple we need to convert it to a list first.

# **** Declare of a tuple and displaying it ****
tuple1 = (1, "ram", "@", "ram", "India")
print(tuple1)  # display tuple

# **** Displaying specific Items by index numbers ****
print(tuple1[2])  # display a specific item with index number
print(tuple1[-4:-1])  # display a set of specific items with start index and end index number
print(tuple1[:-2])  # display a specific item with index number
print(tuple1[1:-2])  # display a specific item with index number

# ****I.E-EXCEPTIONAL CASE: if any tuple need to create with one value or item then have to put a comma after its one and only item.
tuple2 = ("ram",) # without comma it will treat as string only
var_type = type(tuple1)  # type is used to know the type of variable
print(var_type)

# **** Length of a tuple ****
tuple_length = len(tuple1)  # len is a method where we can put a object or variable to find its length
print("the length of the tuple1: ", tuple_length)

# **** Search a item in tuple ****
if "&" in tuple1:
    print("Yes Found")
else:
    print("Not Found")

# **** Concatinate two tuple using (+) operator or sum() ****
tuple10 = (1, 2, 3, 4, 5)
tuple20 = (3, 4, 5, 6, 7)
tuple30 = tuple1 + tuple2  # concatenate tuples using + operator
print(tuple30)

tuple31 = sum((tuple1, tuple2), ()) #have to pass one blank tuple as 2nd argument
print(tuple31)

# **** Tuple is unchangeable but by converting in list we can modify the items ****
x = (1, "Maths", "#")                           # A Tuple
y = list(x)                                     # Converted to List
y[1] = "Science"                                # Insert a new value at index 1
y.append("Hooghly")                             # Add a new value at the end of list
print(type(y), "  display:", y)                 # Xheck the type of Y and displaying Y
y.remove("Hooghly")                             # Remove an item from the List
z = tuple(y)                                    # Re-converting List to tuple z
print(type(z), "  display:", z)                 # Type of z and displaying it

# **** Add / Copy a tuple into another tuple ****
new_tuple = (True,)
z = z + new_tuple
print("final result:", z)

# **** Get index number of a specific element of a tuple ****
print("The index of the given element is: ", z.index("#"))

# **** Check how many times a specific element is present in a tuple ****
print("no. of times a element occurs: ", tuple1.count("ram"))   #display no. of occurance 

# **** Get maximum and minimum element of a tuple ****
tuplez, tuplex = (15, 500, 700, 450, 120, 5, 780, 549, True), ("ram", "nayak", "#", "school", "vbc", "hmr")
print("max value element: ", max(tuplez))
print("min value element: ", min(tuplez))
print("max value element: ", max(tuplex))
print("min value element: ", min(tuplex))

# **** Sorted a tuple ****
print("sorted element: ", tuple(sorted(tuplez)))

# **** User inputed Tuple in one line ****
my_tuple = tuple(input().split())
print(my_tuple)

# **** Write a program to take a userinput tuple and display it ****
# 6. ============= write a program to take a userinput tupple and display it =============
temp_data = (input("Enter elements in tuple with space:"))
split_data = temp_data.split() # split into list
my_tuple = tuple(split_data)   # reconvert into tuple
print(my_tuple)
print(type(my_tuple))
