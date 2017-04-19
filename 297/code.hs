fibb :: [Integer]
fibb = 1:2: zipWith (+) fibb (tail fibb)

fibbDiff :: [Integer]
fibbDiff = zipWith (-)  (tail fibb) fibb

calc :: Integer -> Integer -> Integer -> [Integer] -> [Integer]
calc a b c list = (a + b + c) : (calc (a + b) c (a + b - 1 + (head (tail list))) (tail list))