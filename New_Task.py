n = int(input("Enter any no of row and column, [row=column]:-"))
m = int(input("Choose a number between 1 or 0, here [1 = True & 0 = False]:-"))
if(m==0):
    g=n
    l=0
    for i in range(g):
        for j in range(l):
            print(end="  ")
        for k in range(g):
            print("* ", end="")
        g=g-1
        l=l+1
        print("\n")
    
if(m==1):
    g=n
    for i in range(g):
        for k in range(g):
            print("* ", end="")
        g=g-1
        print("\n")