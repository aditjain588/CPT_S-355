# Adit Jain

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    if (len(opstack)>0):
        i=opstack[-1]
        opstack.pop()
    else:
        print("Empty List")
        return 0   
    return(i)
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)
    return opstack

#-------------------------- 16% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if(len(dictstack)>0):
        i=dictstack[-1]
        dictstack.pop()
    #print(dictstack)
    return (i)
    # dictPop pops the top dictionary from the dictionary stack.


def dictPush(d):
    dictstack.append(d)
    return dictstack
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.


def define(name,value,scope):
    if(scope=="dynamic" or scope=="static"):
        if(len(dictstack)==0):
            dictPush((0,{name:value}))
        else:
            op=dictstack[-1]
            (k,v)=op
            v[name]=value


def lookup(name,scope):
    if(name[0]!='/'):
        name='/'+name
    #for i in dictstack[::-1]:
    if(scope=="dynamic"):
        for (k,v) in dictstack[::-1]:
            for (k1,v1) in v.items():
                if (k1==name):
                    opPush(v1)
                    return (v1)
    elif(scope=="static"):
        return(lookupHelper(dictstack,name,scope))
    print("Error: Name",name ," not found")
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

def lookupHelper(dictstack,name,scope):
    if(name[0]!='/'):
        name='/'+name
    val=dictstack[-1][0]
    #print("val is ",val)
    i=val+1-len(dictstack)
    
    for a,b in dictstack[::-1]:   
        for x1,y1 in b.items():
            if(x1==name):
                opPush(y1)
                #print(y1)
                return y1
        return lookupHelper(dictstack[:i],name,scope)

def staticLink(name):
    return(staticLinkHelper(dictstack,name))

def staticLinkHelper(dictstack,name):
    if(name[0]!='/'):
        name='/'+name
    val=dictstack[-1][0]
    #print("val is ",val)
    i=val+1-len(dictstack)

    for a,b in dictstack[::-1]:   
        for x1,y1 in b.items():
            if(x1==name):
                #print(a)
                return a
        return staticLinkHelper(dictstack[:i],name)

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            print("Error: add - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        print("Error: add expects 2 operands")


def sub():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op2-op1)
        else:
            print("Error: sub - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: sub expects 2 operands")
    

def mul():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1*op2)
        else:
            print("Error: mul - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: mul expects 2 operands")
    

def eq():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)) or (isinstance(op1,list) and isinstance(op2,list)):
            if(op1 == op2):
                opPush(True)
            else:
                opPush(False)
        elif(isinstance(op1,str) and isinstance(op2,str)):
            if(op1==op2):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: eq - only the opearands with same type can be compared")
            opPush(op1)
            opPush(op2)         
    else:
        print("Error: eq expects 2 operands")

def lt():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            if(op1<=op2):
                opPush(False)
            else:
                opPush(True)
        else:
            print("Error: lt - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: lt expects 2 operands")

def gt():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            if(op1>=op2):
                opPush(False)
            else:
                opPush(True)
        else:
            print("Error: gt - one of the operands is not a numberical value")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error: gt expects 2 operands")



#--------------------------- 20% -------------------------------------
# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if(len(opstack)>0):
        op=opPop()
        if(isinstance(op,str)):
            opPush(len(op)-2)
        else:
            print("Error: expected string argument")
            opPush(op)
    else:
        print("Error: Not enough arguments in opStack to perform lenght()")

def get():
    if(len(opstack)>0):
        index=opPop()
        str1=opPop()
        if(isinstance(str1, str)):
            x=str1[index+1]
            opPush(ord(x))
        else:
            print("Error: expected string argument")
            opPush(str1)
            opPush(index)
    else:
        print("Error: Not enough arguments in opStack to perform get()")


def getinterval():
    if(len(opstack)>2):
        count=opPop()
        index=opPop()
        str1=opPop()
        if(isinstance(str1,str)):
            x=str1[(index+1):(index+count+1)]
            x="(" + x + ")"
            opPush(x)
        else:
            print("Error: expected string argument")
            opPush(str1)
            opPush(index)
            opPush(count)
    else:
        print("Error: Not enough arguments in opStack to perform getinterval()")

