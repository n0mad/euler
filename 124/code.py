N = 100000 + 1

sieve = [[1,n] for n in xrange(N)]

for n in xrange(2, N):
    if sieve[n][0] == 1:
        for t in xrange(n,N,n):
            sieve[t][0] = sieve[t][0]*n
sieve.sort(cmp = lambda x,y: cmp(x[0], y[0]))
print sieve[10000  + 1]
