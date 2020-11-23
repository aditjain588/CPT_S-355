import unittest
from HW4_part1 import *

class HW4Sampletests_part1(unittest.TestCase):
    #If the setUp doesn't clear the stacks succesfully, copy the following function to HW4_part1.py and call it in setup. 

    def setUp(self):
        #clear the opstack and the dictstack
        opstack [:] = []
        dictstack [:] = []  

    # Tests for helper functions : define, lookup   
    def test_lookup1(self):
        dictPush({'/v':3, '/x': 20})
        dictPush({'/v':4, '/x': 10})
        dictPush({'/v':5})
        self.assertEqual(lookup('x'),10)
        self.assertEqual(lookup('v'),5)

    def testLookup2(self):
        dictPush({'/a':355})
        dictPush({'/a':[3,5,5]})
        self.assertEqual(lookup("a"),[3,5,5])

    def test_define1(self):
        dictPush({})
        define("/n1", 4)
        self.assertEqual(lookup("n1"),4)

    def test_define2(self):
        dictPush({})
        define("/n1", 4)
        define("/n1", 5)
        define("/n2", 6)
        self.assertEqual(lookup("n1"),5)
        self.assertEqual(lookup("n2"),6)        

    def test_define3(self):
        dictPush({})
        define("/n1", 4)
        dictPush({})
        define("/n2", 6)
        define("/n2", 7)
        dictPush({})
        define("/n1", 6)
        self.assertEqual(lookup("n1"),6)
        self.assertEqual(lookup("n2"),7)    
    #-----------------------------------------------------
    #Arithmatic operator tests
    def test_add(self):
        #9 3 add
        opPush(9)
        opPush(3)
        add()
        self.assertEqual(opPop(),12)

    def test_sub(self):
        #10 2 sub
        opPush(10)
        opPush(2)
        sub()
        self.assertEqual(opPop(),8)

    def test_mul(self):
        #2 40 mul
        opPush(2)
        opPush(40)
        mul()
        self.assertEqual(opPop(),80)
    #-----------------------------------------------------
    #Comparison operators tests
    def test_eq1(self):
        #6 6 eq
        opPush(6)
        opPush(6)
        eq()
        self.assertEqual(opPop(),True)

    def test_eq2(self):
        #[1 2 3 4] [4 3 2 1] eq
        opPush([1,2,3,4])
        opPush([4,3,2,1])
        eq()
        self.assertEqual(opPop(),False)

    def test_lt(self):
        #3 6 lt
        opPush(3)
        opPush(6)
        lt()
        self.assertEqual(opPop(),True)

    def test_gt(self):
        #4 5 gt
        opPush(4)
        opPush(5)
        gt()
        self.assertEqual(opPop(),False)

    #-----------------------------------------------------
    #stack manipulation operator tests
    def test_dup(self):
        #[3 5 5 True 4]  dup
        opPush([3,5,5,True,4])
        dup()
        isSame = opPop() is opPop()
        self.assertTrue(isSame)

    def test_exch(self):
        # /x 10 exch
        opPush('/x')
        opPush(10)
        exch()
        self.assertEqual(opPop(),'/x')
        self.assertEqual(opPop(),10)

    def test_pop(self):
        l1 = len(opstack)
        opPush(10)
        pop()
        l2 = len(opstack)
        self.assertEqual(l1,l2)

    def test_copy(self):
        #true 1 3 4 3 copy
        opPush(True)
        opPush(1)
        opPush(3)
        opPush(4)
        opPush(3)
        copy()
        self.assertTrue(opPop()==4 and opPop()==3 and opPop()==1 and opPop()==4 and opPop()==3 and opPop()==1 and opPop()==True)
        
    def test_clear(self):
        #10 /x clear
        opPush(10)
        opPush("/x")
        clear()
        self.assertEqual(len(opstack),0)

    #-----------------------------------------------------
    #String operator tests
    def test_length(self):
        #(CptS355) length
        opPush('(CptS355)')
        length()
        self.assertEqual(opPop(),7)      
        self.assertTrue(len(opstack)==0) 
        #length will not push back the string onto the opstack      

    def test_get(self):
        #(CptS355) 3 get
        opPush('(CptS355)')
        opPush(3)
        get()
        self.assertEqual(opPop(),83)
        self.assertTrue(len(opstack)==0)
        #get will not push back the string onto the opstack 
    
    def test_get1(self):
        opPush('(12345)')
        opPush(1)
        get()
        self.assertEqual(opPop(),50)
        self.assertTrue(len(opstack)==0)
    
    def test_getinterval(self):
        #(CptS355-and-CptS322) 8 3 getinterval
        opPush('(CptS355-and-CptS322)')
        opPush(8)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),'(and)')         
        self.assertTrue(len(opstack)==0) 
        #getinterval will not push back the string onto the opstack      
    
    def getinterval2(self):
        opPush('(Cpts355-and-Cpts322)')
        opPush(4)
        opPush(3)
        getinterval()
        opPush('(Cpts355-and-Cpts322)')
        opPush(12)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),'(322)')         
        self.assertTrue(len(opstack)==0) 

    def test_putinterval1(self):
        #(CptS355-and-CptS322) dup 4 (451) putinterval
        opPush('(CptS355-and-CptS322)')
        dup()  #duplicating the string reference
        opPush(4)
        opPush('(451)')
        putinterval()  #putinterval will not push back the changed string onto the opstack 
        self.assertEqual(opPop(),'(CptS451-and-CptS322)')  #we pop the string reference we copied with "dup"
        self.assertTrue(len(opstack)==0)

    def test_putinterval2(self):
        # /x (CS451) def x 0 (EE) putinterval x
        x = '(CS451)'
        define('/x',x)
        opPush(x) #pushing the string reference onto the stack
        opPush(0)
        opPush('(EE)')
        putinterval()  #put will not push back the changed string onto the opstack 
        self.assertEqual(lookup('x'),'(EE451)') #we pop the string reference we bound to name /x     
        self.assertTrue(len(opstack)==0)

    def test_putinterval3(self):
        #(CptS355-and-CptS322) dup dup 4 (4) putinterval  16 (4) putinterval
        opPush('(CptS355-and-CptS322)')
        dup() # we duplicate the string reference
        dup() # we duplicate the string reference once more
        opPush(4)
        opPush('(4)')
        putinterval()
        opPush(16)
        opPush('(4)')
        putinterval()
        self.assertEqual(opPop(),'(CptS455-and-CptS422)')
        self.assertTrue(len(opstack)==0)

    def putinterval4(self):
        opPush('(Cpts360)')
        dup()
        dup()
        dup()
        dup()
        opPush(4)
        opPush('(260)')
        putinterval()
        self.assertEqual(opPop(),'(Cpts260)')
        self.assertTrue(len(opstack)==0)

    def test_search1(self):
        # (355-322-451) (-) search
        #push the string that will be split
        opPush('(355-322-451)')
        #push the 'seek' string
        opPush('(-)')
        search()
        self.assertTrue(opPop()==True and opPop()=='(355)' and opPop()=='(-)' and opPop()=='(322-451)')

    def test_search2(self):
        # (355-321) (22) search
        #push the string that will be split
        opPush('(355-321)')
        #push the 'seek' string
        opPush('(22)')
        search()
        self.assertTrue(opPop()==False and opPop()=='(355-321)')

    def test_search3(self):
        opPush('(123234)')
        opPush('(112)')
        search()
        self.assertTrue(opPop()==False and opPop()=='(123234)')
    #-----------------------------------------------------
    #Array operator tests
    def test_evaluateArray(self):
        define('/x',2)
        define('/y',5)  
        # [1 x 3 4 y 6]
        # [1 1 1 add y x sub] 
        # [(aBCd) 1 2 getinterval (BC) eq]
        self.assertEqual(evaluateArray([1,'x',3,4,'y',6]), [1,2,3,4,5,6])
        self.assertEqual(evaluateArray([1,1,1,'add','y','x','sub']), [1,2,3])
        self.assertEqual(evaluateArray(['(aBCd)',1,2,'getinterval','(BC)','eq']), [True])


    def test_aload(self):
        #[3 5 5 True4] aload
        opPush([True,'(CptS)',3,5,5,'(Fall)',2020])
        aload()
        self.assertTrue(opPop()==[True,'(CptS)',3,5,5,'(Fall)',2020] and opPop()==2020 and opPop()=='(Fall)' and opPop() == 5 and opPop()==5
                        and opPop() == 3  and opPop()=='(CptS)' and opPop()== True)  

    def test_astore(self):
        # 1 2 3 4 true (end) [0 0 0 0] astore
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(True)
        opPush('(end)')
        opPush([0,0,0,0])  # the array doesn't necessarily neeed to have 0 values. 
        astore()
        self.assertTrue(opPop()==[3,4,True,'(end)'] and opPop()==2 and opPop()==1)  
    
    #-----------------------------------------------------
    #dictionary stack operators
    def test_dict(self):
        #1 dict
        opPush(1)
        psDict()
        self.assertEqual(opPop(),{})

    def test_psDef(self):
        #/x 10 def /x 20 def x
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        opPush("/x")
        opPush(20)
        psDef()
        self.assertEqual(lookup('x'),20)

    def test_psDef2(self):
        #/x 10 def 1 dict begin /y 20 def x
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        dictPush({})
        opPush("/y")
        opPush(20)
        psDef()
        self.assertEqual(lookup('x'),10)

    def test_psDef3(self):
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        dictPush({})
        opPush("/x")
        opPush(20)
        psDef()
        dictPush({})
        opPush("/x")
        opPush(30)
        psDef()
        self.assertEqual(lookup('x'),30)

    def test_beginEnd(self):
        #/x 3 def 1 dict begin /x 4 def end x
        opPush(1)
        psDict()
        opPush("/x")
        opPush(3)
        psDef()
        opPush(1)
        psDict()
        begin()
        opPush("/x")
        opPush(4)
        psDef()
        end() 
        self.assertEqual(lookup('x'),3)

    def test_psDef3(self):
        #/x 3 def 1 dict begin /x 30 def 1 dict begin /x 300 def end x
        # define x in the bottom dictionary
        dictPush({})
        opPush("/x")
        opPush(3)
        psDef()
        # define x in the second dictionary
        dictPush({})
        opPush("/x")
        opPush(30)
        psDef()
        # define x in the third dictionary
        dictPush({})
        opPush("/x")
        opPush(300)
        psDef()
        dictPop()
        self.assertEqual(lookup('x'),30)

    def test_begin(self):
        opPush(2)
        begin()
        self.assertEqual(dictPop(),{})

    def test_end(self):
        dictPush({"x":2})
        end()
        self.assertEqual(len(dictstack),0)

    #Tests to check "error checking"

    # #  Make sure that the following test prints/raises an error message about the type of the bottom argument
    # #  Also make sure that the opstack content is : ['(test)', 10]
    # def test_subInputs(self):
    #     opPush('(test)')
    #     opPush(10)
    #     sub()
    #     print(opstack)

    # # Make sure that the following test prints/raises an error message about the type of the botton argument (the variable name needs be a string)
    # # 4 pts
    # def test_psDefInputs(self):
    #     opPush(1)
    #     opPush(10)
    #     psDef()
    #     print(opstack)"""

if __name__ == '__main__':
    unittest.main()

