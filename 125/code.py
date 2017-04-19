bound = 10**8#+20000000
def isPolyndrom(k):
    k = str(k)
    for i in xrange(len(k)/2):
        if not k[i] == k[len(k)-1-i]:
            return False
    return True
    
    
assert isPolyndrom(595)
assert isPolyndrom(5995)
assert not isPolyndrom(5950)

count = 0
poly_sum_poly = 0

list = []

for x in xrange(1, bound):
    sum_poly = x*x
    if sum_poly >= bound:
        break
    #if x % 100 == 0:
    #    print x
    for offset in xrange(1, bound):

        
        sum_poly += (x+offset)**2
        if sum_poly >= bound:
            break
        if isPolyndrom(sum_poly):
            #print sum_poly
            count += 1
            poly_sum_poly += sum_poly
            list.append(sum_poly)
print 'count', count
print 'sum_poly', poly_sum_poly

print len(list), sum(list)
print list[-1] < bound