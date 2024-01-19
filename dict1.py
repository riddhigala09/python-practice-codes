k = 1
v = 10

d = dict()
n = int(input("Enter how many numbers do you want: "))

for k in range(1, n + 1):
    k = k + 1
    v = v + 10
    d[k] = v

print(d)