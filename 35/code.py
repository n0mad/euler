file = open('./../100000_primes.txt', 'rb')
primes = []
def shift(n):
    return '%s%s'%(n[1:],n[0])
    
for line in file:
    #strings!
    primes += line.split()
    if len(primes[-1]) > 6:
        break
    
file.close()

circular = 0
assert shift('197') == '971'
goodNums=set(['1','3','7','9'])
good_filter=lambda x: not set(str(x)).difference(goodNums)
primes=filter(good_filter,primes)


for prime in primes:
    if int(prime) > 10**6:
        break
    if ('2' in prime) or ('5' in prime) or ('0' in prime) or ('4' in prime) or ('6' in prime):
        continue
    is_circular = True
    length = len(prime)
    prime_test = prime
    #print 
    #print prime_test, ':',
    for t in xrange(0, length-1):
        prime_test = shift(prime_test)
        #print prime_test,
        if prime_test not in primes:
            is_circular = False
            break
    if is_circular:
        print 'Circular:',prime
        circular += 1
        
        
print circular+2