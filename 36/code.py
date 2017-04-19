import math
def isBase10Poly(n):
    s = str(n)
    
    for t in xrange(len(s)/2):
        if not s[t] == s[-t-1]:
            return False
    return True

def isBase2Poly(n):
    max = int(math.log(n)/math.log(2)) + 1
    #print n, max
    for t in xrange(max/2):
        #print ((n >> t ) & 1), ((n >> (max - t) ) & 1)
        if not ((n >> t ) & 1) == ((n >> (max - t - 1) ) & 1):
            return False
    return True
    
assert isBase10Poly(101)
assert isBase10Poly(10101)
assert isBase10Poly(585)
assert not isBase10Poly(1015)
assert not isBase10Poly(107403)
assert isBase2Poly(3)
assert isBase2Poly(585)

sum = 0
for x in xrange(1, 1000000):
    if (isBase2Poly(x) and isBase10Poly(x)):
        print x
        sum += x
print 'sum:', sum