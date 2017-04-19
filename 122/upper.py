import math

def nu(x):
    t = 0
    while x > 0:
        if (x % 2 == 1):
            t += 1
        x = x / 2
    return t
def upperBound(x):
    return math.ceil( math.log(x)/math.log(2) + nu(x) ) - 1
    
assert upperBound(2) == 1
assert upperBound(8) == 3

if __name__ == '__main__':
    pair = [0,-100]
    for x in xrange(2,201):
        if upperBound(x) > pair[1]:
            pair = x, upperBound(x)
            
    print pair