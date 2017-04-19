def isOriginIn(x1,y1,x2,y2,x3,y3):
    if rawn(x1,y1,x2,y2, x3,y3) == rawn(x2,y2,x3,y3,x1,y1) == rawn(x3,y3,x1,y1,x2,y2):
        return True
    return False
    

def rawn(x1,y1,x2,y2,x3,y3):
    pr1=(x2-x1)*(-y1)-(y2-y1)*(-x1)
    pr2=(-x1)*(y3-y1)-(-y1)*(x3-x1)
    if pr1*pr2>=0 :
        return True
    return False
    
    
assert isOriginIn( -340,495,-153,-910,835,-947)
assert not isOriginIn(-175,41,-421,-714,574,-645)

total = 0
withOrigin = 0

file = open('triangles.txt', 'rb')
for line in file:
        x1,y1,x2,y2,x3,y3 = map(int, line.split(','))
        total += 1
        if isOriginIn(x1,y1,x2,y2,x3,y3):
            withOrigin+= 1
            
            
            
print total, withOrigin
file.close()
