# def doSort(temp_list):
#     for i in range(0,len(temp_list)):
#         for j in range(0,(len(temp_list)-i)):
#             if temp_list[j] > temp_list[j+1]:
#                 temp = temp_list[j]
#                 temp_list[j]    =   temp_list[j+1]
#                 temp_list[j+1]  =   temp
#     print("sorted list",temp_list)

n = int(input("Enter number of elements you want to insert inside linked list: "))   # First need to enter the number of elements you want to insert in list
print("now enter "+str(n)+" elements one by one: ")

list1 = []    # creating an empty list
for i in range(0,n):   # iterating till the range
    num = int(input("element "+str(i)+": "))
    list1.append(num)  # adding the element

# print(list1)

for i in range(0,len(list1)):
    # print("pass-",i)
    for j in range(0,(len(list1)-1-i)):
        # print("innerloop===",j)
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j]    =   list1[j+1]
            list1[j+1]  =   temp
        # print("intermidiate-sorted-list===",list1)
# print("sorted list",list1)
# doSort(list1)