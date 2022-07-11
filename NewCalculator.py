Result= 0
num1= int(input("Enter the first number:-"))
print("You can choose the operation")
print("For Addition=[+]")
print("For Substraction=[-]")
print("For Multiplication=[*]")
print("For Devidation=[/]")
print("For modulo=[%]")
print("Now choose operatin::(^_^)")
opt= (input())
num2= int(input("Enter the second number:-"))
Addition= '+'
Substraction= '-'
Multiplication= '*'
Devidation= '/'
Modulo= '%'

#For addition
if(opt==Addition):
    Result=num1+num2
    print(Result)

#For substraction
if(opt==Substraction):
    Result=num1-num2
    print(Result)

#For multiplication
if(opt==Multiplication):
    Result=num1*num2
    print(Result)

#For Devidation
if(opt==Devidation):
    Result=num1/num2
    print(Result)

#For modulo
if(opt==Modulo):
    Result=num1%num2
    print(Result)