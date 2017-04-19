def makeIteration(previous_set, base_set, bound):
    new_set = set()
    for x in base_set:
        for y in previous_set:
            if x*y < bound:
                new_set.add(x*y)
    return new_set
    
def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in xrange(2, int(x**0.5) + 2):
        if 0 == x % i:
            return False
    return True

BOUND = 10**8
ITERS = BOUND / 2 + 1
TOP = 5

base_set = set( filter(isPrime, range(2,TOP + 1)))
print 'base', base_set
previous_set = range(1, TOP + 1)
print previous_set

for x in xrange(ITERS):
    previous_set = makeIteration(previous_set, base_set, BOUND)
print len(previous_set)
