import numpy, psyco
psyco.full()

F_N, F_N_1 = 1,1
k = 2
T = 10**10

def digit_iter(n):
    while n > 0:
        yield n % 10
        n = n / 10
        
def check(number, ar = numpy.zeros(10)):
    ar -= ar
    
    last_9_digit_number = number % T
    
    for k in digit_iter(last_9_digit_number):
        ar[k] = 1
    if len(str(last_9_digit_number)) < 10:
        ar[0] = 1
    #print ar
    if (not (ar == 1).all()):
        return False
        
    ar -= ar
    #try:
    #    a = float(number)
    #except:
    #    print number
    #    exit()
    #t = numpy.log(a)
    #t /= numpy.log(10)
    power = len(str(number))# + 1# long(numpy.ceil(t))
    
    first_9_digit_number = number / (10**(power - 10))
    first_9_digit_number = long(first_9_digit_number)
        

    for k in digit_iter(first_9_digit_number):
        #if ar[k] == 1:
        #    return False
        ar[k] = 1
    #print ar    
    return (ar == 1).all()
    
assert check(123456789000000987654321)
assert check(1234567809)

while 1:
    F_N, F_N_1 = F_N + F_N_1, F_N
    if F_N < 10**8:
        continue
    if check(F_N):
        print F_N
        break
