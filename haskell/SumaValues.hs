module SumaValues where
 sumavalues' :: Int -> Int -> Int
 sumavalues' a b = if a < b then a + sumavalues' (a + 1) b else
                   if a > b then a + sumavalues' (a-1) b else b
                  
