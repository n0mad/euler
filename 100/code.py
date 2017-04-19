import psyco
psyco.full()

def getBlueDiscs(total):
    D = (1 + 2*(total - 1)*total)**0.5
    a =  (1.0 + D)/2
    
    return a
    
    
assert getBlueDiscs(85+35) == 85
assert getBlueDiscs(21) == 15

t = 10**12

while True:
    r = getBlueDiscs(t)
    if r == long(r):
        a = r
        total = t
        if a * (a - 1) *2 == t * (t - 1):
            print '!!!!!!!!!!', a, t
            break
        
        #print t, a, t > 10**12
        #break
    t += 1
    