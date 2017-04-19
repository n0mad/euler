import sys, string

file = open(sys.argv[1], 'rb')

list = map(string.strip, file.readlines())
list.sort()
print list[937]
print map(lambda x: ord(x) - ord('A') + 1, "COLIN")
res = []
for t in list:
    tmp = map(lambda x: ord(x) - ord('A') + 1, t)
    if t == 'COLIN':
        print '!', tmp, sum(tmp)
    #sum = #reduce(lambda x, y: x + y, tmp)
    res.append(sum(tmp))
sum = 0
print res[937]
for p in xrange(1, len(res) + 1):
    sum += p * res[p-1]
    
#l = [map(lambda x: ord(x) - ord('A') + 1, t)]
file.close()
print sum