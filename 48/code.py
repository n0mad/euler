mod = 10**10

def toPower(base, power, modulo):
    x = base
    t = 1
    while power > 1:
        if power % 2 == 0:
            x = (x*x) % modulo
            power = power / 2
        else:
            t = (t * x) % modulo
            power = power - 1
    return t * x % modulo
    
    
assert toPower(2,5, 100) == 32
assert toPower(2,5, 2) == 0
assert toPower(2,5, 20) == 12
#print toPower(2,5, 20)
assert toPower(3,2, 100) == 9

sum = 0
for x in xrange(1, 1000001):
    sum = (sum + toPower(x,x, mod)) % mod
print sum