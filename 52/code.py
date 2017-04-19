#1(1\2\3\4\5\6)
def test(x):
    x_ = [].__class__(str(x))
    x_.sort()
    
    x_6 = [].__class__(str(x*6))
    x_6.sort()
    
    if not x_6 == x_:
        return False
        
    x_2 = [].__class__(str(x*2))
    x_2.sort()
    
    if not x_2 == x_:
        return False
        
    x_3 = [].__class__(str(x*3))
    x_3.sort()
    
    if not x_3 == x_:
        return False
    
    x_4 = [].__class__(str(x*4))
    x_4.sort()
    
    if not x_4 == x_:
        return False
    
    x_5 = [].__class__(str(x*5))
    x_5.sort()
    
    if not x_5 == x_:
        return False
    return True
    
for t in xrange(2, 100):
    for x in xrange(10**t, 10**t+7*10**(t-1)):
        if test(x):
            print x
            