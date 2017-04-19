import sys

file = open(sys.argv[1], 'rb')
sum = 0
for line in file:
    sum += int(line[:11])
file.close()

print str(sum)[:10]