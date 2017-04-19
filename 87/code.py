file = open('./../100000_primes.txt')
primes = []
for line in file:
    primes +=  map(int, line.split())
file.close()
    
primes_x = filter(lambda x: x < (50*10**6)**0.5, primes)
primes_y = filter(lambda x: x < (50*10**6)**(1.0/3), primes)
primes_z = filter(lambda x: x < (50*10**6)**(1.0/4), primes)


l = len(primes)
print len(primes_x)*len(primes_y)*len(primes_z)
count = 0
s = set()
import time
start = time.time()
for x in primes_x:
    for y in primes_y:
        for z in primes_z:
            #count += 1
            #if 0 == count % 100000:
            #    print count
            n = x*x + y*y*y + z*z*z*z
            if n < 50 * 10**6:
                s.add(n)
                
                
print time.time() - start, len(s)
