import sys

matrix = []
file = open(sys.argv[1], 'rb')
for line in file:
    matrix.append(map(int, line.split()))
file.close()
import numpy

matrix = numpy.array(matrix)
#matrix = matrix.T

max_horizontal = 0
max_line, max_t = None, None
for line in xrange(len(matrix)):
    for t in xrange(0, len(matrix[line]) - 3):
        mul = reduce(lambda x, y: x * y, matrix[line][t:t+4])
        if  mul > max_horizontal:
            
            max_horizontal = mul
            max_line, max_t = line, t
            
            #print matrix[max_line][t:t+4]
            #print 
            
print 'horizontal' , max_horizontal
#print max_line, max_t
#print reduce(lambda x, y: x * y, matrix[max_line][max_t:max_t+4])
#print matrix[max_line][max_t:max_t+4]
max_diag = 0
x0, y0, v = 0,0 ,0
for x in xrange(len(matrix)-3):
    for y in xrange(0, len(matrix[0]) - 3):
        mul = matrix[x][y]*matrix[x+1][y+1]*matrix[x+2][y+2]*matrix[x+3][y+3]
        
        if mul > max_diag:
            max_diag = mul
            x0, y0,v  = x,y, matrix[x][y]
print max_diag, x0, y0, v


max_diag = 0
x0, y0, v = 0,0 ,0
for x in xrange(0, len(matrix)-3):
    for y in xrange(3, len(matrix[0])):
        mul = matrix[x][y]*matrix[x+1][y-1]*matrix[x+2][y-2]*matrix[x+3][y-3]
        
        if mul > max_diag:
            max_diag = mul
            x0, y0,v  = x,y, matrix[x][y]
print max_diag, x0, y0, v
