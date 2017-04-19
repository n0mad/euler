import sys
file = open(sys.argv[1], 'rb')
triangle = []
distances = []
for line in file:
    triangle.append(map(int, line.split()))
    distances.append([-1]*len(line.split()))
file.close()


for x in xrange(len(triangle[-1])):
    distances[-1][x] = triangle[-1][x]
    
#print triangle
#print distances

for index_y in xrange(len(distances)-2, -1, -1):
    #index_y = len(distances) - index_y - 2
    #print '!', index_y
    for index_x in xrange(len(distances[index_y])):
        #print index_y, index_x
        
        a = distances[index_y+1][index_x]
        b = distances[index_y+1][index_x+1]
        distances[index_y][index_x] = max(a,b) + triangle[index_y][index_x]
        
print distances[0][0]
