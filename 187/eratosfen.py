
k = 50000000
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
#print len(cell)
for x in primes:
    print x