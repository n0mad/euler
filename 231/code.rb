require 'java'

def init(bound)
    sieve = Java::int[Bound+1].new
    for k in 2..Bound do
        sieve[k] = k
    end
    return sieve
end

def dump(a, size)
    for k in 0...size do
        print "#{a[k]} "
    end
end

def toadd(t, prime)
    s = 0
    while 0 == t % prime do
        s += prime
        t = t / prime
    end
    return s
end

def markPrimes(sieve, bound, bound_a, bound_b)
    total_sum = 0
    
    for k in 2..bound do
        if sieve[k] != 0 then
            sieve[k] = 0
            factor = 1
            while 1 do
                t = factor * k
                if t > Bound:
                    break
                end
                
                sieve[t] = 0
                
                if t <= bound_a then
                    sieve[k] -= toadd(t, k)
                end
                if t > bound_b then
                    sieve[k] += toadd(t,k)
                end
                
                factor += 1
                
            end
        end
    end
    return sieve
end

Bound = 20000000
sieve = init(Bound)
#markPrimes(sieve, Bound, 3, 7)
markPrimes(sieve, 20000000, 5000000, 15000000)

#dump(sieve, Bound + 1)
puts
puts sieve.reduce { |x,y|
                        x + y
                   }
        