num = int(input("Enter a number: "))
x = int(num / 2)

def checksqrt(num):
    
    for i in range(x+1):
        if i * i == num:
            print(num, "is a perfect square and Square Root of", num,"is: ", i)
            break

    else: 
        print(num, "is not a Perfect Sqaure")

checksqrt(num)