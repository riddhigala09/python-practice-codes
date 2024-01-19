n = [1, 2, 3, 5, 6, 7, 8, 10]
m = []

max_num = max(n)

for i in range(max_num + 1):
    if i not in n:
        m.append(i)
    
print("missing numbers in list are: ",m)