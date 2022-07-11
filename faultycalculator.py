result = 0
while(True):

    num1 = int(input("Enter your first number = "))
    num2 = int(input("Enter your second number = "))
    opt = input("Choose your operator ['+' '-' '*' '/']\n")
    add = '+'
    mul = '*'
    dev = '/'
    sub = '-'
    if num1==56 and num2==9 and opt=='+':
        result = 77
        print("Your result is = ",result)

    elif num1==45 and num2==3 and opt=='*':
        result = 555
        print("Your result is = ",result)

    elif num1==56 and num2==6 and opt=='/':
        result = 4
        print("Your result is = ",result)

    elif opt=='+':
        result = num1+num2
        print("Your result is = ",result)

    elif opt=='-':
        result = num1-num2
        print("Your result is = ",result)

    elif opt=='*':
        result = num1*num2
        print("Your result is = ",result)

    elif opt=='/':
        result = num1/num2
        print("Your result is = ",result)

    print("\nFor cantinue press  [ 'Y' or 'y' ]\n")
    print("For terminate [ You are Free ]\n")
    yes = input()
    if yes == 'y' or yes == 'Y':
        continue
    else:
        break