# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

N = int(input("Enter length of list: "))
lis = input("Enter element of list: ")
lis = lis.split(" ")
are_all_negative = all(int(x) > 0 for x in lis)

if are_all_negative == True:
    print(any(str(x) == str(x)[::-1] for x in lis))
else:
    print('False')