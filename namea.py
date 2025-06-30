n = 5
for i in range(0, n):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range(0, i + 1):
        if i == n // 2 or k == 0 or k == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()