
# Python has two primitive loop commands:
# 1. while loops
# 2. for loops.

# ********** While Loop *************
# With the while loop we can execute a set of statements as long as a condition is true. 

# While loop execution Ex-2
a = 5
while a < 10:
    print("hello-", a)
    a += 1                  #  Don't forgot to increament i else the loop will execute forever.

# Ex-2 including conditional statement and break in while loop
a = 5
i = 1
while i < 6:
    res = a**i
    # print("hello-", a)
    if res >= 500:
        break              #  With the break statement we can stop the loop even if the while condition is true:
    print("power-", res)
    i = i + 1

# Continue statement in while and we can use ele statement with while
i = 0
while i < 10:
    i = i+1
    if i >= 4 and i <= 6:
        continue            #  With the continue statement we can stop the current iteration, and continue with the next:
    if i < 10:
        print(i)
else:
    print("i is no longer less than 10. loop execution is done")




