max = 10**8

file = open('primes_up_to_50M')

primes = []
for line in file:
    primes.append(int(line))# += map(int, line.split())
print len(primes)
final_list = filter(lambda x: x < max/2 + 1, primes)
#print final_list[0]
size = len(final_list)
print size
count = 0

for x in xrange(size):
    for y in xrange(x, size):
        if final_list[x]*final_list[y] < max:
            count += 1
        else:
            break
print count