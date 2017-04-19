from math import *

def Cnk(n,k):
    if (k == 0) or (k == n):
        return 1
        
    Cnk = 1
    k_max = max(k, n - k)
    k_min = min(k, n - k)
    for n_ in xrange(k_max+1, n+1):
        Cnk = Cnk * n_
    for k_ in xrange(2, k_min + 1):
        Cnk = Cnk / k_
        
    return Cnk
    
def isDivisible1(n,k):
    if int(log(n,7)) > int( log(k,7) + log(n-k, 7)):
        return True
    return False
    
    
def isDivisible2(n,k):
    return 0 == Cnk(n,k) % 7
    
def isDivisible3(n,k):


    if counter(n) > counter(n-k) + counter(k):
        return True
    return False
total = 0
count = 0
def getCount(n):
    if n == 0:
        return 1
    return 2 + 2*(n % 7)
 
#for n in xrange(0, 100):
#    count += getCount(n)
#    total += n + 1
for n in xrange(53,54):
    for k in xrange(0, n + 1):
        total += 1
        if not isDivisible2(n,k):
            #print n,k
            count += 1
            #print n,k
        #if not (isDivisible2(n,k) == isDivisible3(n,k)):
        #    print n,k, isDivisible2(n,k), isDivisible3(n,k),  Cnk(n,k), counter(n), counter(n-k) , counter(k)
        ##    exit()
print total, count