import time
def digitsSum(n):
    return reduce(lambda x,y:x+y, map(int, str(n)))
    
assert digitsSum(100) == 1
assert digitsSum(12345) == 15


start = time.time()
max = 0
max_b, max_p = 0, 0
for base in xrange(2, 100):
    t = 1
    for power in xrange(1, 100):
        t = t * base
        s = digitsSum(t*base)
        if s > max:
            max = s
            
            max_b = base
            max_p = power
print time.time()  - start
print max

print max_b, max_p