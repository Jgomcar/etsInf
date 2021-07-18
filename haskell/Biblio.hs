module Biblio where
 type Person = String
 type Book = String
 type Database = [(Person,Book)]
 exampleBase :: Database
 exampleBase = [("Alicia","El nombre de la rosa"),("Juan","La hija del canibal"),
                ("Pepe", "Odisea")]
                
 obtain :: Database -> Person -> [Book]
 obtain dBase thisPerson = [book |(person, book) <- dBase, person == thisPerson]
 
 borrow :: Database ->Book -> Person -> Database
 borrow dBase thisBook thisPerson = (thisPerson, thisBook) : dBase
 
 return' :: Database -> (Person, Book) -> Database
 return' [] _ =[]
 return' (db:dbx) (p,b) = if db == (p,b) then dbx 
                              else return' dbx(p,b)
