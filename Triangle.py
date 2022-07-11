m=0
n= int(input("Enter the value of row::\n"))
k=n
for i in range(n):
    for j in range(k):
        print(end=" ")
    for j in range(m):
        print(end="* ")
    m=m+1
    k=k-1
    print("\n")