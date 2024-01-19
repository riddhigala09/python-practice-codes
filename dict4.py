n = int(input("Enter how many items do you want in a dictionary: "))

d = dict()

for i in range(1, n + 1):

    d[i] = i * i

print(d)