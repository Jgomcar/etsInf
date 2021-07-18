module Max where
 max' :: Int -> Int -> Int
 max' a b = if a > b then a else 
            if a < b then b else a
