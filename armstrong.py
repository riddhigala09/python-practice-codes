s = 0
n = int(input("Enter a number: "))
x = len(str(n))
ono = n

for i in range(n):
    temp = n % 10
    c = temp ** x
    s = c + s
    n = n // 10
    if s == ono:
        print(ono, "is Armstrong")
        break
else: 
    print(ono, "is not Armstrong")

    
