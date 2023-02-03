
# =============== pattern-1 ===============
n = 5
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
for i in range(0, n):
    for j in range(n-1, i, -1):
        print("  ", end="")
    for k in range(0, i+1):
        print("* ", end="")
    print()

# ============= pattern-2 =============
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
for i in range(0, n):
    for j in range(n-1, i, -1):
        print("  ", end="")
    for k in range(1, i+2):
        print(k, end=" ")
    print()

# ============= pattern-3 =============
#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
for i in range(0, n):
    for j in range(n-1, i, -1):
        print("  ", end="")
    for k in range(0, i+1):
        print(i-k+1, end=" ")
    print()


