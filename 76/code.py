def p(a,b, h = {}):
    if a == 2:
        return (b-1)/2
    elif (a,b) in h:
        return h[(a,b)]
    else:
        sum = 0
        for t in xrange(a-1, b+1):
            sum += p(a-1,t)
        h[(a,b)] = sum
        return sum
print p(100,100)