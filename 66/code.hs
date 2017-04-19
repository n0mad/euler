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
        
generateFractionR :: Integer -> Integer -> Integer -> Integer -> Integer -> [Integer]
generateFractionR a m d s 0 = [a]
generateFractionR a m d s depth = 
    let (an, mn, dn) = continuedFraction a m d s
    in a : generateFractionR an mn dn s (depth - 1)

generateFraction :: Integer -> Integer -> [Integer]
generateFraction s depth = generateFractionR (floor (sqrt (fromInteger s))) 0 1 s depth
            
generatePQR :: Integer -> Integer -> Integer -> Integer -> [Integer] -> [(Integer, Integer)]
generatePQR pn_1 pn qn_1 qn [] = [(pn, qn)]
generatePQR pn_1 pn qn_1 qn fractionList = 
    let a = head fractionList
        pnext = pn * a + pn_1
        qnext = qn * a + qn_1
    in
    (pn,qn) : generatePQR pn pnext qn qnext (tail fractionList)

generatePQ :: Integer -> Integer -> [(Integer, Integer)]
generatePQ depth d = 
            let 
                fractionList = generateFraction d depth
                a0 = head fractionList
                a1 = head (tail fractionList)
                p0 = a0
                p1 = a0*a1 + 1
                q0 = 1
                q1 = a1
            in generatePQR p0 p1 q0 q1 (tail (tail fractionList))

check :: Integer -> (Integer, Integer) -> Bool
check d (first, second) = 1 == first*first - d*second*second

generateAndCheck :: Integer -> Integer -> (Integer, Integer)
generateAndCheck depth d = 
                foldl (min) (10^100,1000^100) (filter (check d) (generatePQ depth d))
        
doIt =
    let squareFree = [1..1000] \\ (map (^2) [1..33])
        pqs =  (map (generateAndCheck 100)  squareFree)
        t = foldl max (0,0) pqs--mins = map (head) pqs
    in t--pqs
        