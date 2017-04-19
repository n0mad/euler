def f(k):
    #print k, k*(3*k - 1)/2
    return k*(3*k - 1)/2
    
def generate():
    Pn = [1]
    #
    n = 1
    while 1:
    #for n in xrange(1, N + 1):
        sum = 0
        k = 1
        while 1:
            if n-f(k) >= 0:
                first = Pn[n-f(k)]
            else:
                first = 0
            
            if n-f(-k) >= 0:
                second = Pn[n-f(-k)]
            else:
                second = 0
            if first == second == 0:
                break
            sum += (-1)**(k+1) * (first + second)
            k += 1
        Pn.append(sum)
        yield Pn[-1]    #n += 1
        n += 1
    #return Pn
Pn = generate()
#[6]
count = 0
for x in Pn:
    #print x
    count += 1
    if 0 == x % 10**6:
        print x, count
        break
#assert Pn[1] == 1
#assert Pn[2] == 2