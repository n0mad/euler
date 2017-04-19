import Data.Numbers.Primes

myprimes = takeWhile (\x -> x < 2*10^7) primes

calcPower :: Integer -> Integer