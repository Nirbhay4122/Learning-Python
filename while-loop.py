# ..............................
# while loop
# ..............................

# num = 1
# while num <= 10:
#     print("This while loop.")
#     num += 1

# printing up triangle using while loop

# num = 1
# a = 1
# while num <= 5:
#     if num == 1:
#         print("*", end="")
#         print("")
#     if num == 2:
#         while a <= 2:
#             print("*", end=" ")
#             if a == 2:
#                 print("")
#             a += 1
#     if num == 3:
#         while a <= 3:
#             print("*", end=" ")
#             if a == 3:
#                 print("")
#             a += 1
#     if num == 4:
#         while a <= 4:
#             print("*", end=" ")
#             if a == 4:
#                 print("")
#             a += 1
#     if num == 5:
#         while a <= 5:
#             print("*", end=" ")
#             a += 1
#     a = 1
#     num += 1


# printing down triangle using while loop

siz_p = int(input("Enter size of pyramid : "))
whlp = 1
num = 1
a = 1

print("This triangle is printed by while loop.")
print("")
print("")

while num <= siz_p:
    if num == a:
        while a <= siz_p:
            print("*", end=" ")
            if a == siz_p:
                print("")
            a += 1
    whlp += 1
    a = whlp
    num += 1

print("")
print("")

input("press Enter to exit")

# print("a = ", a)
# print("a = ", a)
# print("num = ", num)