def putinterval():
    if(len(opstack)>2):
        str2=opPop()
        index=opPop()
        str1=opPop()
        if(isinstance(str1,str)):
            ans=str1[:index+1] + str2[1:len(str2)-1] +str1[len(str2)-1+index:]
            for i in range(0,len(opstack)):
                if (opstack[i]==str1):
                    opstack[i] = ans
                else:
                    pass
            if(len(dictstack)!=0):
                for (k,v) in dictstack:
                    for (k1,v1) in v.items():
                            if (v1==str1):
                                i[k]=ans
        else:
             print("Error: expected string argument")
             opPush(str1)
             opPush(index)
             opPush(str2)
    else:
        print("Error: Not enough arguments in opStack to perform getinterval()")


def search():
    if(len(opstack)>0):
        seek=opPop()
        seek1=seek
        str1=opPop()
        seek=seek[1:len(seek)-1]
        print(seek)
        if seek in str1:    
            x=str1.split(seek,1)
            x[1] = "(" +x[1]
            x[0] = x[0]+")"
            opPush(x[1])
            opPush(seek1)
            opPush(x[0])
            opPush(True)
        else:
            opPush(str1)
            opPush(False)
    else:
        print("Error: Not enough arguments in opStack to perform search()")


#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

#

##############
################### evaluateArray at end of part 1 before beginning of part 2############
##############


def aload():
    op=opPop()
    for i in op:
        opPush(i)
    opPush(op)
    return opstack


def astore():
    op=opPop()
    for i in range(len(op)):
        op[i] = opPop()
    op=list(reversed(op))
    opPush(op)


#--------------------------- 6% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if len(opstack) > 0:
        op1 = opPop()
        opPush(op1)
        opPush(op1)
        #print(opstack)
    else:
        print("Empty list cannot be duplicated")

def copy():
    if(len(opstack) > 0):
        count = opPop()
        copyList = []
        for  x in range(0,count):
            copyList.append(opPop())
        for item in reversed(copyList):
            opPush(item)
        for item in reversed(copyList):
            opPush(item)
    else:
        print("Error: copy - not enough arguments")

def count():
    count=len(opstack)
    opPush(count)

def pop():
    if (len(opstack) > 0):
        opPop()

def clear():
    opstack [:] = []
    dictstack[:] = []

def exch():
    op1=opPop()
    op2=opPop()
    opPush(op1)
    opPush(op2)

def stack():
    print(opstack)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    opPop()
    opPush({})
    return dictstack

def begin():
    op1=opPop()
    #op2=opPop()
    dictPush({})

def end():
    dictPop()

def psDef(scope):
    v=opPop()
    k=opPop()
    if(isinstance(k,str)):
        define(k,v,scope)
    else:
        print("Error: String argument expected but got ", type(k))
        opPush(k)
        opPush(v)

eval_funcs = {'pop':opPop,'dictpush':dictPush,'dictpop':dictPop,'push':opPush,'add':add,'sub':sub,'mul':mul,'eq':eq,'lt':lt,'gt':gt,'exch':exch,'begin':begin,'end':end,'dict':psDict,'def':psDef,'clear':clear,'length':length,'get':get,'search':search,'getinterval':getinterval,'putinterval':putinterval,'dup':dup,'stack':stack,'aload':aload,'astore':astore,'count':count,'copy':copy}
def evaluateArray(aInput,scope):
    res=[]
    opPush('[')
    for i in aInput:
        if(isinstance(i,int) or (isinstance(i,bool))):
            opPush(i)
        elif(isinstance(i,str)):
            if(i[0]=='('):
                opPush(i)
            elif(i in eval_funcs.keys()):
                f=eval_funcs[i]   
                f()
            else:
                lookup(i,scope)

    for i in opstack[::-1]:
        if(i=='['):
            break
        else:
            res.append(opPop())

    opPop()
    res.reverse()
    return (res)


################################################################################################################
################################################## PART 2 ######################################################
################################################################################################################

import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)  


def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            try:
                res.append(int(c))
            except ValueError:
                if(c[0]=='['):
                    a=c.strip('][').split(' ')
                    for i in range(0,len(a)):
                        try:
                            a[i]=int(a[i])
                        except ValueError:
                            pass
                        a[i]=int(a[i])
                    res.append(a)
                else:
                    res.append(c)
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            try:
                res.append(int(c))
            except ValueError:
                if(c[0]=='['):
                    a=c.strip('][').split(' ')
                    for i in range(0,len(a)):
                        try:
                            a[i]=int(a[i])
                        except ValueError:
                            pass
                    res.append(a)
                else:
                    res.append(c)
    #print(res)
    return {'codearray':res}


