# A List->
list1 = ["Ram", 20, "Hooghly", 8899774455]
# A Tuple->
tuple1 = ("Ram", 20, "Hooghly", 8899774455)

#  ****************** Defination of Dictionary in Python *******************
#  1. dictionary is always declare in curly braces.
#  2. it consists two things one is key and another is value of that key
#  3. we can put string, number, symbol, boolean, a tuple or list or  a dictionary itself as a value of a key.
#  4. keys are always be in double quote. if we use integer as key as don't require.
#  5. duplicate value will override existing one

py_dictionary = {
    "name": "Ram",
    "age": 20,
    "age": 21,  # duplicate value will override existing one
    "address": {"City/Town": "Dasghara", "District": "Hooghly", "Pin": 778888},
    "mobile": 8899774455,
    "participate": True,
    "Sports": ["Cricket", "Badminton", "Swimming"]
}

# Displaying dictionary
print(py_dictionary)

# to check a variable is dictionary or not
print(type(py_dictionary))

# length of a dictionary using-  len(<dictionary_name>)
print(len(py_dictionary))


# ********************* Adding a new key and value to a dictionary **********************

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
py_dictionary["color"] = "brown"

# or using update(). If the item does not exist, the item will be added.
py_dictionary.update({"color": "grey"})


# ********************* Accessing a dictionary, its key, value *********************

# accessing all keys and values using-  <dictionary_name>.items()
print(py_dictionary.items())

# get or accessing all keys using-  <dictionary_name>.keys()
print(py_dictionary.keys())

# get or access all values only using-  <dictionary_name>.values()
print(py_dictionary.values())

# Accessing a specific key value using-  <dictionary_name>["<key_name>"]
print(py_dictionary["name"])

# Accessing a specific key value using-  <dictionary_name>.get(["key_name"])
print(py_dictionary.get("participate"))


# ****************** Modify or update a dictionary and its key and values *****************

# modify or update a key value by directly assign a new value-  <dictionary_name>["<key_name>"] = <new value>
py_dictionary["participate"] = False

# modify or update a key value by update method-  <dictionary_name>.update("<key_name>":<new value>)
py_dictionary.update({"name": "Vijay"})

#  **************************** copying a dictionary ***************************
dictionary2 = dict(py_dictionary)
print(dictionary2)


# ********************* Delete a specific key or a dictionary itself *********************

# delete a specific item with key
py_dictionary.pop("participate")

# The popitem() method removes the last inserted item-  <dictionary_name>.popitem()
py_dictionary.popitem()

# Delete a specific item with key. it can delete a whole dictionary also by--  del <dictionary_name>
del py_dictionary["participate"]  # deleting a particular key with value
del py_dictionary

# *********************** print key and its value by accessing a dictionary using loop *************************
for x, y in dictionary2.items():
    print(x, y)


# ************************ User defined dictionary with example ***********************

# ********* Program-1 **********
input_dict = {}  # new blank dictionary
n = int(input("Enter number of elements or record you want to store: "))  # define length of dictionary
for i in range(n):
    name = input("Enter name of the student:")
    marks = int(input("Enter marks of the student:"))
    input_dict[name] = marks  # considering name as key and marks as value

print(input_dict)


# ******** Program-2 *********
# write a program to create a nested dictionary that keep students name and roll with a student serial number as key
# like - "Student1": {"name": "Ram", "Marks":90}"
# After creating dictionary now print those student name and marks who scored more than 75
dictionary_input = {}
n = int(input("Enter the number of student you want to enroll:"))  # number of student you want to keep as record
for i in range(n):
    name = input("Enter name of the student:")
    marks = int(input("Enter marks of the student:"))
    temp_dict = {
        "name": name,
        "marks": marks
    }
    dict_key = "student" + str(i + 1)
    dictionary_input[dict_key] = temp_dict

print(dictionary_input)  # display the dictionary
new_dict = {}

print("Students who scored more than 75 marks:\n")
for x, y in dictionary_input.items():
    if y["marks"] > 75:
        new_dict[x] = y

for x, y in new_dict.items():
    print(y)

