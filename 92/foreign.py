import array
t=array('l',[0]*(9*9*7+1))
for i in range(10):
    t[i*i]=1
for i in range(0,6):
    nt=array('l',[0]*(9*9*7+1))
    for j in range(0,10):
        for k in range(j*j,9*9*(i+2)+1):
            nt[k]+=t[k-j*j]
    t=nt
def cycle(n):
    if n==1 or n==89:
        return n
    a,b,c=n/100,(n%100)/10,n%10
    return cycle(a*a+b*b+c*c)
nb = 0
for i,x in enumerate(t[1:]):
    nb += 0 if cycle(i+1)==1 else x
print nb