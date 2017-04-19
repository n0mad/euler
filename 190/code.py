def calc(m):
    list = [0 for i in xrange(m)]
    m = len(list)
    list[0] = 2.0/(m + 1)
    
    for k in xrange(1, len(list)):
        list[k] = list[0] * (k+1)
    return list

def P(list):
    prod = 1
    for k in xrange(len(list)):
        prod = prod * (list[k] ** (k+1))
    return int(prod)
    
m = 10
list = calc(m)
print P(list)
s = 0
for m in xrange(2,16):
    list = calc(m)
    s += P(list)
print s
