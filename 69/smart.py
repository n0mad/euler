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
import sys
mul = 1
for prime in primes:
    mul = mul * prime
    if mul > 10**6:
        print mul / prime
        sys.exit()