import psyco
psyco.full()

BOUND = 10**7
def getPrimes(thres = 3300):
    primes = []
    f = open("./../100000_primes.txt")
    for line in f:
        line = map(int, line.split())
        primes += line
    f.close()
    
    primes = filter(lambda x: x < thres, primes)
    print len(primes)
    return primes
#def hashTableSum(a,b):
#    t = {}
    
#AlreadyCountedPrimes = [{}]  * BOUND 
primes = getPrimes()
primes.reverse()
primesSet = set(primes)


current, prev = 0, 0
def divizors(i):
    lst = {}
    
    #if  i in primesSet:
    #    return 2

    t = i
    #current = 0
    for prime in primes:
        while(t % prime == 0):
            t = t / prime
            lst[prime] = lst.get(prime,0) + 1
    if t > 1:
        lst[t] = 1
    #if current == 0:
    #    return 2
    #r = map(lambda x: x + 1, lst.itervalues())
    #t = reduce(lambda x,y: x * y, r)
    s = 1
    for k in lst.itervalues():
        s = s * (k + 1)
    return s
    
    #return reduce(lambda x, y: lst.values()    
    #return 2 ** current
c,p = 0,0
t = 0    
for k in xrange(2, BOUND):
    p = c
    c = divizors(k)
    #print k, c
    if p == c:
        
        t += 1
print t
    #t = k
    #prev = current
    #current = 0
    #print k, divizors(k)
    #print k, 1 + 2 ** current
