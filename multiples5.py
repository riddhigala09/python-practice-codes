num = int(input("enter a number: "))

def multi(num):
    
    x = 0

    x = num % 5
    if x == 0:
        print(num, "is a multiple of 5")

    else: 
        print(num,"is not a multiple of 5")

multi(num)