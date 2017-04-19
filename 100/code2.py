import math
import psyco
psyco.full()

Lower = 10**11
Upper = 10**14

sqrtL = int(Lower**0.5) + 1
n = sqrtL
m = n
mode = 0

while n < Upper:
    m = int(2.4142*n)
    while m < int(n*2.4143):
        a = m**2 - n**2
        b = 2*m*n

        if abs(a-b) == 1:
            print (1 + m**2 + n**2)/2, m, n, 1.0*m/n
        m += 1
    n += 1