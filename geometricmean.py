from squareroot import sqrt

i = 0 
p = 1

n = int(input("How many nos do you want? "))
for i in range(n):
    x = int(input("Enter number: "))
    p = p * x

gmean=sqrt(p)
print(gmean)