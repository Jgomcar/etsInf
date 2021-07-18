module Arboles where 
 
 data Tree a = Leaf a | Branch (Tree a) (Tree a) deriving Show
 numleaves :: Tree a -> Int
 numleaves (Leaf x) = 1
 numleaves (Branch a b) = numleaves a + numleaves b
 
 data BinTreeInt = Void | Node Int BinTreeInt BinTreeInt deriving Show
 
 --Ejercicio 12
 symmetric :: Tree a -> Tree a
 symmetric (Leaf a) = Leaf a
 symmetric (Branch a b) = Branch (symmetric b) (symmetric a)
 
 --Ejercicio 13
 list2tree :: [a] -> Tree a
 list2tree (x:[]) = Leaf x
 list2tree (x:xs) = Branch (Leaf x) (list2tree xs)
 
 tree2list :: Tree a -> [a]
 tree2list (Leaf a) = [a]
 tree2list (Branch a b) = tree2list a ++ tree2list b

--Ejercicio 14
 insTree :: Int -> BinTreeInt -> BinTreeInt
 insTree e Void = Node e Void Void
 insTree e (Node x izq der)
          | e <= x = Node x (insTree e izq) der
          | e > x = Node x izq (insTree e der)
