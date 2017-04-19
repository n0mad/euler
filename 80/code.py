from decimal import *

def get_sum(decimal):
    s = filter(lambda i: i != '.', str(decimal))[:100]
    s = map(lambda x: int(x), s)
    return sum(s)


getcontext().prec = 102

perfect_squares = [x*x for x in xrange(1, 10)]

result = 0
for i in xrange(2, 100):
    if i in perfect_squares:
        continue
    result += get_sum(Decimal(i).sqrt())
print result 
