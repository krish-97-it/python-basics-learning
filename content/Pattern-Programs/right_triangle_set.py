# *
# * *
# * * *
# * * * *
# * * * * *
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print()

# ===============Pattern-2===============
# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4
for i in range(0, n):
    for j in range(0, i+1):
        print(i, " ", end="")
    print()


# ============= Pattern-3 ===============
# 0
# 0  1
# 0  1  2
# 0  1  2  3
# 0  1  2  3  4
for i in range(0, n):
    for j in range(0, i+1):
        print(j, " ", end="")
    print()

# ============== Pattern-4 ===============
# A
# A  B
# A  B  C
# A  B  C  D
# A  B  C  D  E
for i in range(65, 70):   # 97-122 for lowercase
    for j in range(65, i+1):
        print(chr(j), " ", end="")
    print()

# ===============pattern-5================
# 0
# 0 #
# 0 # 0
# 0 # 0 #
# 0 # 0 # 0
for i in range(0, n):
    for j in range(0, i+1):
        if (j % 2) == 0:
            print("0 ", end="")
        else:
            print("# ", end="")
    print()
