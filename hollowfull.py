n = 5
for i in range(0,n):
    for j in range(0,n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*", end="")
        else:
            print(" ", end="")

    print()

#     n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()