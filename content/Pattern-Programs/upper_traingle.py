n = 5
# =============== pattern-0 ===============
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# 1 2 3 4 5
#   1 2 3 4
#     1 2 3
#       1 2
#         1
for i in range(n, 0, -1):
    for j in range(0, n-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print(k, end=" ")
    print()

# =============== pattern-1 ===============
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(i, 0, -1):
        print("* ", end="")
    print()

# ================ pattern-2 ===============
# 5  5  5  5  5
# 4  4  4  4
# 3  3  3
# 2  2
# 1
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(i, 0, -1):
        print(i, " ", end="")
    print()

# ================ pattern-3 ===============
# 5  4  3  2  1
# 4  3  2  1
# 3  2  1
# 2  1
# 1
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(i, 0, -1):
        print(j, " ", end="")
    print()

# ================ pattern-4 ===============
# 1  2  3  4  5
# 1  2  3  4
# 1  2  3
# 1  2
# 1
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(1, i+1):
        print(j, " ", end="")
    print()

# ================ pattern-4 ===============
# 1  2  3  4  5
# 1  2  3  4
# 1  2  3
# 1  2
# 1
k = 1
for i in range(n, 0, -1):  # (start,limit/range, inc/dec
    for j in range(1, i+1):
        print(k, " ", end="")
    print()
    k = k+1
p = 4
for i in range(1, n):  # (start,limit/range, inc/dec
    for j in range(0, i+1):
        print(p, " ", end="")
    print()
    p = p-1
