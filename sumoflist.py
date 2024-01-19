sum = 0
num = []

n = int(input("How many numbers do you want? "))

for i in range(n):
    x = int(input("Eneter number: "))
    num.append(x)

print(num)

for i in num:
    sum = sum + i

print("Sum of elements of list", num, "is: ", sum)