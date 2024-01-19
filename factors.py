n = int(input("Enter a number: "))
a = ''
for i in range(1,n+1):
    if n  % i == 0:
        a += str(i) + ', ' 

print("Factors of ", n, "are: ", a)