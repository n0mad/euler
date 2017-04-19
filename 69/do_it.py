primes = set([2])

def phi(n):
    denomin = n
    phi = n
    for prime in primes:
        if denomin % prime == 0:
            phi = phi * (1 - 1.0/prime)
            if denomin == 1:
                return phi
                
            while denomin % prime == 0:
                denomin = denomin / prime
                if denomin == 1:
                    return phi
                
    for x in xrange(2,denomin+1):
        
        if denomin % x == 0:
            phi = phi * (1 - 1.0/x)
            if not x in primes:
                primes.add(x)
                
            if denomin == 1:
                return phi
                
            while 0 == denomin % x:
                denomin = denomin / x

                    
                if denomin == 1:
                    return phi

max = -1
k = -1
assert phi(2) == 1
assert phi(8) == 4
for t in xrange(2, 10**6):
    #if t % 1000 == 0:
    #    print t
    if t*1.0/phi(t) > max:
        print t, phi(t), t*1.0/phi(t)
        max = t*1.0/phi(t)
        k = t
print k, phi(k), max