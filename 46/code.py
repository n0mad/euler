import numpy
primes = []
prime_file = open('./../100000_primes.txt', 'rb')
for str in prime_file:
    primes += map(int, str.split())
prime_file.close()

primes = numpy.array(primes)

length = len(primes)
assert 7 in primes
for x in xrange(2, primes.max()+2):
    if x % 2 == 0:
        continue
    if x in primes:#.searchsorted(x) == length:
        #thats a prime
        continue
    isPresented = False
    
    for prime in primes:
        if prime > x:
            break
        #print prime,
        t = x - prime
        #print t,
        if (t % 2 == 0) and ((t/2)**0.5 == int((t/2)**0.5)):
            isPresented = True
            #print '%s = %s + 2 * %s'%(x, prime, t/2)
            break
    if not isPresented:
        print x, prime
        break
        
            