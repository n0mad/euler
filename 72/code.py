all = set()

for d in xrange(1, 10**6):
    for n in xrange(1,d):
        all.add(1.0*n/d)
        
print len(all)