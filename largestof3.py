num = []

for i in range(3):
    n = int(input("Enter a number: "))
    num.append(n)

print(num)

if num[0] > num[1] and num[0] > num[2]:
    print(num[0], "is Largest")

elif num[1] > num[0] and num[1] > num[2]:
    print(num[1], "is largest")

else:
    print(num[2], "is Largest")