-- Name: Adit Jain

module HW2
     where

import Data.Char
import Data.List (sort)
-- 1
{- (a) merge2 5%-}
merge2 :: [a] -> [a] -> [a]
merge2 [] [] = []
merge2 (x:xs) [] = x:xs
merge2 [] (y:ys) = y:ys
--merge2 (x:xs) (y:ys) if (x > y) then x:merge2 xs (y:ys) else = y:merge2 (x:xs) ys
merge2 (x:xs) buf = x : (merge2 buf xs)                        

{- (b) merge2Tail 10% -}

mergeHelp :: Ord a => [a] -> [a] -> [a] -> [a]
mergeHelp [] [] buf = buf
mergeHelp (x:xs) [] buf = revAppend buf (x:xs)
mergeHelp [] (y:ys) buf = revAppend buf (y:ys)
--mergeHelp (x:xs) (y:ys) if (x > y) then x:mergeHelp xs (y:ys) else = y:mergeHelp (x:xs) ys
--mergeHelp (x:xs) il buf = x : (mergeHelp il xs buf)
mergeHelp (x:xs) il buf = mergeHelp il xs (x:buf)


revAppend :: [a] -> [a] -> [a]
revAppend [] acc = acc
revAppend (x:xs) acc = revAppend xs (x:acc)

merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail [] [] = []
merge2Tail (x:xs) [] = mergeHelp (x:xs) [] []
merge2Tail [] (x:xs) = mergeHelp [] (x:xs) []
merge2Tail (x:xs) (y:ys) = mergeHelp (x:xs) (y:ys) []
{-
merge2Tail [] [] = []
merge2Tail li [] = li
merge2Tail [] li = li
merge2Tail (x:xs) (y:ys) = merge2Tailhelper [] (x:xs) (y:ys)

merge2Tailhelper acc [] [] = acc
merge2Tailhelper acc [] (x:xs) = merge2Tailhelper (acc ++ [x]) xs []
merge2Tailhelper acc (x:xs) (y:ys) = merge2Tailhelper (acc ++ [x]) (y:ys) xs-}

     

{- (c) mergeN 5%-}


mergeN xs = foldl merge2 [] xs

-- 2
{- (a) removDuplicates 10% -}

iskey acc x = if x `elem` acc then acc else acc ++ [x]

removeDuplicates:: Eq a => [a] -> [a]
removeDuplicates il  = foldl iskey [] il 
 

{- (b) count 5% -}

--count x xs = (length . filter (==x)) xs
helper v x = (v==x)
count v xs = length (filter(helper v) xs)


{- (c) histogram 10% -}

histogram :: Eq a => [a] -> [(a, Int)]
histogram  [] = []
histogram (x:xs) = (x,(count x xs)+1) : histogram xs'
     where xs' = xs

-- 3                

{- (a) concatAll 4% -}

helper1 xl = foldr (++) "" xl

concatAll :: [[String]] -> String
concatAll il = helper1 (map helper1 il) 


{- (b) concat2Either 9% -}               
data AnEither  = AString String | AnInt Int 
                deriving (Show, Read, Eq)


helper2 :: AnEither -> AnEither -> AnEither
helper2 (AString x) (AString y)  = AString (x++y) 
helper2 (AString x) (AnInt y) = AString (x++(show(y)))
helper2 (AnInt x) (AString y) = AString (y++(show(x)))
helper2 (AnInt x) (AnInt y) = AString ((show(x))++(show(y)))


concat2Either2 :: [AnEither] -> AnEither
concat2Either2 (x:xs) = (foldl helper2 x xs)
concat2Either2 [] = AString ""

concat2Either :: [[AnEither]] -> AnEither
concat2Either xl = concat2Either2 (map concat2Either2 xl)

--concat2Either2 [] = AString ""

{- (c) concat2Str 6% -}               

helper3 (AString x) y  =  (x++y) 
--helper3 x (AnInt y) =  (x++(show(y)))
helper3 (AnInt x) y =  (y++(show(x)))
--helper3 (AnInt x) (AnInt y) =  ((show(x))++(show(y)))

concatHelp3b (x:xs) = (foldr helper3 "" (x:xs))
concatHelp3b [] = ""

concat2Str il = concat (map concatHelp3b il)

-- 4 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y


data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}
evaluateTree :: ExprTree Int -> Int
evaluateTree (ELEAF x) = x
evaluateTree (ENODE Add l r) = evaluateTree l + evaluateTree r
evaluateTree (ENODE Sub l r) = evaluateTree l - evaluateTree r
evaluateTree (ENODE Mul l r) = evaluateTree l * evaluateTree r
evaluateTree (ENODE Pow l r) = evaluateTree l ^ evaluateTree r

{- (b) printInfix - 10% -}

show' Add x y = show (show' Add x y)

printInfix:: Show a => ExprTree a -> String 
printInfix (ELEAF x) = show x
printInfix (ENODE Add t1 t2) = "(" ++ printInfix t1++ " " ++ "`"  ++ show Add ++ "`" ++ " " ++ printInfix t2 ++ ")" 
printInfix (ENODE Sub t1 t2) = "(" ++ printInfix t1++ " " ++ "`"  ++ show Sub ++ "`" ++ " " ++ printInfix t2 ++ ")"
printInfix (ENODE Mul t1 t2) = "(" ++ printInfix t1++ " " ++ "`"  ++ show Mul ++ "`" ++ " "  ++ printInfix t2 ++ ")"
printInfix (ENODE Pow t1 t2) = "(" ++ printInfix t1++ " " ++ "`"  ++ show Pow ++ "`" ++ " " ++printInfix t2 ++ ")"

{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)


createRTree :: ExprTree Int -> ResultTree Int
createRTree (ELEAF x) = RLEAF x
createRTree (ENODE Add t1 t2) =  RNODE (evaluateTree t1 + evaluateTree t2) (createRTree t1) (createRTree t2)
createRTree (ENODE Sub t1 t2) =  RNODE (evaluateTree t1 - evaluateTree t2) (createRTree t1) (createRTree t2)
createRTree (ENODE Mul t1 t2) =  RNODE (evaluateTree t1 * evaluateTree t2) (createRTree t1) (createRTree t2)
createRTree (ENODE Pow t1 t2) =  RNODE (evaluateTree t1 ^ evaluateTree t2) (createRTree t1) (createRTree t2)

-- 5
{-Sample trees 4% -}
exprtree3 = (ENODE Add (ENODE Add (ENODE Mul (ELEAF 3)(ELEAF 5))(ELEAF 20)) (ENODE Add (ENODE Mul(ELEAF 2)(ELEAF 4))(ELEAF 10)))  
exprtree4 = (ENODE Mul (ENODE Pow (ELEAF 2)(ELEAF 4))(ENODE Add (ENODE Sub (ELEAF 30)(ELEAF 10))(ELEAF 20)))


main = do print(evaluateTree (exprtree3))
          print(printInfix (exprtree3))
          print(createRTree (exprtree3))
          print(evaluateTree (exprtree4))
          print(printInfix (exprtree4))
          print(createRTree (exprtree4))