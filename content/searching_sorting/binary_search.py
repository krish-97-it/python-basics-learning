# applicable only for sorted array
# it follows divide and conquer
# faster than linear search as less iteration required

def bSearch(arr,key):
    # i=0
    start = 0
    end = len(arr)-1

    while start <= end: #0<6

        mid = (start + end)//2

        # print("------iteration------",i)
        # print("startpoint",start)
        # print("endpoint",end)
        # print("midpoint-",mid)
        
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            start=mid+1
        else:
            end=mid-1

        # i=i+1
    else:
        return False
    
# execution of program will start from here
n = int(input("Enter number of elements you want to insert inside linked list: "))   # First need to enter the number of elements you want to insert in list
print("now enter "+str(n)+" elements one by one: ")

list1 = []    # creating an empty list
for i in range(0,n):   # iterating till the range
    num = int(input("element "+str(i)+": "))
    list1.append(num)  # adding the element

ele =  int(input("Enter a element to search:"))
index = bSearch(list1,ele)
if index:
    print("element found at-",index)
else:
    print("element not found")
