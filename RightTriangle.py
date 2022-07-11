m=5
n = int(input("Enter the number of row and column:-\n"))
for i in range(n):
    for j in range(m):
        print(end="* ")
    m=m-1
    print("\n")