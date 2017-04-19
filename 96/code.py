import psyco
from constraint import * 
psyco.full()

def UnEqual(*params):
    all = [0,0,0,0,0,0,0,0,0,0]
    #print params
    #params = list(params)
    #params = sorted(params)
    #print params
    for i in (params):
        if all[i] == 1:
            return False
        else:
            all[i] = 1
    return True

    
def loadSudoku(filename):
    matrixes = []
    file = open(filename, 'r')
    
    while True:
        t = file.readline() #gridN
        if (None == t) or ('' == t):
            break
        matrix = []
        for i in xrange(9):
            line = file.readline()
            row = map(int, line.strip())
            matrix.append(row)
        matrixes.append(matrix)
    file.close()
    return matrixes
def makeProblem(matrix):
    problem = Problem() 
    dom = [1,2,3,4,5,6,7,8,9]
    
    names = []
    #adding variables
    for row in xrange(len(matrix)):
        names.append([])
        for column in xrange(len(matrix[row])):
            name = "[%s,%s]"%(row, column)
            names[-1].append(name)
            if matrix[row][column] != 0:
                problem.addVariable(name, [matrix[row][column], ])
            else:
                problem.addVariable( name, dom)
    
    #row constraint
    for row in xrange(len(matrix)):
        problem.addConstraint(UnEqual, names[row])
    #column constrain
    onecolumn = []
    for column in xrange(len(matrix[0])):
        for row in xrange(len(matrix)):
            onecolumn.append(names[row][column])
        problem.addConstraint(UnEqual, onecolumn)
        onecolumn = []
            
    return problem
    
a = loadSudoku("testsudoku.txt")
print makeProblem(a[0]).getSolution()