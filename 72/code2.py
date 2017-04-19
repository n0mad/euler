bound = 10**6+1#10**5+1
def phi(n, hash = {}):
    denomin = n
    phi = 1
    for x in xrange(2,n+1):
        #print x, denomin
        if 0 == denomin % x:
            phi = phi*(1 - 1.0/x)
            while 0 == denomin % x:
                denomin = denomin / x
                phi = phi * x
            if denomin in hash:
                hash[n] = int(hash[denomin]*phi)
                return int(hash[denomin]*phi)
        if denomin == 1:
            hash[n] = phi
            return int(phi)
assert phi(7) == 6
assert phi(36) == 12
    
sum = 0
import time
start = time.time()
for denom in xrange(2, bound):
    if denom % 10000 == 0:
        print denom
    sum += phi(denom)
#import math
print 'calc ', bound , ' took ', time.time() - start
print 'strict sum is' , sum
#print 3.0/(math.pi**2)*(bound**2)