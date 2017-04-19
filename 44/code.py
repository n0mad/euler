import psyco
psyco.full()

def isInt(x):
    return x == int(x)
    
def isP (x):
    D = 1 + 24 * x
    if not isInt(D**0.5):
        return False
    n_1 = (1 + D**0.5)/6
    n_2 = (1 - D**0.5)/6
    
    if ((n_1 > 0) and ( isInt(n_1))):
        return True
    
    if ((n_2 > 0) and ( isInt(n_2))):
        return True
        
    return False
    
    
for x in [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]:
    assert isP(x)

for x in [2,3,11, 100]:
    assert not isP(x)
    
    
for k in xrange(1,10000):
    for j in xrange(k,10000):
        p1 = k*(3*k-1)/2
        p2 = j*(3*j-1)/2
        
        if isP(p1 + p2) and ( isP( p2-p1 )):
            print p1,p2, p1+p2, p2 - p1