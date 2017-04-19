def count(i, floor, hash={}):
    #print "f(%s,%s)=?"%(i, floor)
    #if i == floor:
    #    print "f(%s,%s)=1"%(i, floor)
    #    return 1
    if i == 0:
        #print "f(%s,%s)=1"%(i, floor)
        return 1
    elif i < floor:
        #print "f(%s,%s)=0"%(i, floor)
        
        return 0
    else:
        sum = 0
        for k in xrange(floor, i+1):
            if (i-k, k) in hash:
                sum += hash[i-k, k]
            else:
                sum += count(i-k, k)
        #print 'f(%s,%s)=%s'%(i, floor,sum)
        hash[(i, floor)] = sum
        return sum
        

        
        
        
        
import sys


assert count(5,1) == 7
assert count(4,1) == 5
assert count(2,1) == 2


print count(100,1)

#i = 5
#while True:
#    if i % 1000 == 0:
#        print i
#    if count(i, 1) % 1000000 == 0:
#        print i
#        break
#    i += 1    