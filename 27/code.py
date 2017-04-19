#below 10^6
primes = []

#b - list of primes below 1000
b_list = []

file = open('./../100000_primes.txt', 'rb')

for line in file:
    primes += map(int, line.split())
file.close()

def getLen(a,b):
    n = 0
    while n*n+a*n+b in primes:
        n += 1
    return n
assert getLen(1, 41) == 40

b_list = filter(lambda x: x < 1001, primes)
primes = set(primes)
print 
max_len, max_a, max_b = 0, 0, 0

for a in xrange(-1000, 1001):
    for b in b_list:
        #print a,b
        
        if getLen(a,b) > max_len:
            max_len = getLen(a,b)
            max_a, max_b = a, b
        
        if getLen(a,-b) > max_len:
            max_len = getLen(a,-b)
            max_a, max_b = a, -b
print max_len, max_a, max_b, max_a*max_b
        