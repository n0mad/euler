import psyco
psyco.full()

#digits = [0,0]
digits =  [0 for i in xrange(10)]

#target = [5,2,9]
target = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9]
target.reverse()

result = [0 for i in xrange(len(target))]

def multiply(position, digits):
    sum = 0
    for i in xrange(0,position+1):
#        if i < len(digits) and (position - i) < len(digits):
        sum += digits[i] * digits[position - i]
    #if 0 == position % 2:
    #    sum += digits[position/2] * digits[position/2]
    return sum

def checkDigit(position, target, result):
    if target[position] == 0:
        return True
    if target[position] == result[position]:
        return True
    return False
    
def isReallyGood(digits):
    t = list(digits) #.copy()
    t.reverse()
    
    i = int(''.join(map(str, t)))
    k = i * i
    #print k, i
    #for t in xrange(len(k)):
    k = str(k)
    if k[0] == '1' and k[2] == '2' and k[4] == '3' and k[6] == '4' and k[8] == '5':
        print k+"00", i*10
def backtrackFirst(position, target, result, digits, toadd):
    if position >= len(digits):
        isReallyGood(digits)
        return
        
    #print "starting backtrack with toadd = %s"%(toadd), "digits = ", digits, "results= ", result
    for d in xrange(0,10):
        digits[position] = d
        curr = toadd + multiply(position, digits)
        result[position] = curr % 10
        toaddnew = curr / 10
        
        if checkDigit(position, target, result):
            #print "going deeper, ", curr#, #digits, toadd, result[:position+1]
            backtrackFirst(position + 1, target, result, digits, toaddnew)

#print checkDigit(0, [9,0,8], [8,0,0])
            
backtrackFirst(0,target, result, digits, 0)