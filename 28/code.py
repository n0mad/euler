dim = 1001

sum_ = 1
for n in xrange(3,dim+1, 2):
    sum_ += 4*n*n - 6*n + 6
print sum_

#669171001

print sum(4*n**2-6*n+6 for n in range(3, dim+1, 2))+1