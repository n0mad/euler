import sys, math
def isTriangle(x):
    sum = 0
    for letter in x:
        #print ord(letter) - ord('A') + 1
        sum += (ord(letter) - ord('A') + 1)
    #print sum    
    D = (1 + 8*sum)
    if int(D**0.5) == D**0.5:
        return True
    return False
assert isTriangle('SKY')

infile = open(sys.argv[1], 'rb')
triangles = 0

for x in infile:
    x = x.strip()

    if isTriangle(x):
        triangles += 1
infile.close()


print triangles