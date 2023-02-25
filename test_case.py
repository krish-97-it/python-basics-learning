
# ************************ This file is to write code and test it randomly *****************************
# ********** Freqently Code can be changed as per need of test **********

# *Program/Feature Name You have to mention- 

# *Write a program to input elements into a list and display the list
list_one = []    # creating an empty list
n = int(input("Enter number of elements : "))   # First need to enter the number of elements you want to insert in list

for i in range(0, n):   # iterating till the range
    ele = int(input())
    list_one.append(ele)  # adding the element

print(list_one)  # displaying list

print(max(list_one))
print(min(list_one))

# *Write a program to find maximum and minimum number in the list without max and min function
max_num = list_one[0]
min_num = list_one[0]
for i in range(0, len(list_one)):
    if max_num < list_one[i]:
        max_num = list_one[i]
    elif min_num > list_one[i]:
        min_num = list_one[i]
print("Minimum Number:", min_num)
print("Maximum number:", max_num)

# Maximum and minimum elemnt using max and min function
list_sort = [11,80,10,16,4,110,1]
print(max(list_sort))
print(min(list_sort))