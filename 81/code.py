import sys, string, numpy
inF = open(sys.argv[1], 'rb')
matrix = []
for line in inF:
    matrix.append(map(int, line.split(',')))
matrix = numpy.array(matrix)

x_len, y_len = len(matrix), len(matrix[0])
matrix_dist = numpy.zeros((x_len, y_len))

matrix_dist[0][0] = matrix[0][0]

for y in xrange(1, y_len):
    matrix_dist[0][y] = matrix[0][y] + matrix_dist[0][y-1]

for x in xrange(x_len):
    matrix_dist[x][0] = matrix[x][0] + matrix_dist[x-1][0]
    
for x in xrange(1, x_len):
    for y in xrange(1, y_len):
        matrix_dist[x][y] = matrix[x][y] + min(matrix_dist[x-1][y], matrix_dist[x][y-1])
inF.close()
print matrix
print matrix_dist#[x_len-1][y_len-1]