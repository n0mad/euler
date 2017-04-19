import sys
n = int(sys.argv[1])#11
f1 = 1L
f2 = 1L
for x in xrange(1, n + 1):
    if 0 == x % 25:
        f1 = (f1 / 4) * (x / 25)
    elif x % 10 == 0:
        f1 = f1* (x / 10)

    elif 0 == x % 5:
        pass
        f1 = (f1 / 2) * (x / 5)
    else:
    #    
        f1 = f1 * x
    f2 = f2 * x
print f1
print f2
f = str(f1)
sum = 0
for t in xrange(len(f)):
    #print sum
    sum += int(f[t])
print sum