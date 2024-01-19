dict1 = {
    "1":"10",
    "2":"20",
    "3":"30",
    "4":"40"
}

n = str(input("Enter which key you want to search?"))

if n in dict1:
    print("Key exists")
    v = dict1.get(n)
    print("Value of key", n, "is", v)

else:
    print("Key doesn't exists")