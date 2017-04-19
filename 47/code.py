
def primes(k):
    primes = []

    for i in xrange(1,k):
        
        if 0 == k % i:
            primes.append(i)
            while 0 == k % i:
                k = k / i
    return primes
assert primes(644) == [2,7,23]          

all = []
start = 600

all.append(primes(start ))
all.append(primes(start + 1))
all.append(primes(start + 2))

for delta in xrange(3,10000):
    del all[0]
    t = primes ( start + delta)
    all.append( t )
    if (not len(t) == 3) or (not len(all[0]) == 3) or (not len(all[1]) == 3):
        continue

    aset = set()
    set.add(all[0])
    set.add(all[1])
    set.add(all[2])

    if len(aset) == 9:
        print set    
