x = int(input("Enter the list size: "))
num = []
sum = 0

for i in range(int(x)):

    print("Enter number at position", i, ":")
    n = int(input())

    num.append(n)

    sum = sum + n

average = sum/x

print("The list is: ",num)
print("The average of sets of integers is: ", average)