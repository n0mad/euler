powers = [0, 1, 2**5, 3**5, 4**5, 5**5, 6**5, 7**5, 8**5, 9**5]

#print powers[-1]
def sumDigits(n):
    sum = 0
    
    while n > 0:
        sum += powers[n % 10]
        n = n / 10
    return sum
assert sumDigits(10) == 1
assert sumDigits(1023456789) == sum(powers)
#60 000 * n < 10^(n)
#n = 7
#420 000 < 10 000 000
list = []
for i in xrange(2, 10**7):
    if i == sumDigits(i):
        list.append(i)
print list
print sum(list)