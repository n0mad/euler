k = 775146
cell = range(2, 1+k)
primes = []

import time
time1 = time.time()
for k in xrange(len(cell)):
    if cell[k] == -1:
        continue
    prime,cell[k] = cell[k], -1
    primes.append(prime)
    
    for t in xrange(1, 1 + (len(cell)+2)/prime):
        #print 'prime: ', prime, ' t: ', t, ' cell ', cell
        try:
            cell[t*prime - 2] = -1
        except:
            pass
        #if prime == 2:
        #    print cell#print t
        
#print primes
#print cell
#print reduce(lambda x,y: x + y, primes)
print time.time() - time1
import array

time1 = time.time()
cell = array.array('i', [0])*(k+2) #numpy.zeros(k+2)
cell[0], cell[1] = -1, -1
primes = []

for prime in xrange(2, k):
    if cell[prime] == -1:
        continue
    primes.append(prime)
    cell[k] = -1
    for t in xrange(1, 1 + (k/prime)):
        #print k*prime
        try:
            cell[t*prime] = -1
        except:
            pass
print time.time() - time1
#print cell#
#print primes