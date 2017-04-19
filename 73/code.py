strict_bound = 10000 + 1
count = 0
def gcd(a,b):
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
        
def areCoprime(n,m):
    if gcd(n, m) == 1:
        return True
    return False
    
    
import time
start = time.time()

assert areCoprime(7,3)
assert areCoprime(100,3)

for d in xrange(2, strict_bound):
    a = int(1.0/3 * d) + 1
    b = int(1.0/2 * d)# - 1
    for e in xrange(a, b):
        if (float(e)/d <= 1.0/3):
            continue
            
        if (float(e)/d >= 0.5):
            break
        if areCoprime(d,e):
            count +=1
    if d % 100 == 0:
        print d
print count, time.time() - start
