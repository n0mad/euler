import psyco
psyco.full()
def gcd(a,b):
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
        
L = 1500000
sieve = [ 0 for x in xrange(L + 1)]
sqrtL = int(L**0.5) + 1

for n in xrange(1,sqrtL):
    for m in xrange(n + 1, sqrtL):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if 1 != gcd(a, b):# or a > b:
            continue
        #if (a,b,c) == (30, 40, 50):
        #    print "!", a, b, c
        p = a + b + c
        factor  = 1
        while p * factor <= L:
            #print p * factor, ": " , factor * a, factor * b, factor * c
            sieve[p * factor] += 1
            factor += 1
 
#print sieve
total = 0
for k in sieve:
    if k == 1:
        total += 1
print total