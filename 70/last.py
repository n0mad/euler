def hasSameDigits(n,k):
    if (k < 0.1*n) or (n < k*0.1):
        return False
        
    a = [].__class__(str(n))
    b = [].__class__(str(k))
    a.sort()
    b.sort()
    
    return a == b
    
cell = range(2, 10000)
primes = []

for k in xrange(len(cell)):
    if cell[k] == -1:
        continue
    prime,cell[k] = cell[k], -1
    #if prime > 10**3:
    primes.append(prime)
    
    for t in xrange(1, 1 + (len(cell)+2)/prime):
        #print 'prime: ', prime, ' t: ', t, ' cell ', cell
        try:
            cell[t*prime - 2] = -1
        except:
            pass

#print primes
min = 100
k = -1
for p1 in xrange(len(primes)):
    for p2 in xrange(p1):
        t1 = primes[p1]
        t2 = primes[p2]
        if (t1*t2 < 10**7) and (hasSameDigits(t1*t2, (t1-1)*(t2-1))):
            if min > t1*t2*1.0/((t1-1)*(t2-1)):
                min = t1*t2*1.0/((t1-1)*(t2-1))
                k = t1*t2
print k
print min