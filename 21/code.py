
def getDivizorsSum(n):
    k = 1
    sum = 1
    for k in xrange(2, int(n ** 0.5)+1):
        if n % k == 0:
            sum += k
            if not k == n / k:
                
                sum += n / k
    return sum
    
assert getDivizorsSum(220) == 284
assert getDivizorsSum(2) == 1
#print getDivizorsSum(4)
assert getDivizorsSum(4) == 3

hash = {}
pairs = []

for x in xrange(2, 10000 + 1):
    div_sum = getDivizorsSum(x)
    if (div_sum in hash) and (x == hash[div_sum]):
        pairs.append((div_sum, x))
    else:
        hash[x] = div_sum
sum = 0
for pair in pairs:
    sum += pair[0] + pair[1]
print sum