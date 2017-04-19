def triangle(n):
    return n*(n-1)/2
def pentagonal(n):
    return n*(3*n-1)/2
def hexagonal(n):
    return n*(2*n - 1)
    
    
tri_set = set()
pent_set = set()
hex_set = set()

#n1, n2, n3 = 1,1,1
for t in xrange(1, 100000):
    tri = triangle(t)
    if ((tri in pent_set) and (tri in hex_set)):
        print tri
    else:
        tri_set.add(tri)
    pent_set.add(pentagonal(t))
    hex_set.add(hexagonal(t))