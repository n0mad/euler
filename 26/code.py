import math
def period(n):
    """ (10, n) = 1, i.e. 10 and n are co-prime"""
    k = 1
    while 1:
        if (10**k - 1) % n == 0:
            return k
        k += 1
assert period(7) == 6
assert period(39) == 6
assert period(3) == 1



max = 0
d = 0
for t in xrange(3, 1000):
    if (t % 2 == 0) or (t % 5 == 0):
        continue
    p = period(t)
    
    if p > max:
        max = p
        d = t
        
        
print 'period of 1/%s is %s'%(d, max)