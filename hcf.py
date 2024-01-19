a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = [], []
for i in range(1,a+1):
    if a % i == 0:
        x.append(i)

for j in range(1,b+1):
    if b % j == 0:
        y.append(j)

print(x)
print(y)

# z = (list(set(x).intersection(y)))
# print(z[-1])
z  = []

for i in x:
    for j in y:
        if i == j:
            #print(i)
            z.append(i)

print(z)
print("Higest comon factor is: ", z[-1])
