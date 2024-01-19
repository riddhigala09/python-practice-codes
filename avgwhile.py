num = []
i=0
sum = 0

while i in range(10):
    n = int(input("Enter a number: "))
    num.append(n)
    i += 1

    sum = sum + n

print(num)

avg = sum / 10

print("Average: ", avg)