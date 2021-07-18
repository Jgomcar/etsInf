module Figure where
 type Xpos = Float
 type Ypos = Float
 type Pos = (Xpos, Ypos)
 type Radius = Float
 type Base = Float
 type Height = Float
 data Shape = Circle Pos Radius | Rectangle Pos Base Height deriving Show