def psfor(scope):
    op = opstack.pop()
    final =opstack.pop()
    incr = opstack.pop()
    init = opstack.pop()

    if(incr>0):
            final+=1
    else:
            final-=1
     
    for i in range(init,final,incr):
        opPush(i)
        interpretSPS(op,scope)

def psif(scope):
    op1=opPop()
    op2=opPop()
    if(isinstance(op2,bool) and op2==True):
        interpretSPS(op1,scope)

def psifelse(scope):
    op1=opPop()
    op2=opPop()
    op3=opPop()
    if(isinstance(op3,bool) and op3==True):
        interpretSPS(op2,scope)
    else:
        interpretSPS(op1,scope)


functions = {'pop':opPop,'dictpush':dictPush,'dictpop':dictPop,'push':opPush,'add':add,'sub':sub,'mul':mul,'eq':eq,'lt':lt,'gt':gt,'exch':exch,'begin':begin,'end':end,'dict':psDict,'def':psDef,'clear':clear,'length':length,'get':get,'search':search,'getinterval':getinterval,'putinterval':putinterval,'dup':dup,'stack':stack,'aload':aload,'astore':astore,'count':count,'copy':copy}
def interpretSPS(code,scope): # code is a code array
    for k,v in code.items():
        for c in v:
            if(isinstance(c,str)):        
                if(c[0]=='/'):
                    opPush(c)
                elif(c[0]=='('): 
                    opPush(c)
                elif(c=='def'):
                    psDef(scope)
                elif(c=='for'):
                    psfor(scope)
                elif(c=='if'):
                    psif(scope)
                elif(c=='ifelse'):
                    psifelse(scope)
                elif(c=="true"):
                    opPush(c)
                elif(c=="false"):
                    opPush(c)
                elif(c in functions.keys()):
                    f=functions[c]   
                    f()
                else:
                    res=lookup(c,scope)
                    #print("res returned ",res)
                    if(isinstance(res,dict)):
                        opPop()
                        if(scope=="dynamic"):
                            dictPush((0,{}))
                        elif(scope=="static"):
                            dictPush((staticLink(c),{}))
                            #print("dictpushed retuened ",dictstack)
                        
                        interpretSPS(res,scope)
                        #dictPop()
                    else:
                        pass
            elif(isinstance(c,dict)):
                opPush(c)
            elif(isinstance(c,int)):
                opPush(c)
            elif(isinstance(c,list)):
                opPush(evaluateArray(c,scope))
            elif(isinstance(c,bool)):
                opPush(c)
            print(dictstack, c)
                
def interpreter(s,scope): # s is a string
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)


#clear opstack ansd dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


def clearBoth():
    opstack[:] = []
    dictstack[:] = []



########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():

    testinput1 = """
    /x 1 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput2 = """
    /x 4 def
    (static_?) dup 7 (x) putinterval /x exch def
    /g { x stack } def
    /f { /x (dynamic_x) def g } def
    f
    """

    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """

    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n -1 1 {pop x mul} for} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput6 = """                
    /out true def           
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """

    testinput7 = """
    /x [1 2 3 4] def
    /A { x aload pop add add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """
    testinput9="""
    /x 5 def
    /f { /x 100 def x } def
    /g { /y 100  def x } def
    /h { /x 200 def /z { x f g } def } def
    h
    z
    """

    testinput10="""
    /x 5 5 add 3 mul  def
    /g { x 40 dup mul 2 exch} def
    /f { /x (abcd) length def g } def
    f
    """

    testinput11="""
        /x [1 2 3 4] def
        /A { x } def
        /C { /x [10 20 30 40 50 60] def A  } def
        /B { /x [6 7 8 9] def /A { x  } def C } def
        B
        """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8, testinput9, testinput10, testinput11]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        print("=============")
        interpreter(input, "static")
        print("=============")
        c=len(dictstack)-1
        for j in (dictstack[::-1]):
            print("---",c,"---0---")
            c=c-1
            print(j[1])
        
        clearBoth()
       
        print("Dynamic")
        print("=============")
        interpreter(input, "dynamic")
        print("==============")
        c=len(dictstack)-1
        for j in (dictstack[::-1]):
            print("---",c,"---0---")
            c=c-1
            print(j[1])
        clearBoth()
        print('\n-----------------------------')

#sspsTests()