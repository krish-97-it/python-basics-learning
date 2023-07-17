def findPos(ar,ele):
    if(ar[0]>ele): # 10>35 #10>5
        return 0
    else:
        pos = -1

    for i in range(len(ar)-1): #i=3
        if(ar[i]<ele and ele<ar[i+1]): # 30<35 and 35<40
            pos = i+1  #pos = 3+1
            break

    if(pos == -1 and i <= ar[len(ar)-1]):
        pos = len(ar)

    return pos

def eleShift(ar,pos):
    ar.append(None)
    size = len(ar)
    i = size-1 # 10
    print("pos====",pos)
    print("i======",i)
    while i >= pos:  #10>=5
        ar[i] = ar[i-1] #ar[10] = ar[9]
        i = i-1

myList = [10,20,25,30,40,60,75,80,90,100]
print("Given List: ",myList)

element = int(input("Enter an new element to insert: "))

get_index = findPos(myList,element)

print("Element will be inserted at- ",get_index)
eleShift(myList,get_index)
myList[get_index] = element
print("List after inserting new element at pos- ",str(get_index),": ")
print(myList)


    