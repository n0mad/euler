import math
def isEq(N):
    t = N
    sum = 0
    while t > 0:
        sum += t % 10
        t = t / 10
    #sum = reduce(lambda x,y: x + y, map(int, str(N)))
    #k = 1
    if (sum == 1) and (not N == 1):
        return False
    if (not N % 2 == sum % 2) or (not 0 == N % sum):
        return False
    
    candidate = sum**(int(math.log(N)/math.log(sum)) - 1)
    
    
    t = candidate
    while 1:
        if N < t:
            return False
        if N == t:
            return True
        t = t * sum
assert isEq(512)
assert isEq(614656)
assert not isEq(100)

count  = 0
t = 10
while count < 31:
    
    if isEq(t):
        count += 1
        print t
    t += 1