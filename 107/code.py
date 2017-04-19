import sys

def loadNet(file):
    def translate (x):
        if not x == '-':
            return int(x)
        else:
            return x
            
    net =[]
    file = open(file, 'rb')
    #t = 0
    for line in file:
        #if t > 0:
        net.append(map(translate, line.rstrip().split(',')) )
        #else:
        #    net.append(map(translate, line.rstrip().split(',') ) )
        #t += 1
    file.close()
    
    return net
def getSum(net):
    sum = 0
    for v in net:
        for co_v in v:
            if not '-' == co_v:
                sum += co_v
    return sum / 2
def getArcsAscending(net):
    list = []
    for i in xrange(len(net)):
        for j in xrange(len(net[i])):
            if not net[i][j] == '-':
                list.append((i,j))
    def my_cmp(x,y):
        return cmp(net[x[0]][x[1]], net[y[0]][y[1]])
    #print list
    #print my_cmp(list[0], list[1])
    list.sort(cmp = my_cmp, reverse = True)
    return list
    
def kruskal(net, arcsAsc):
    trees = []
    arcsUsed = []
    sum = 0
    for v in xrange(len(net)):
        t = set()
        t.add(v)
        trees.append(t)
    while (len(trees) > 1) and (len(arcsAsc) > 0):
        edge = arcsAsc.pop()
        first, second = None, None
        for tree in trees:
            if edge[0] in tree:
                first = tree
                break
        if edge[1] in tree:
            continue
        for tree in xrange(len(trees)):
            if edge[1] in trees[tree]:
                second = trees[tree]
                break
        del trees[tree]
        first.update(second)
        sum += net[edge[0]][edge[1]]
        
        #arcsUsed.append(edge)
        print edge, net[edge[0]][edge[1]]
    return sum, arcsUsed
        
        
    
net = loadNet(sys.argv[1])
print net
#print getSum(net)
arcsAsc =  getArcsAscending(net)#[:10], map(lambda x: net[x[0]][x[1]], getArcsAscending(net)[:10])
w = getSum(net)
min_w, arcs_used = kruskal(net, arcsAsc)
print w - min_w
print arcs_used, min_w