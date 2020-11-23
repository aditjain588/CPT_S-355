-- Name: Adit Jain

module HW1
where

import Data.Char

-- 1a bigger date and maxbate
biggerDate::(Ord a1,Ord a2,Ord a3)=>(a3,a2,a1)->(a3,a2,a1)->(a3,a2,a1)
biggerDate (x1,y1,z1) (x2,y2,z2)= if z1>z2 then (x1,y1,z1) else if z1<z2 then (x2,y2,z2) else if y1>y2 then (x1,y1,z1) else if y1<y2 then (x2,y2,z2) else if x1>x2 then (x1,y1,z1) else (x2,y2,z2) 

--1b maxDate
maxDate :: (Ord a1,Ord a2, Ord a3) => [(a3,a2,a1)]->(a3,a2,a1)
maxDate[] = error "List is empty"
maxDate[x] = x
maxDate (x:xs) = x `biggerDate` (maxDate xs)


--2a ascending
ascending :: Ord t => [t] -> Bool
ascending [] = True
ascending [x] = True
ascending(x:y:ys) | (x<=y) = ascending(ys)
                  | otherwise = False

--3a insert   
insert :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
insert 0 item il = item:insert 10 item il
insert _ _ [] = []
insert n item (x:xs) = x:insert (n-1) item xs


--3b insertEvery
insertEvery :: (Eq t, Num t) => t -> a ->[a] -> [a]
insertEvery n item il = helper n il where
  helper n [] = [] 
  helper 0 xs = item: insertEvery n item xs
  helper n (x:xs) = x:helper(n-1) xs
                  
--5a 
split' c [] buf = (reverse buf):[]
split' c (x:xs) buf = if (x/=c) then (split' c xs (x:buf))
                      else (reverse buf):(split' c xs [])

--5b
nsplit' 0 c [] buf = (reverse buf):[]
nsplit' n c (x:xs) buf = if (x/=c) then (nsplit' n c xs (x:buf))
                         else if(x==c) && (n/=0) then (reverse buf):(nsplit' (n-1) c xs [])
                         else (nsplit' 0 c xs (x:buf))


main = do print(split' ',' "Courses:,CptS355,CptS322,CptS451,CptS321" "") --------------5a
          print(split' 0  [1,2,3,0,4,0,5,0,0,6,7,8,9,10] [])  -------------------5a
          print(split' 0  [1,2,3,4,0,5,6,7,8,9,10] [])---------------5a
          print(split' 0  [1,2,3,4,0,5,0,0,0,7,8,9,10] [])----------------------5a
          print(nsplit' 1 ',' "Courses:,CptS355,CptS322,CptS451,CptS321" "")-------------------5b
          print(nsplit' 2 ','"Courses:,CptS355,CptS322,CptS451,CptS321" "")----------------5b
          print(nsplit' 4 ','"Courses:,CptS355,CptS322,CptS451,CptS321" "")---------------5b
          print(nsplit' 3 ','"Courses:,CptS355,CptS322,CptS451,CptS321" "")----------------5b
          print(nsplit' 3 0 [1,2,3,0,4,0,5,0,0,6,7,8,9,10] [])--------------5b
          print(nsplit' 3 0 [1,2,3,0,4,0,5,0,0,0,0,0,0] [])---------------5b
          print(nsplit' 3 0 [1,2,3,0,4,5,6] [])--------------5b
