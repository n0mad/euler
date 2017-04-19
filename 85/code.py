#3x2 = 18


#fixing left-upper corner at (X,Y) we have (a-X)*( b - Y) rectangles


#=> Sum (X < a, Y < b) (a-X)(b-Y)

#(b+1)b/2 * (a+1)*a/2
def rects(k,n):
    return (k+1)*k*n*(n+1)/4

import math
closest_d, closest_a, closest_b = 2000, 0, 0
for a in xrange(2000):
    for b in xrange(a):
        res = rects(a,b)
        
        if abs(res - 2000000) < closest_d:
            closest_d = abs(res - 2000000)
            closest_a, closest_b = a, b
print closest_a, closest_b