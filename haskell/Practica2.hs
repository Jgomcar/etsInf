module Practica2 where 
 repeat' :: a -> [a]
 repeat' x = xs where xs = x:xs
 
 take' :: Int->[a]->[a]
 take' _[] = []
 take' n(x:t)
        | n <= 0 = []
        | otherwise = x : take' (n-1) t
       
 decBin :: Int -> [Int]
 decBin x = if x < 2 then [x]
            else (mod x 2) : decBin (div x 2)
            
 binDec :: [Int] -> Int 
 binDec (x:[]) = x
 binDec (x:y) = x + binDec y * 2
 
 divisors :: Int -> [Int]
 divisors n = [x| x <-[1..n], mod n x == 0]
 
 member :: Int -> [Int] -> Bool
 member n [] = False
 member n (x:t)
           | n == x = True
           | otherwise = member n t
 
 isPrime :: Int-> Bool
 isPrime n = if (length (divisors n)) <= 2 then True
             else False
 
 primes :: Int -> [Int]
 primes n = take n [x|x <- [1..], isPrime x]

        
 selectEven :: [Int] -> [Int]
 selectEven [] = []
 selectEven (x:t) = if mod x 2 == 0 then x : selectEven t
                    else selectEven t
                    
 selectEven' :: [Int] -> [Int]
 selectEven' xs = [x | x <-xs , even x]
 
 selectEvenPos :: [Int] -> [Int]
 selectEvenPos xs = [(!!) xs x| x <- [0..((length xs)-1)], even x]
 
 ins :: Int -> [Int] -> [Int]
 ins x [] = [x]
 ins x1 (x2:xs)
             | x1 < x2 = x1:x2:xs
             |otherwise = x2:(ins x1 xs)
             
 iSort :: [Int] -> [Int]
 iSort [] = []
 iSort (x:xs) = ins x (iSort xs)
 
 doubleAll :: [Int] -> [Int]
 doubleAll xs = map (*2) xs
 
 map' :: (a -> b) ->[a] -> [b]
 map' f xs = [f x|x <- xs] 
 
 filter' :: (a -> Bool) -> [a] -> [a]
 filter' f xs = [x | x <- xs, f x == True]
