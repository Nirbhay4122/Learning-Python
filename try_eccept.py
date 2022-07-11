print("Enter the first number:-")
num1 = input()
print("Enter the second number:-")
num2 = input()
try:
    print("The sum of the number is:-", int(num1)+int(num2))
except Exception as n:
    print(n)

print("Now choose a number:-")
num3 = int(input())
print("Your choosen number is:", num3)
    