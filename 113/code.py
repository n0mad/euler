def F(a, k, hash = {}):
    #k - digits, that starts with a and are decreasing
    if k == 1:
        return 1
    if (a,k) in hash:
        return hash[(a,k)]
    sum = 0
    
    for t in xrange(a+1):
        sum += F(t, k - 1)
    hash[(a,k)] = sum
    return sum    

assert F(1,2) == 2
   
    
def S(k):
    #k = k - 1
       
    sum = 1
    for t in xrange(1, 10):
        for digits in xrange(1, k+1):
            sum += 2* F(t, digits) - 1
    return sum
print S(1)
assert S(1) == 10
print S(2)
#assert S(2) == 100
print S(6)
