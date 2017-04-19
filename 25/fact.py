import math
f1 = 1L
f2 = 1L
k = 2
while 1:
    k += 1
    f1, f2 = f2, f1 + f2
    
    if math.log10(f2) >= (1000 - 1):
        print k
        break