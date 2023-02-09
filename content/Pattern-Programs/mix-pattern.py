n = 5
print("================ pattern-1 =================")
# ================ pattern-1 =================
# 1  1  1  1  1
# 2  2  2  2
# 3  3  3
# 4  4
# 5
# 4  4
# 3  3  3
# 2  2  2  2
# 1  1  1  1  1

k = 1
p = 4
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(1, i + 1):
        print(k, " ", end="")
    print()
    k = k + 1
for i in range(1, n):  # (start,limit/range, inc/dec
    for j in range(0, i + 1):
        print(p, " ", end="")
    print()
    p = p - 1

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
for i in range(0, n):
    for j in range(n-1, i, -1):
        print("  ", end="")
    for k in range(0, i+1):
        print("* ", end="")
    print()
for i in range(n, 0, -1):
    for j in range(0, n-i):
        print("  ", end="")
    for k in range(0, i):
        print("* ", end="")
    print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
for i in range(0, n):
    for j in range(n-1, i, -1):
        print(" ", end="")
    for k in range(0, i+1):
        print("* ", end="")
    print()

for i in range(n, 0, -1):
    for j in range(0, n-i):
        print(" ", end="")
    for k in range(0, i):
        print("* ", end="")
    print()


print("Pattern-")
#     *
#   * * *
# * * * * *
#   * * *
#     *

for i in range(0, n):
    if i % 2 == 0:
        for j in range(n-1, i, -1):
            print(" ", end="")
        for k in range(0, i+1):
            print("* ", end="")
        print()
for i in range(n-1, 0, -1):
    if i % 2 != 0:
        for j in range(0, n-i):
            print(" ", end="")
        for k in range(0, i):
            print("* ", end="")
        print()


#         1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
for i in range(0, n):
    for j in range(n-1, i, -1):
        print("  ", end="")
    for k in range(0, i+1):
        print(i-k+1, end=" ")
    for z in range(2, i + 2):
        print(z, end=" ")
    print()


n = 7

#       *
#     *   *
#   *       *
# * * * * * * *
last = 0
for i in range(0, n):   # 1.(0, i<5, i++)    2.(1, 1<5, i++)False   3.(2, 2<5, i++)
    if i % 2 == 0:  # T
        for j in range(n-1, i, -1):     # 2.[(4,j>2, j--) (3,j>2, j--) (2,j>0, j--)]
            print(" ", end="")
        # only for last row
        if (i + 1) == n:
            last = 1
            for k in range(0, n):
                print("* ", end="")
        else:
            print("*", end="")
        # for printing space
        for k in range(1, 2*i):  # (0, k<-1, k++)
            print(" ", end="")
        # to eliminate extra star or space
        if i == 0:
            print(" ", end="")
        elif last == 1:
            print(" ", end="")
        else:
            print("*", end="")
        print()


#     *
#   *   *
# *       *
#   *   *
#     *

for i in range(0, n):   # 1.(0, i<5, i++)    2.(1, 1<5, i++)False   3.(2, 2<5, i++)
    if i % 2 == 0:  # T
        for j in range(n-1, i, -1):     # 2.[(4,j>2, j--) (3,j>2, j--) (2,j>0, j--)]
            print(" ", end="")
        print("*", end="")
        for k in range(1, 2*i):  # (0, k<-1, k++)
            print(" ", end="")
        if i == 0:
            print(" ", end="")
        else:
            print("*", end="")
        print()
for i in range(n-1, 0, -1):
    if i % 2 != 0:
        for j in range(0, n-i):
            print(" ", end="")
        print("*", end="")
        for k in range(1, 2 *(i-1)):  # (0, k<-1, k++)
            print(" ", end="")
        if i == 1:
            print(" ", end="")
        else:
            print("*", end="")
        print()

last = 0
n = 7
# * * * * * * *
#   *       *
#     *   *
#       *
for i in range(n-1, -1, -1):   # 1.(0, i<5, i++)    2.(1, 1<5, i++)False   3.(2, 2<5, i++)
    if i % 2 == 0:  # T
        for j in range(n-1, i, -1):     # 2.[(4,j>2, j--) (3,j>2, j--) (2,j>0, j--)]
            print(" ", end="")
        # only for last row
        if (i + 1) == n:
            last = 1
            for k in range(0, n):
                print("* ", end="")
        else:
            print("*", end="")
        # for printing space
        for k in range(2*i, 1, -1):  # (0, k<-1, k++)
            print(" ", end="")
        # to eliminate extra star or space
        if i == 0:
            print(" ", end="")
        else:
            if i+1 != n:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# * * * * * * * *
# *             *
# *             *
# *             *
# *             *
# * * * * * * * *
n = 6
m = 8
for i in range(0, n):
    for j in range(0, m):
        if i == 0 or i == n-1:
            print("* ", end="")
        else:
            if j == 0 or j == m-1:
                print("* ", end="")
            else:
                print("  ", end="")
    print()

