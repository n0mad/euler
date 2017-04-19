import sys
bound = 1000000


primes = []
file = open(sys.argv[1], 'rb')

for line in file:
    primes += map(int, line.split())

file.close()
hashtable = set(primes)

largest_start = 0
largest_offset = 0
largest_sum = -1

for start in xrange(len(primes)):
    curr_sum = 0
    for offset in xrange(len(primes) - start):
        curr_sum += primes[start + offset]
        
        if curr_sum > bound:
            break
            
        if (curr_sum in hashtable) and (offset > largest_offset):
            largest_start = start
            largest_offset = offset
            largest_sum = curr_sum
            
assert largest_sum == sum(primes[largest_start:largest_start+largest_offset + 1])
assert largest_sum in hashtable
print primes[largest_start:largest_offset+1]
print largest_start, largest_offset, largest_sum