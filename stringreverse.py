s = str(input("Enter a string: "))
revs = ''

for i in s:
    revs = i + revs

print("Reverse of string", s, "is",revs)