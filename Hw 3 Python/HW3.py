# CptS 355 - Fall 2020 - Assignment 3
# Adit Jain

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1-a) getNumCases - 10%

def getNumCases(data,counties,months):
    count=0
    for x1,y1 in data.items():
        for i in range(0,len(counties)):
            if(x1==counties[i]):
               for x2,y2 in y1.items():
                   for j in range(0,len(months)):
                       if(x2==months[j]):
                           count=count+y2
                        
    #print(count)
    return count


## problem 1-b) getMonthlyCases - 15%


def getMonthlyCases(data):
    d={}
    for k1,v1 in data.items():
        for k2,v2 in v1.items():
            if k2 in d:
                t=d[k2]
            else:
                t={}
            t[k1] = v2
            d[k2] = t

    #print(d)
    return d



CDCdata = { 'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},
            'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266}, 
            'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811}, 
            'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751}, 
            'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }


from functools import reduce
## problem 1-c) mostCases - 15%

def helper(x,d):
    a=sum(d[1].values())
    #print(x,a)
    return (x,a)
    
def mostCases(data):
   data=getMonthlyCases(data)
   d1=data.items()
   #print(d1)
   a=max(list(map(helper,data.keys(), d1)),key = lambda x :x[1])
   #print (a)
   return (a)

## problem 2a) searchDicts(L,k) - 5%

def searchDicts(L,k): 
    L.reverse()
    #print(L)
    for i in range(0,len(L)):
        for x1,y1 in L[i].items():
            if(x1==k):
                print(y1)
                return y1
    return 'None'

## problem 2b) searchDicts2(L,k) - 10%

def searchDicts2(L,k):
    if not L:
        return None
    val=L[-1][0]
    #print("val is ",val)
    i=val+1-len(L)

    for a,b in L[::-1]:   
        for x1,y1 in b.items():
            if(x1==k):
                print(y1)
                return y1
        return searchDicts2(L[:i],k)


## problem 3 - adduptoZero - 10%
from itertools import combinations
def adduptoZero(L,n):
    x=list(combinations(L,n))
    #print(x)
    a=[]
    for i in range(0,len(x)):
        if (sum(x[i]) == 0):
            a.append(list(x[i]))
    print(a)
    return a

## problem 4 - getLongest - 10%

def getLongest(L):
    if isinstance (L,str):
        return L
    else:
        return (max([getLongest(x) for x in L]))
        #for x in L:
        #    return (max(getLongest([x])))

print (getLongest(['1',['22',['333',['4444','55555',['666666']],'7777777'],'4444'],'22']))
print(getLongest([['cat',['dog','horse'],['bird',['bunny','fish']]]]))
print(getLongest(['222',[['44444',[['555555555555555'],'3333333'],'1111111']]]))



## problem 5 - apply2nextN - 20% 

class apply2nextN (): 
    def __init__(self,op,n,L):
        self.op=op
        self.n=n
        self.L=L
       
    def __iter__(self):
        return self
        
    def __next__(self):
        self.j=0
        self.res=0
        self.str1=""
        if self.L is None:
            raise StopIteration
        else:
            try:
                for self.i in self.L:
                    self.j+=1
                    self.res=self.op (self.res,self.i)
                    if(self.j%self.n==0):
                        break
                if((self.res==0)):
                    raise StopIteration
            except TypeError:
                for self.i in self.L:
                    self.str1 = self.op(self.str1,self.i)
                    print(self.j)
                    self.j+=1
                    
                    if(self.j%self.n==0):
                        break
                if((self.str1=="")):
                    raise StopIteration
                return self.str1
            
            return self.res


"""iSequence = apply2nextN(lambda a,b:a+b, 3, iter(range(1,7)))
print(iSequence.__next__())
print(iSequence.__next__())
print(iSequence.__next__())
print(iSequence.__next__())

strIter =iter('aaaabbbbccccddddeeeeffffgggghhhhjjjjkkkkllllmmmm')
iSequence = apply2nextN(lambda a,b:a+b, 4, strIter)
print(iSequence.__next__()) # returns 'aaaa'
print(iSequence.__next__()) # returns 'bbbb'
print(iSequence.__next__()) # returns 'cccc'

iSequence2 = apply2nextN(lambda  a,b: a-b, 4, iter(range(1,10)))
print(iSequence2.__next__())
print(iSequence2.__next__())
print(iSequence2.__next__())

iSequence2 = apply2nextN(lambda  a,b: (a-b)*2, 4, iter(range(1,15)))
print(iSequence2.__next__())
print(iSequence2.__next__())
print(iSequence2.__next__())
print(iSequence2.__next__())"""
