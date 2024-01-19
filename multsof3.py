def mults3():
    a = ''
    for i in range(10,52):
        if (i % 3 == 0):
            a += str(i) + ', '
            
    print("Multiples of 3 in range of 10 and 52 are: ", a)            
mults3()
