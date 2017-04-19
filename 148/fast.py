import numpy, math
SIZE = 55

count_table = numpy.zeros(SIZE)
result_table = numpy.zeros(SIZE)

def counter(a):
    k = 7
    count = 0
    while (a >= k):
        count += a / k
        k = k * 7
    return count
    
def fillCountTable(table):
    for i in xrange(len(table)):
        table[i] = counter(i)
    return table


total = 0    
count_table = fillCountTable(count_table)
#fill in first 7 arguments of result table
for i in xrange(0, 7):
    result_table[i] = 1 + i
    total += 1 + i;

prev_power = 0
#all berfore 7 is filled in
i = 7
while 1:
    #out of table
    if i >= SIZE:
        break
    total += i + 1
    #point of growth
    if int( math.log(i, 7) ) > prev_power:
        print 'To4ka rosta: ', i
        for k in xrange(7):
            if i + k > SIZE - 1:
                break
            result_table[i] = (k+1) * 2
            i += 1
            #if k =< 6:
            total += i + 1
        prev_power = int( math.log(i, 7) )
        continue
            
    result_table[i] = result_table[i - 7]
    
    for k in xrange(i - 6, i + 1):
            if count_table[i] - count_table[i - k] == count_table[k]:
                result_table[i] += 1

    i += 1

print total , sum(result_table)