dict1 = {
    1:10,
    2:20,
    3:30,
    4:40,
    5:50
}

n = int(input("Enter which item you want to remove: "))

dict1.pop(n)

print(dict1)