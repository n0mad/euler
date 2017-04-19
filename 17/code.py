hash = {1: "one",  	11: "eleven" , 10:"ten", 2 : "two", 12: "twelve", 20:"twenty", 3: "three", 13:"thirteen", 30:"thirty",
 4:"four", 14:"fourteen", 40:"forty", 5: "five", 15:"fifteen", 50:"fifty",
6:"six", 16:"sixteen", 60:"sixty" , 7:"seven", 17:"seventeen", 70:"seventy",
8: "eight", 18: "eighteen", 80:"eighty", 9:"nine", 19:"nineteen", 90:"ninety" }

def my_len(str):
    l = 0
    for k in xrange(0, len(str)):
        if 'a' <= str[k] <= 'z':
            l+= 1
    return l
    
def processTens(i):
    t = hash[i - i % 10]
    if i % 10 > 0:
        t += '-' + hash[i % 10]
    return t
    
def processHundreds(i):
    t = hash[i / 100] + " hundred"
    if i % 100 > 0:
        t += ' and ' + NumToWord(i % 100)
    return t
    
def NumToWord(i):
    print i
    
    if i == 0:
        return ''
        
    if 0 < i < 20:
        return hash[i]
    
    if 20 <= i < 100:
        return processTens(i)
    if 100 <= i < 1000:
        return processHundreds(i)
        
#print NumToWord(342 )
assert "three hundred and forty-two" == NumToWord(342)
assert my_len(NumToWord(342)) == 23 
assert my_len(NumToWord(115))  == 20
s = 0
for k in xrange(1, 1000):
    print NumToWord(k)
    s += my_len(NumToWord(k))
    
print s + my_len('one thousand')