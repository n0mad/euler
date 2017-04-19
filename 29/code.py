the_set = set()

for a in xrange(2,101):
    for b in xrange(2,101):
        the_set.add(a**b)
        
        
print len(the_set)