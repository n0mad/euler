import Data.List

continuedFraction :: Integer -> Integer -> Integer -> Integer -> (Integer, Integer, Integer)
continuedFraction a m d s =
    let mn = d*a - m
        dn = (s - mn*mn)`div` d
        s_sqrt = sqrt (fromInteger s)
        mn_f = fromInteger mn
        dn_f = fromInteger dn
        an = floor ( (s_sqrt + mn_f) / dn_f)
        in (an, mn, dn)
        
generateFractionR :: Integer -> Integer -> Integer -> Integer -> Integer -> [(Integer, Integer, Integer)]
generateFractionR a m d s 0 = [(a,m,d)]
generateFractionR a m d s depth = 
    let (an, mn, dn) = continuedFraction a m d s
    in (a, m, d) : generateFractionR an mn dn s (depth - 1)

generateFraction :: Integer -> Integer -> [(Integer, Integer, Integer)]
generateFraction depth s = generateFractionR (floor (sqrt (fromInteger s))) 0 1 s depth
            
findPeriod :: [(Integer, Integer, Integer)] -> Integer
--findPeriod [] = 
findPeriod list = findPeriodR (head (tail list)) (tail (tail list)) 1

findPeriodR :: (Integer, Integer, Integer) -> [(Integer, Integer, Integer)] -> Integer -> Integer
findPeriodR triplet list depth = 
    if triplet == (head list) then depth
    else findPeriodR triplet (tail list) (depth + 1)
    
isOdd :: Integer -> Bool
isOdd n = (1 == n `mod` 2)
    
doIt =
    let squareFree = [1..13] \\ (map (^2) [1..100])
        pqs =  (map (generateFraction 1000)  squareFree)
        periods = map findPeriod pqs -- = foldl max (0,0) pqs--mins = map (head) pqs
        odd_periods = filter isOdd periods
        in length (odd_periods)
