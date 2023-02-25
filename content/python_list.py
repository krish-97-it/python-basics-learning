
# ******************* Definition of list *****************
# A list is  the example of iterable object like tuple, sets, dictionary etc.
# A list is declared in square bracket
# Lists are used to store multiple items
# A list is ordered, changeable, allowable for storing duplicate elements
# List items are indexed

# Example of list
list1 = ["Bat", "Ball", "Bag", 10, "@"]

# ************************* display of list ****************************
print("This is a list", list1)

# *************************length of list*****************************
list1_length = len(list1)
print("length of list1", list1_length)

# ********************* How to access list elements ************************
# accessing element of list with specific index number
n = int(input("Enter the index: "))
print("Specific element of the given index", list1[n])

# list support negative indexing
n = int(input("Enter the second last index: "))
print("Specific element of the given negative index", list1[n])

# we can print particular range of elements of a given index
start_at = int(input("Enter the starting index: "))
end_at = int(input("Enter the ending index: "))
print(list1[start_at:end_at])
print(list1[:end_at])  # print all till before the mentioned end index
print(list1[start_at:])

# search a specific element whether it is present in our list or not
ele = input("Enter the the element you want to search: ")
if ele in list1:
    print("Yes Found")
    # how can I get the index number of an element from a list
    print("The index of the given element is: ", list1.index(ele))
else:
    print("Not Found")

# ******************* Modifying / changing list items **********************
# referring index number to change the value of a specific item
ele = input("Enter the element you want to replace or change: ")
index_no = list1.index(ele)
new_ele = input("Enter the element you want to place: ")
list1[index_no] = new_ele
print("After change the value of the specific index", list1)

# We can change elements of a range of index
list1[3:] = ["Wicket", "Gloves"]
print("A range of elements have been changed from the given index", list1)

# ********************** Insert element in list ***********************
# inserting a new single element in list in specific index
list1.insert(3, "Wicket")
print("Insert element at a specific index position", list1)

# inserting a new  single element at the end of the list
list1.append("Wicket")
print("List after appending a new element at the end", list1)

# inserting new multiple element as tuple,list,set at the end of the list
list1.extend(["Wicket", "Bottle", "Gloves"])
print("List after adding iterable object:", list1)

# ******************* Removing/deleting element or entire list ********************
# removing specific element
list1.remove("Bottle")
print("list after removing the specific element", list1)

# removing element of a specific index
list1.pop(4)
del list1[2]
print("list after removing the element of specific index", list1)

# remove an element from last of the list
list1.pop()
print("After removing last element", list1)

# without deleting, clear list or empty a list
list1.clear()
print("list are now empty", list1)

# Delete entire list using "del" keyword
del list1


#               ******************************* Assignments **********************************

# 1. *******-[ Write a program to input elements into a list and display the list ]-*******
list_one = []    # creating an empty list
n = int(input("Enter number of elements : "))   # First need to enter the number of elements you want to insert in list

for i in range(0, n):   # iterating till the range
    ele = int(input())
    list_one.append(ele)  # adding the element

print(list_one)  # displaying list

# 2. ********-[ Write a program to print all the odd numbers in a list]
print("Odd numbers in the list")
# for i in range(0, len(list_one)):
#     if list_one[i] % 2 != 0:
#         print(list_one[i])
for j in list_one:
    if j % 2 != 0:
        print(j)

# 3. *******-[ Write a program to print the sum of all even numbers ]-*******
print("Sum of all even numbers in the list:")
e_sum = 0
for j in list_one:
    if j % 2 == 0:
        e_sum = e_sum + j

print(e_sum)


# 4. *******-[ Write a program to check duplicate elements in array or not ]-*******
list_two = []
duplicate = []
for i in list_one:
    if i not in list_two:
        list_two.append(i)
    else:
        duplicate.append(i)

if len(duplicate) >= 1:
    print("duplicate number is present in the array")
else:
    print("no duplicate elements")

# 5. *******-[ Write a program to find maximum and minimum number in the list ]-********
max_num = list_one[0]
min_num = list_one[0]
for i in range(0, len(list_one)):
    if max_num < list_one[i]:
        max_num = list_one[i]
    elif min_num > list_one[i]:
        min_num = list_one[i]
print("Minimum Number:", min_num)
print("Maximum number:", max_num)
