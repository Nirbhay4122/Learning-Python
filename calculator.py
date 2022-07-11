

print("")
print("")

print("CALCULATOR APP")

print("")
print("")

num1 = int(input("Enter first Number : "))
print("")
print("Choose the operation :")
print("[1.] Choose { + }")
print("[2.] Choose { - }")
print("[3.] Choose { * }")
print("[4.] Choose { / }")
print("")
opr = input()
print("")
a = 1
rslt = 0
while a <= 1:
    if opr == "+":
        print("You choosed Addition (^_^) ")
        print("") 
        num2 = int(input("Enter second Number : "))
        print("") 
        rslt = num1 + num2
        print("") 
        print("Result =>>",num1, opr, num2, "= ", rslt)
        break

    elif opr == "-":
        print("You choosed Subtraction (^_^) ")
        print("")
        num2 = int(input("Enter second Number : "))
        print("")
        rslt = num1 - num2
        print("")
        print("Result =>>",num1, opr, num2, "= ", rslt)
        break

    elif opr == "*":
        print("You choosed Multiplication (^_^) ")
        print("")
        num2 = int(input("Enter second Number : "))
        print("")
        rslt = num1 * num2
        print("")
        print("Result =>>",num1, opr, num2, "= ", rslt)
        break

    elif opr == "/":
        print("You choosed Division (^_^) ")
        print("")
        num2 = int(input("Enter second Number : "))
        print("")
        rslt = num1 / num2
        print("")
        print("Result =>>",num1, opr, num2, "= ", rslt)
        break

    else:
        print("You choose wrong Operation.")

    a += 1

print("")
print("")
input("Press Enter to exit.")
