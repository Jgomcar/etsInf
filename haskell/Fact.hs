module Fact where
 fact :: Int -> Int
 fact 0 = 1
 fact n = n * fact (n - 1)
 
 sumFact :: Int -> Int
 sumFact n = if n >= 0 then fact n + sumFact(n - 1) else -1
