num = input("Enter a number: ")
i=0
fa =0 
l = len(num)
ono = int(num)

while i < l:
    temp = int(num) % 10
    fa = fa + temp
    num = int(num) // 10

    i += 1

print("Sum of", ono, "is: ", fa)
