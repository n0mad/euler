import Data.Ratio


contFracStep :: Ratio Integer -> Ratio Integer -> Ratio Integer
contFracStep x y = x + 1/y

all :: Int -> [Ratio Integer]
all n = map (\x -> 1/x + 1) (tail (scanr contFracStep 2 (take n (1:[2,2..]))))

--intLen :: Integer -> Int
--intLen n = length (show  n)

intLenAux :: Integer -> Integer
intLenAux 0 = 0
intLenAux n = 1  + (intLenAux (n `div` 10))


isGood :: Ratio Integer -> Bool
isGood n = (intLenAux (numerator n) ) /= ( intLenAux (denominator n))