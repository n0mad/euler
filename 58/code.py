def getNumbers(layer):
    k = layer
    return 4*k*k+4*k+1, 4*k*k+2*k+1, 4*k*k+1, 4*k*k - 2*k + 1
    
def isPrime(n):
    for x in xrange(2, int(n**0.5) + 1):
        if 0 == n % x:
            return False
    return True
    
assert (1,1,1,1) == getNumbers(0)
assert (9,7,5,3) == getNumbers(1)


assert isPrime(7)
assert not isPrime(93)
k = 1
prime, total = 0,1
import time
start = time.time()
while 1:
    numbers = getNumbers(k)
    total += len(numbers)
    prime += len(filter(isPrime, numbers))
    #print 'primes %s, total %s, k %s'%(prime, total, k) 
    if prime*1.0/total < 0.1:
        print 'primes %s, total %s, k %s'%(prime, total, k) 
        print 2*k+1
        break
    k += 1
    
print 'time: ', time.time() - start