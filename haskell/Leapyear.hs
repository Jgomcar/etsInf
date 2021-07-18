module Leapyear where
 leap' :: Int -> Bool
 leap' a = if mod a 4 == 0 && mod a 100 /= 0 then True else
           if mod a 400 == 0 then True else False 
             
 daysAmonth :: Int -> Int -> Int
 daysAmonth m y = if leap' y == True && m == 2 then 29 else
                  if m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12 
                    then 31 else 30
