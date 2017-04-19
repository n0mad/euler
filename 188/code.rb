
def order(n, m)
    e, k = 1, n % m
    while 1 != k do
        k = (k * n) % m
        e += 1
    end
    return e
end

def exp(a, e, m)
  r, b, k = 1, a, e
  while (k > 0)
    r = (r * b) % m if k & 1 == 1
    k >>= 1
    b = (b * b) % m
    return 0 if b == 0
    return r if b == 1
  end
  r
end

def hyperexp(base, power, modulo)
    return 0 if modulo == 1
    return base % modulo if power == 1
    ord = order(base, modulo)
    power = hyperexp(base, power - 1, ord)
    return exp(base, power, modulo)
end
    
print hyperexp(1777, 1855, 10**8)