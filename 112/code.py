def isBouncy(n):
    wasInc = False
    wasDec = False
    prev = str(n)[0]
    for digit in str(n)[1:]:
        
        if digit > prev:
            wasInc = True
            prev = digit
        elif digit < prev:
            wasDec = True
            prev = digit
        elif digit == prev:
            prev = digit
            continue
        if wasDec and wasInc:
            return True
    if wasDec and wasInc:
        return True            
    return False
assert isBouncy(1230)
assert not isBouncy(123)
assert not isBouncy(321)
assert  isBouncy(155349)
bouncy = 0
number = 1


while 1:
    number += 1
    if 0 == number % 1000:
        print number
    if isBouncy(number):
        bouncy += 1
    
    
    if bouncy*1.0/number >= 0.99:
        print number
        break
        