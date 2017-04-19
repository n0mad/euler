# 3, 8,9 pandigits are divizible by 3
#1,2 are not prime
#so we are to test only 4,5,6,7 pandigits, less than 7! 
def getNextTransform(n):
    list_str = [].__class__(str(n))
    list = map(int, list_str)
    last = len(list) - 1
    
    while (last > 0) and (list[last - 1] > list[last]):
        last -= 1
    #print 'last', last
    if 0 == last:
        return n
    else:
        #part1 = list[:last-1]
        #part2 = list[last-1:]
        min_pos = None
        for t in xrange(last, len(list)):
            if (None == min_pos) or ((list[t] < list[min_pos]) and (list[t] > list[last-1])):
                min_pos = t
        #print 'min_pos', min_pos        
        result = list_str[:last-1]
        result.append(list_str[min_pos])
        del list_str[min_pos]
        part2 = list_str[last-1:]
        part2.sort()
        result += part2
        
        return int(''.join(result))

def isPrime(k):
    for t in xrange(2, int(k**0.5) + 1):
        if 0 == k % t:
            return False
    return True
        
#assert getNextTransform(1) == 1
#assert getNextTransform(21) == 21
#assert getNextTransform(12) == 21
#assert getNextTransform(123) == 132
#assert getNextTransform(132) == 213
#assert getNextTransform(213) == 231
#assert getNextTransform(231) == 312
#assert getNextTransform(312) == 321
#assert getNextTransform(321) == 321
import time
start = time.time()
test_list = [1234567]
max = 0
for number in test_list:
    prev = number
    next = getNextTransform(number)
    
    while not next == prev:
        if isPrime(next) and (next > max):
            max = next#pass#print next
        prev, next = next, getNextTransform(next)
print time.time() - start
print max