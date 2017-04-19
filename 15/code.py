HASH = {}
def F(k, n):
    if (k, n) in HASH:
        return HASH[(k,n)]
    if (n, k) in HASH:
        return HASH[(n,k)]
    if k == 1:
        return n+1
    if n == 1:
        return k+1
    sum = 0
    for n_ in xrange(0, n+1):
        sum += F(k-1, n_)
    HASH[(k,n)] = sum
    return sum
print F(20,20)