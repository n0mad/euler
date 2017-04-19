
power = 7830457
modulo = 10 ** 10

x = 2
t = 1
while power > 1:
    if power % 2 == 0:
        x = (x*x) % modulo
        power = power / 2
    else:
        t = (t * x) % modulo
        power = power - 1
        
print (28433*x*t+1) % modulo