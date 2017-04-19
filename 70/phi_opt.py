primes = set([2])

def phi(n):
    denomin = n
    phi = 1
    for prime in primes:
        while denomin % prime == 0:
            denomin = denomin / prime
            phi = phi*(prime-1)
            
            if denomin == 1:
                return phi
                
    for x in xrange(2,denomin+1):
        while 0 == denomin % x:
            denomin = denomin / x
            phi = phi*(x-1)
            if not x in primes:
                primes.add(x)
                
            if denomin == 1:
                return phi
def hasSameDigits(n):
    #toInt = lambda x : int(x)
    
    #n_phi = phi(n)
    #return False
    #n_str = str(n)
    
    #phi_str = str(n_phi)
    #if not len(n_str) == len(phi_str):
    #    return False
        
    #n_digits_sum = sum(map(toInt, n_str))
    #phi_digits_sum = sum(map(toInt, phi_str))
    
    #if not n_digits_sum == phi_digits_sum:
    #    return False
    #if sum(map(lambda x:int(x), str(n)))
    #return False
    phi_n = phi(n)
    if phi_n < 0.1*n:
        return False
        
    a = [].__class__(str(n))
    b = [].__class__(str(phi_n))
    a.sort()
    b.sort()
    
    return a == b
    #return set(str(n)) == set(str(phi(n)))

min = 1000000000
k = -1
for t in xrange(87109+2,87109-2,-1):
    if t % 10 == 0:
        print t
    #if 0 == t % 1000:
    #    print t, len(primes)
    if hasSameDigits(t):
        print '!!!!!!!!!!!' , t, phi(t), t*1.0/phi(t)
        #if t*1.0/phi(t) < min:
            #min = t*1.0/phi(t)
            #k = t
print k, phi(k), min    
#assert  phi(19) == 18
#phi(55)
#phi(197)
#print phi(7)
#print primes
#assert phi(87109) == 79180
#print k, phi(k), min