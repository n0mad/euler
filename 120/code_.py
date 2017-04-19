def getMaxRemainder(a):
    
    max_n, max_r, n = 1, 0, 3
    result_first = (2*a) % (a*a)
    result = -1
    #n should be odd
    #even n 2n*a % a^2
    #return (2*(pn**odd)*(n**odd)) % (pn*pn)
    a_2 = a**2
    while not result_first == result:
        result = 2*n*a % a_2
        if result > max_r:
            max_n, max_r = n, result
        n = n + 2
    return max_r
assert   42 == getMaxRemainder(7)  

sum = 0
for k in xrange(3, 1001):
    sum += getMaxRemainder(k)
print sum
#    if getRemainder(k, primes[k]) >= 10**10:
#        print k
#        break
        
        
#print time.time() - start