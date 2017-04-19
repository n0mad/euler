def C(n,k):
    c = 1
    if k < n - k:
        k = n - k
    for t in xrange(k + 1, n + 1):
        c = c * t
    for t in xrange(2, n - k + 1):
        c = c / t
    return c
def isSquareFree(k):
    for m in xrange(2, 1 + int(k**0.5)):
        if (0 == k % m) and (0 == k % (m*m)):
            return False
    return True


assert C(5,2) == C(5,3) == 10
assert C(5,0) == 1

assert True == isSquareFree(2)
assert False == isSquareFree(4)
assert False == isSquareFree(98)

uniq = set()
rows = 51
for n in xrange(1, rows):
    for k in xrange(0, n/2 + 1):
        Cnk  = C(n,k)
        if isSquareFree(Cnk):
            uniq.add(Cnk)
print reduce(lambda x,y: x + y, uniq)
            