num = int(input("Enter a number: "))

def check(num):
    if num % 5 == 0 and num % 7 == 0:
        print(num, "is a multiple of 5 and 7")

    else:
        print(num, "is not a multiple of 5 and 7")

check(num)