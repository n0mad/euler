def test(a,b):
    f = 1.0*a/b
    
    if (f == (a/10)*1.0/(b/10)) and ((a % 10) == (b % 10)):
        return True
    if (f == (a/10)*1.0/(b % 10)) and ((a % 10) == (b / 10)):
        return True
    if (f == (a % 10)*1.0/(b/10)) and ((a / 10) == (b % 10)):
        return True
    if (f == (a% 10) * 1.0 / (b%10)) and ((a / 10) == (b / 10)):
        return True
    return False
    
mul_enum, mul_denom = 1,1
for denominator  in xrange (10, 100):
    if denominator % 10 == 0:
        continue
        
    for enumerator in xrange(1, denominator):
        if enumerator % 10 == 0:
            continue
    
        
        #fraction = 1.0*enumerator/denominator
        if test(enumerator, denominator):
            print enumerator, denominator
            mul_enum *= enumerator
            mul_denom *= denominator
            
            




for t in xrange(2,mul_enum):
    while (mul_enum % t == 0) and (mul_denom % t == 0):
        mul_enum = mul_enum / t
        mul_denom = mul_denom / t
        
        
print '%s/%s'%(mul_enum, mul_denom)