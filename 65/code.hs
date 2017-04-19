import Data.Ratio
continued :: Integer -> [Integer]
continued n = 1:n:1: continued (n + 2)


fractionR :: Integer -> [Integer] -> Rational
fractionR 0 continued = fromInteger (head continued)
fractionR depth continued = 
        let toadd = fromInteger (head continued)
            fract = fractionR (depth - 1) (tail continued)
        in  toadd + 1 / fract
        
fraction [x] = x%1
fraction (x:xs) = x%1 + 1/(fraction xs)

--main =
--    fractionR 98 (continued 2)