def seqLen(n, hash={}):
    start = n
    seqLen = 1
    if n in hash:
        return hash[n]
        
    while not 1 == n:
        if n in hash:
            return hash[n] + seqLen
        if 0 == n % 2:
            n = n / 2
        else:
            n = n * 3 + 1
        seqLen += 1
    hash[start] = seqLen
    return seqLen
#print  seqLen(13)
assert seqLen(13) == 10


max, max_n = 0, 0

for x in xrange(2, 1000000):
    l = seqLen(x)
    if  l > max:
        max = l
        max_n = x
    #if 0 == x % 1000:
    #    print x
print max_n, max