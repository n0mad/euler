def getPrimes(m)
    k = m
    primes = []
    for i in 2..m do
        if (k > 1 ) then
            already  = false
            while (0 == k % i)
                k = k / i
                if not already then
                    primes << i
                    already = true
                end
            end
        end
    end
    return primes
end

def getUniq(m)
    return getPrimes(m).length
end

start = 10
primes = [getUniq(start), getUniq(start + 1), getUniq(start + 2), getUniq(start + 3)]
bool = primes.collect { |i| i == 4 }

for i in (start + 4)..1000000 do
    primes[0], primes[1], primes[2], primes[3] =  primes[1], primes[2], primes[3], getUniq(i)
    bool[0],  bool[1], bool[2], bool[3] = bool[1], bool[2], bool[3], getUniq(i) == 4
    if (primes[0] == 4) and (primes[1] == 4) and (primes[2] == 4) and (primes[3] == 4) then
        puts primes
        puts "----"
        puts "#{i}"
    end
end