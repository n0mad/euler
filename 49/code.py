def isSeq(lst):
    len_lst = len(lst)
    assert len_lst > 2
    
    lst.sort()
    
    for first_index in xrange(0, len_lst - 1):#0,1
        for second_index in xrange(first_index + 1, len_lst): #1,2
            for third_index in xrange(first_index + 1, second_index): #
                
                if lst[first_index] + lst[second_index] == 2 * lst[third_index]:
                    print '!!!!', first_index, second_index, third_index
                    return True
    return False
    
assert isSeq([1,3,5])

assert isSeq([1,10,19])
assert isSeq([1,1, 3,1,5])
assert not isSeq([100,150,149])
file = '4_digit_primes'
primes = []
file = open(file, 'rb')
for line in file:
    primes += line.split()
file.close()

hash = {}

for prime in primes:
    list = map(int, prime)
    assert 4 == len(list)
    list.sort()
    list = ().__class__(list)
    if list in hash:
        hash[list].append(prime)
    else:
        hash[list] = [prime]
        
for key in hash:
    if (len(hash[key]) > 2):# and ('1487' in hash[key]):
        print hash[key]
        if isSeq(map(int, hash[key])):
            print '!', hash[key]