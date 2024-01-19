a = str(input("Enter first string: "))
b = str(input("Enter second string: "))

for i in a:
    for j in b:
        if i == j:
            print("Common characters: ", i)
            continue
    
        #else:
         #   print("Uncommon characters are: ", i, j)