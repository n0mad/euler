table = [200, 100, 50, 20, 10, 5, 2,1]
hash = {}
def P(money, index=0):
    #how many combinations using coins less or equal than table[index]
    if money == 0:
        return 1
    
    if index == len(table) - 1:
        return 1
        
    if (money, index) in hash:
        return hash[(money,index)]
    sum = P(money, index + 1)
    #sum = 0
    rem = money - table[index]
    while rem >= 0:
        sum += P(rem, index + 1)
        rem = rem - table[index]
    hash[(money, index)] = sum
    return sum
    
#print P(1)
assert P(1) == 1
#print P(3)
assert P(2) == 2
assert P(5) == 4


print P(200)