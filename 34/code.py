fact = {0:1, 1:1, 2:2, 3:6, 4:24, 5: 120, 6:720, 7:7*720, 8:8*7*720, 9:9*8*7*720}
def getDigitsFactSum(n):
    sum = 0
    
    while n > 0:
        sum += fact[n % 10]
        n = n / 10
    return sum
assert getDigitsFactSum(145) == 145
assert getDigitsFactSum(5) == 120
assert getDigitsFactSum(1234567890) == sum(fact.values())

#10**k > 400 000 * k

#k = 6
#10 000 000  2 400 000
list = []
for  i in xrange(3, 10**7):
    if i == getDigitsFactSum(i):
        list.append(i)
        
print list