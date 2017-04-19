known_primes = []

def phi(n):
    denomin = n
    phi = 1
    for x in xrange(2,n+1):
        #print x, denomin
        while 0 == denomin % x:
            denomin = denomin / x
            phi = phi*(x-1)#phi * (1 - 1.0/x)
            
        if denomin == 1:
            return int(phi)
    
def hasSameDigits(n):
    return set(str(n)) == set(str(phi(n)))

min = 1000000000
k = -1

for t in xrange(2, 10**7):
    if 0 == t % 1000:
        print t
    if hasSameDigits(t):
        if t*1.0/phi(t) < min:
            min = t*1.0/phi(t) #print t, phi(t)
            k = t
    
#assert  phi(7) == 6
#assert phi(87109) == 79180
print k, phi(k), min