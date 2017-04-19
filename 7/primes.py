primes = [2]
count = 10001
n = 3
max_prime = 2

while len(primes) < count:
    divided = False
    for prime in primes:
        if prime > n**0.5:
            break
        if (n % prime == 0):
            divided = True
            break
    if not divided:
        primes.append(n)
        max_prime = n
    n += 1
print max_prime