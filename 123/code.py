def readPrimes():
    primes = []
    file = open('./../100000_primes.txt', 'rb')
    for line in file:
        primes += map(int, line.split())
    file.close()
    return primes
    
assert getRemainder(3,5) == 5
assert getRemainder(4,7) == 2
import math,time
primes = readPrimes()

def getRemainder(n, pn):
    odd = n % 2
    # res is C(n,0)[1 + (-1)^(n)] + C(n,1)[1 + (-1)^(n+1)]pn
    #even n 2n*a % a^2
    return (2*(pn**odd)*(n**odd)) % (pn*pn)
    
start = time.time()

for k in xrange(3, 100000, 2):
    if getRemainder(k, primes[k]) >= 10**10:
        print k
        break
        
        
print time.time() - start