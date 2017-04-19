def argmax(lst):
    max,arg = lst[0], 0
    for k in xrange(1, len(lst)):
        if lst[k] > max:
            max, arg = lst[k], k
    return arg
    
def nextLexPermutation(list):
    flag = 0
    min_max = argmax(list)
    
    i = len(list) - 2
    while list[i] > list[i + 1]:
        i = i - 1
    #print "i", i
    
    j = len(list) - 1
    while list[i] > list[j]:
        j = j - 1
        
    #print "j", j        
    list[i], list[j] = list[j], list[i]
        
    r = len(list) - 1
    s = i + 1
            
    while (r > s):
        list[r],list[s] = list[s], list[r]
        r -= 1
        s += 1
        

def makeInt(lst):
    i = 0
    k = 1
    
    for t in xrange(len(lst) - 1, -1, -1):
        i += lst[t]*k
        k = k * 10
    return i
    
def check(d):
    #d_(2)d_(3)d_(4)=406 is divisible by 2
    if makeInt(d[1:4]) % 2 > 0:
        return 0
    #d_(3)d_(4)d_(5)=063 is divisible by 3
    if makeInt(d[2:5]) % 3 > 0:
        return 0
    #d_(4)d_(5)d_(6)=635 is divisible by 5
    if (10* d[4] + d[5]) % 5 > 0:
        return 0
    #d_(5)d_(6)d_(7)=357 is divisible by 7
    if makeInt(d[4:7]) % 7 > 0:
        return 0
    #d_(6)d_(7)d_(8)=572 is divisible by 11
    if makeInt(d[5:8]) % 11 > 0:
        return 0
    #d_(7)d_(8)d_(9)=728 is divisible by 13
    if makeInt(d[6:9]) % 13 > 0:
        return 0
    #d_(8)d_(9)d_(10)=289 is divisible by 17
    if makeInt(d[7:10]) % 17 > 0:
        return 0

    return 1
assert check(map(int , [].__class__("1406357289"))) == 1
sum = 0
prev = [0,1,2,3,4,5,6,7,8,9]
for k in xrange(0, 10*9*8*7*6*5*4*3*2*1):
    nextLexPermutation(prev)
    #print prev
    t= check(prev)
    if t == 1:
        print prev
        sum += makeInt(prev)#t
print sum

#prev = [0,1,2]#,3,4,5,6,7,8,9]
#count = 0
#while 1:
#    print prev
#    
#    flag = nextLexPermutation(prev)
#    if (count > 6):
#        break
#    print flag, prev