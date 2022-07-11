print("You have to guess the number and you can only chose the numbers between 0 to 9::\n")
i=1
j=5
n=5 
while(i<=5):
    print("Now gues the number:-\n")
    print("You have total no. of gusses left",j)
    num= int(input())
    if (num<0 or num<5):
        print("You choose wrong number\n")
        j=j-1

    if (num>9 or num>5):
        print("You choose wrong number\n")
        j=j-1

    if (num==n):
        print("You choose wright number \n")
        print("Well done you are winner (^_^) ")
        break

    if (j==0):
        print("You are running out of guesses\n")
        print("You lose the game\n Game over")

    i=i+1