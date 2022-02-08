def weirdAlgo(n):
    num = []
    while(n>1):
        if n%2 == 0:
            n /=2
            num.append(n)
           
        else:
            n = 3*n + 1
            num.append(n)

    
        

    return list(num)

print(weirdAlgo(5))