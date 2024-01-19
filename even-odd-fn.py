num = input("Enter a number: ")

def even_odd_fn(num):

    x = int(num) % 2

    if x==0:
        print("Even")

    else:
        print("Odd")

even_odd_fn(num)