def Zeckendorf(n):
    fib = [1,1]
    while(fib[-1] < n):
        fib.append(fib[-1]+fib[-2])
    zeck = [0 for i in fib]
    for i in range(2,len(fib)):
        zeck[i] = zeck[i-1] + zeck[i-2] + fib[i-2]
    print zeck
    
    s = 0
    for i in range(len(fib)-1, -1, -1):
        if n >= fib[i]:
            s += zeck[i]
            n -= fib[i]
            s += n
    return s
 
#print Zeckendorf(10**6)
print Zeckendorf(10**6)