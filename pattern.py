#This is the programe of right-right angle triangle
# print("Enter the number of row and column [rows==column]::\n")
# m =int(input())
# n=1
# for i in range(m):
#     for j in range(n):
#         print(" *", end=" ")
#     n=n+1
#     print("\n")

# This is the programe for left-right angle triangle
print("Enter the number of row and column [rows==column]::\n")
m =int(input())
n=m
l=0
for i in range(m):
    for j in range(l):
        print(end="  ")
    for k in range(n):
        print("* ", end="")
    n=n-1
    l=l+1
    print("\n")

#This is the programe for triangle
# print("Enter the number of row and column [rows==column]::\n")
# m =int(input())
# n=m
# l=0
