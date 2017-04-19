def getDivizors(n):
    a, b = 0, 0
    
    if (n + 1) % 2 == 0:
            a,b =  n, (n + 1)/2
    else:
        a,b = n + 1, n/2
    #print 'n-th is '    , a ,'*', b
    count_a, count_b = 0    ,  0
    for factor in xrange(1, 1 + a):
        if a % factor == 0:
            count_a += 1
            #print '!', factor
        if b % factor == 0:
            #print '!', factor
            count_b += 1
    return count_a * count_b# - 1   


#print getDivizors(5)
assert getDivizors(5) == 4
assert getDivizors(7) == 6


divizors = 500
n = 1
while 1:
    if divizors < getDivizors(n):
        print getDivizors(n), n, n*(n+1)/2
        break
    n = n + 1
    if n % 100 == 0:
        print n