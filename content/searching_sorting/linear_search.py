# step-1 : len1 = lenght of the list and i = 0
# step-2 : Repeat step 3 and step 4 until i is lesser than len1
# step-3 : if len1[i] == n then element is found at position i
# step-4 : i = i+1

# step-1: start search from the first element of the list1 and check n with each element of the list1
# step-2: if element is found, return the position of the element
# step-3: if element is not found, return element is not present

def lenSearch(arr,key):
    i = 0
    # while i < len(arr) and arr[i] != key: # 0<5 and 1!=7 || 1<5 and 9!=7 || 2<5 and 7!=7
    #     i=i+1
    
    # if i<len(arr):
    #     return i
    # else:
    #     return False
    while i<len(arr):
        if arr[i] == key:
            return i
        else:
            i=i+1
    else:
        return False
    
# execution of program will start from here
n = int(input("Enter number of elements you want to insert inside linked list: "))   # First need to enter the number of elements you want to insert in list
print("now enter "+str(n)+" elements one by one: ")

list1 = []    # creating an empty list
for i in range(0,n):   # iterating till the range
    num = int(input())
    list1.append(num)  # adding the element

ele =  int(input("Enter a element to search:"))
index = lenSearch(list1,ele)
if index:
    print("element found at-",index)
else:
    print("element not found")
