from itertools import izip

import psyco
psyco.full()

set   = [6, 9, 11, 12, 13]
flags = [0, 0,  0,  0,  0]
def check(s, f):
    s1 = 0
    s2 = 0
    for item, flag in izip(s,f):
        if flag == 1:
            s1 += item
        else:
            s2 += item
    return s1 == s2
    
for i in xrange( 2**(len(set) )):
    #print i
    #generate flags
    k = i
    for pos in xrange( len(flags) - 1, -1, -1):
        flags[pos] = k % 2
        k = k / 2
    #print flags
    if check(set, flags):
        print set, flags