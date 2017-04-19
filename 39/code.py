import numpy

per = numpy.zeros(1000)

for c in xrange(500):
    for a in xrange(c):
        for b in xrange(a):
            if c*c == a*a + b*b:
                if a+b+c < 1000:
                    per[a+b+c] += 1
assert per[120] == 3

print per.argmax()