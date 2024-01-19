n = input("Enter a number: ")
s = 0
i = 0
ono = n
l = len(n)

while i < l:
    temp = int(n) % 10
    s = s + temp
    n = int(n) // 10

    i += 1

print("Sum of",ono, "is: ", s)

if s % 2 == 0:
    print(s, "is an even number")

else: print(s, "is an odd number")
