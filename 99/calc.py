import sys, math
max = 0
max_line = 0
current_line = 0
file = open(sys.argv[1], 'rb')

for x in file:
    current_line += 1
    base, power = map(int, x.split(','))
    if power*math.log(base) > max:
        max = power*math.log(base)
        max_line = current_line
print max_line