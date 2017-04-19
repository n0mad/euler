
def doTransform(N):
    return int(N) , N - int(N)
    
def getPeriod(N):
    lst = []
    current = N
    while True:
        res = doTransform(current)
        lst.append(res[0])
        current = 1.0/res[1]
        if (len(lst) > 1) and ((current - N - lst[0])*1.0/current < 0.0001):# and (lst[0] == res[0]):
            print current, current - N - lst[0]
            break
        
        
    return     lst
        
def test():
    firstStep = doTransform(14**0.5)
    assert 3 == firstStep[0]
    
    secondStep = doTransform(1.0/firstStep[1])
    
    assert 1 == secondStep[0]
    print getPeriod(14**0.5)
    assert [3,1,2] == getPeriod(14**0.5)
test()