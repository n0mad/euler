import itertools


def isPrime(k):
    if k == 1:
        return False

    top = min(k - 1, int(k**0.5) + 2)
    for t in xrange(2, top):
        if 0 == k % t:
            return False
    return True

def composeSet(lst, ends):
    current_num = 0
    i = 0
    set = []
    for k in lst:
        if not k == 0:
            current_num = current_num * 10 + k
        else:
            current_num = current_num * 10 + ends[i]
            set.append(current_num)
            current_num = 0
            i += 1

    current_num = current_num * 10 + ends[i]
    set.append(current_num)

    return ().__class__(set)

def getSets(ends, others):
    for perm in set(itertools.permutations(others)):
        numberset = composeSet(perm, ends)
        isGood = True
        for k in numberset:
            if not isPrime(k):
                isGood = False
                break
        if isGood:
            yield numberset    

def getAllSets(ends, others):
    allsets = set()

    for toremove in xrange(0, len(ends) ):
        for removed in itertools.combinations(ends, toremove):
            othersnew = others[toremove:] + list(removed)
            endsnew   = list( set(ends).difference( set(removed) ) )
            allsets  = allsets.union(getSets(endsnew, othersnew))
    return allsets

others = [0, 0, 0, 2, 5, 4, 6, 8]
ends   = [1, 3, 7, 9]

allsets = set()
allsets =  getAllSets(ends, others)

allsets = allsets.union(getAllSets(ends, [0, 0, 0,    4, 5, 6, 8])) #2 as an independent number
allsets = allsets.union(getAllSets(ends, [0, 0, 0,    4,    6, 8])) #2 and 5 as independent numbers
allsets = allsets.union(getAllSets(ends, [0, 0, 0, 2, 4,    6, 8])) #5 as ..

print len(allsets)

isin = False
for k in itertools.permutations( (47,89,631) ):
    if k in allsets:
        isin = True
assert isin
