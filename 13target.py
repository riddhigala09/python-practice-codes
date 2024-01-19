num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(num)+1):
#     for j in range(i+1, len(num)+1):
#         if i + j == 13:
#             print(i,j)
            

i = 0
j = len(num)-1  
while i < j:
    if num[i] + num[j] == 13:
        print("Pair found:", num[i], num[j])
        i += 1
        j -= 1
    elif num[i] + num[j] < 13:
        i += 1
    else:
        j -= 1
        