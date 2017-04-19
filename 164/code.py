import itertools

def getGoodTriplets():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    alltriplets = itertools.combinations_with_replacement(digits, 3)
    sumless9    = itertools.ifilter(lambda x: x[0] + x[1] + x[2] < 9, alltriplets)

    for tri in sumless9:
        for tri2 in set(itertools.permutations(tri)):
            yield tri2


def isGood18(t):
    for k in xrange(0, 5):
        if t[k][1] + t[k][2] + t[k+1][0] > 9:
            return False
        if t[k][2] + t[k+1][0] + t[k+1][1] > 9:
            return False
    return True
    #not all!

def getGood18(triplets):
    all18   = itertools.combinations_with_replacement(triplets, 6)
    filter = itertools.ifilter(isGood18, all18)
    return filter

def getPairs(n):
    #tooo lazy to think
    count = 0
    for a in xrange(1, 9 - n):
        for b in xrange(0, 9 - n - a):
            count += 1

    return count

triplets = getGoodTriplets()

c18 = getGood18(triplets)

a = [0 for t in xrange(10)]

for k in c18:
    a[ k[0][0] ] += 1

print a

exit(0)

for i in xrange(len(a)):
    sum += getPairs[i] * a[i]

print sum

