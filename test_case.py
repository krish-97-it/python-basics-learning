# 1. *******-[ Write a program to input elements into a list and display the list ]-*******
list_one = []    # creating an empty list
n = int(input("Enter number of elements : "))   # First need to enter the number of elements you want to insert in list

for i in range(0, n):   # iterating till the range
    ele = int(input())
    list_one.append(ele)  # adding the element

print(list_one)  # displaying list