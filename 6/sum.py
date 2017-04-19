
def sum_2(n):
    sum = 0
    for x in xrange(1, n+1):
        for y in xrange(x+1, n + 1):
            sum += x * y
    return sum * 2
    
def sum(n):
    first =  0
    second = 0
    for x in xrange(1, n + 1):
        first += x
        second += x*x
    return first * first - second
    
#for x in xrange(10, 10000):
#    assert sum(x) == sum_2(x)
print sum_2(100)