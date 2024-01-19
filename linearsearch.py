num = []
n = int(input("How many numbers do you want? "))
for i in range(n):
    x = int(input("Enter number: "))
    num.append(x)

print(num)

s = int(input("Enter the number you want to search: "))
for i in range(len(num)):
    if num[i] == s:
        print("Number found at position",i)
        break
else:
    print("Number not in list")