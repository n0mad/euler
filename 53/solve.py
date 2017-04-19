const = 1000000
def fact(n):
    if n == 0:
        return 0
        
    res = 1
    for x in xrange(1, n+1):
        res = res * x
    return res
    
def getCount(n):
    n_fact = fact(n)
    t1 = 1
    t2 = fact(n)
    #denom = n_fact / n
    
    for t in xrange(1,n/2 + 1):
        print t1, t2, t
        t1 *= t
        t2 = t2 / (n-t+1)
        
        if n_fact/(t1 * t2) >= const:
            return n - 2*(t) + 1

    return 0
    
    
    
def test():
    assert fact(1) == 1
    assert 24 == fact(4)
    print getCount(5)
    #assert 4 == getCount(23)
test()

#print getCount(10)
#sum = 0
#for x in xrange(22, 101):
#    sum += getCount(x)
#print sum