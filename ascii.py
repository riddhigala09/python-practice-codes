st = input("Enter a string: ")
l1 = []

for i in st:
    l1.append(ord(i))

print(l1)

for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[j] >= l1[i]:
            l1[j], l1[i] = l1[i], l1[j]
        
print(l1)

for k in range(len(l1)):
    print(chr(l1[k]), end='')