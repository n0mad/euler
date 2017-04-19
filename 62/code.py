def getClassName(i):
    lst = []
    while i > 0:
        lst.append(i % 10)
        i = i / 10
    lst.sort()
    
    t = 1
    sum = 0
    
    for k in lst:
        sum += t * k
        
        t = t * 10
    return sum
    
assert getClassName(123) == getClassName(321)
#print getClassName(231)

t = 300
hash = {}

while 1:
    t += 1
    classID = getClassName(t**3)
    
    if classID not in hash:
        hash[classID] = [t,]
        #print t
        continue
    #print t    
    hash[classID].append(t)
    
    if len(hash[classID]) == 5:
        print hash[classID]
        print map(lambda x: x*x*x, sorted(hash[classID]))
        print map(lambda x: getClassName(x*x*x), hash[classID])
        break
        
    
    
    