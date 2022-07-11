# zero = "0"
# one = "1"
# two = "2"
# three = "3"
# four = "4"
# five = "5"
# six = "6"
# seven = "7"
# eight = "8"
# nine = "9"

arr = [1, 3, 2, 3, 1, 5, 6, 4, 5]
k = 1
# arr[j] = arr[k]
for i in range(9):
    for l in range(9):
        # print(arr[i])
        # print(arr[k])

        if arr[i] == arr[k]:
            print(arr[i])
            # print("*")
        
        k += 1
        if k == 9:
            break    
    k = 1
# while i <= 8 :
#     if arr[j] == arr[k]:
#         print(arr[j])
#         i = 0

#     j += 1
#     k += 1
#     i += 1
#     if k > 8:
#         break
