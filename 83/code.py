import numpy as np

size = 80
def AllocateDist(data):
    dist = np.zeros((size,size,size,size), dtype = float)
    for f_i in xrange(size):
        for f_j in xrange(size):
            for s_i in xrange(size):
                for s_j in xrange(size):

                    if f_i == s_i and f_j == s_j:
                        dist[f_i, f_j, s_i, s_j] = 0
                    else:

                        neighbours = False

                        if ( np.abs(s_i - f_i) == 1 and f_j == s_j ):
                            neighbours = True

                        if ( np.abs(s_j - f_j) == 1 and f_i == s_i ):
                            neighbours = True

                        if neighbours:
                            dist[f_i][f_j][s_i][s_j] = 0.5 * (data[f_i][f_j] + data[s_i][s_j])
                        else:
                            dist[f_i][f_j][s_i][s_j] = 10e10
    return dist

matrix = map(lambda x: map(int, x.split(',')), open('matrix.txt').readlines())
#matrix = map(lambda x: map(int, x.split(',')), open('tmp').readlines())

dist = AllocateDist(matrix)

for t_i in xrange(size):
    for t_j in xrange(size):

        for f_i in xrange(size):
            for f_j in xrange(size):

                for s_i in xrange(size):
                    for s_j in xrange(size):


                        if dist[f_i, f_j, s_i, s_j] > dist[f_i, f_j, t_i, t_j] + dist[t_i, t_j, s_i, s_j]:
                            dist[f_i, f_j, s_i, s_j] = dist[f_i, f_j, t_i, t_j] + dist[t_i, t_j, s_i, s_j]

print(dist[0][0][size-1][size-1] + 0.5 * (matrix[0][0]  + matrix[size-1][size-1]))
