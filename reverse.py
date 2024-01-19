num = input("Enter a three digit number: ")
rev = 0
ono = num 

for i in num:
    d = int(num) % 10
    rev = (rev*10) + d
    num = int(num)//10
    
print("Reverse of", ono, "is", rev)