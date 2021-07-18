module Remainder where 
 remainder' :: Int -> Int -> Int
 remainder' a b = if a < 0 || b <= 0 then -1 else
                 if a < b then a else
                  remainder' (a - b) b
