import sys, numpy

def readWeights(file):
    res = []
    file = open(file, 'rb')
    for line in file:
        res.append(map(int, line.split(',')))
        
    return numpy.array(res)
def buildGraph(weights):
    # link lists
    size = len(weights)
    A = numpy.ones(size**2, size**2) * 100000
    for i in xrange(size):
        for j in xrange(size):
            if 0 < i < size - 1:
                A[i]
                
def shortestPath(weights):
    pass
    