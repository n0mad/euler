memoize_sum = {}
memoize = {}
import time
def digitsSqSum_(n):
    if n in memoize_sum:
        return memoize_sum[n]
    tmp = sum(map(lambda x: int(x)*int(x), str(n)))
    memoize_sum[n] = tmp
    return tmp

def digitsSqSum(n):
    if n in memoize_sum:
        return memoize_sum[n]
    #tmp = sum(map(lambda x: int(x)*int(x), str(n)))
    tmp = 0
    while not 0 == n:
        tmp += (n % 10) ** 2
        n = n / 10
        
    memoize_sum[n] = tmp
    return tmp
    
def endsWith89(n):
    t = n
    while (not t == 89) and (not t == 1):
        if t in memoize:
            memoize[n] = memoize[t]
            return memoize[t]
            
        t = digitsSqSum(t)
    if t == 89:
        memoize[n] = True
        return True
    memoize[n] = False
    return False
   

        
assert digitsSqSum(5) == 25
assert digitsSqSum(12) == 5
assert digitsSqSum(44) == 32


count = 0
start = time.time()
for t in xrange(1, 10**7):
    if endsWith89(t):
        count += 1
    if 0 == t % 10000:
        print t
print time.time() - start
print count
