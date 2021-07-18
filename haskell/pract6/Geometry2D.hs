module Geometry2D (areaSquare, perimeterSquare) where

   areaRectangle :: Float -> Float -> Float
   areaRectangle base altura = base * altura
   
   perimeterRectangle :: Float -> Float -> Float
   perimeterRectangle base altura = 2 * (base + altura)
   
   areaSquare :: Float -> Float
   areaSquare side = areaRectangle side side
   
   perimeterSquare :: Float -> Float 
   perimeterSquare side = perimeterRectangle side side
