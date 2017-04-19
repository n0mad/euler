bound = 51
def dotProduct(a,b):
    return a[0]*b[0] + a[1]*b[1]
    
def isRight(x1,y1, x2,y2):
    a = x1 , y1
    b = x2, y2
    c = x1-x2, y1-y2
    #print a,b,c
    return (dotProduct(a,b) == 0) or (dotProduct(a,c) == 0) or (dotProduct(b,c) == 0)
assert isRight(1,0,0,1)


assert isRight(1,0, 1, 1)
counter = 0    
for x1 in xrange(0, bound):
    for y1 in xrange(0, bound):
        if (x1 == 0) and (y1 == 0):
            continue
        for x2 in xrange(0, bound):
            for y2 in xrange(0, bound):
                
                if (x2 == 0) and (y2 == 0):
                    continue
                if (x1 == x2) and (y1 == y2):
                    continue
                if isRight(x1, y1, x2, y2):
                    #print x1,y1, x2,y2
                    counter += 1
                    
                    
print counter/2