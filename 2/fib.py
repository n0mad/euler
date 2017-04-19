f0 = 1
f1 = 1
sum = 0


while f1 < 4000000:
    f0,f1 = f1, f0 + f1
    if f1 % 2 == 0:
        sum += f1
print sum