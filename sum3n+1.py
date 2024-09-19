for i in range(1,100000000):

    n = i

    while n != 1:

        if n % 2 == 1:

            n = n * 3 + 1
        
        else:

            n /= 2
    
    print(i, "pass")