module NumCbetw2 where
 import Data.Char
 numCbetw2 :: Char -> Char -> Int
 numCbetw2 a b = abs((ord b) - (ord a)) - 1
