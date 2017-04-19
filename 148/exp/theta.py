def counter(a):
    k = 7
    count = 0
    while (a >= k):
        count += a / k
        k = k * 7
    return count
    
def phi(n,k):
    if counter(n) ==  counter(n-k) + counter(k):
        return 1
    return 0
def theta(n):
    sum = 0
    for k in xrange(0, n + 1):
        sum += phi(n,k)
    return sum
def add(n):
    sum = 0
    for k in xrange(n - 6, n + 1):
        sum += phi(n,k)
    return sum
for k in xrange(340, 370):
    print 'theta(%s) =  %s'%(k, theta(k))