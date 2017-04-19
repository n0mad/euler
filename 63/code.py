import math
import time

start = time.time()
power = 1
counter = 0


power_bound = 20+int(math.ceil(-1.0/(math.log10(0.9))))
#print power_bound
for power in xrange(1, power_bound):
    upper_bound = 1 + int(math.ceil(10 * (10**(1.0/power))))
    for x in xrange(1, upper_bound + 1):
        if (x**power > 10**(power-1)) and (x**power < 10**(power)):
            counter+= 1
            #print "%s\^%s"%(x, power),
            #assert len(str(x**power)) == power
    #print 
    
print time.time() - start
print counter + 1