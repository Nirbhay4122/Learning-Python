def addition():
    """This function add only two numbers."""
    a = int(input("Enter first number:-\n"))
    b = int(input("Enter second number:-\n"))
    c = a + b
    print("Result = ", c)

def substraction():
    """This function substract only two numbers."""
    a = int(input("Enter first number:-\n"))
    b = int(input("Enter second number:-\n"))
    c = a - b
    print("Result = ", c)

def multiplication():
    """This function multiply only two numbers."""
    a = int(input("Enter first number:-\n"))
    b = int(input("Enter second number:-\n"))
    c = a * b
    print("Result = ", c)

def division():
    """This function divide only two numbers."""
    a = int(input("Enter first number:-\n"))
    b = int(input("Enter second number:-\n"))
    c = a / b
    print("Result = ", c)

def modulo():
    """This function gave remainder."""
    a = int(input("Enter first number:-\n"))
    b = int(input("Enter second number:-\n"))
    c = a % b
    print("Result = ", c)

def square():
    """This function calculate th square."""
    a = int(input("Enter a number:-\n"))
    c = a * a
    print("Result = ", c)

while(True):
    print("Choose operation to execute.")
    print("Select - [ 1 ] - Addition\nSelect - [ 2 ] - Substraction\nSelect - [ 3 ] - Multiplication\nSelect - [ 4 ] - Devision\nSelect - [ 5 ] - Modulo\nSelect - [ 6 ] - Square\n")
    opt = int(input())
    if(opt < 1 or opt > 6):
        print("Wrong operation.\nKeep calm and choose wright option =>")
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 1):
        addition()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 2):
        substraction()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 3):
        multiplication()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 4):
        division()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 5):
        modulo()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break
    elif(opt == 6):
        square()
        con = input("\nWant cantinue Press [ 'Y' ]\nWant terminate Press [ 'N' ]\n")
        if(con == 'y' or con == 'Y'):
            continue
        else:
            break