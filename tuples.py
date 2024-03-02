'''mytupe=tuple(["max",23,"boston"])
print(mytupe)

tup=('a',"s",'e','j','a','l')

'''
'''
for i in mytupe:
    print(i,end=" ")

if "max" in mytupe:
    print("\n yes")
else:
    print("no")      '''  

'''print(tup.count('a'))
print(tup.index("s"))
my_list=list(tup)
print(my_list)

tup2=tuple(my_list)
print(tup2)
'''
'''a=(1,2,3,4,5,6,6,7,8,9)

b=a[::-2]
print(b)

my_tup=(1,2,3,4,5)

i1, *i2, i3 = my_tup
print(i1)
print(i3)
print(i2)'''
'''
import timeit
print(timeit.timeit(stmt="[1,2,3]",number=10000))
print(timeit.timeit(stmt="(1,2,3)",number=10000))

'''

#dictionary
#mydict={"name":"jim","age":21,"city":"boston"}
#print(mydict)
'''mydict["lastname"]="snow"
print(mydict)

mydict["lastname"]="snowflake"
print(mydict)

del mydict["age"]
print(mydict)
mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict['name'])'''
'''
try:
    print(mydict["city"])
except:
    print("error")  

    '''

'''for key in mydict.items():
    print(key)

mycopy=mydict
print(mycopy)

#mycopy["email"]="li@.com"
#print(mycopy)
#print(mydict)
cpy=dict(name="mary",age=22,city="goa")

copy=mydict.copy()
print(copy)
mydict.update(cpy)
print(mydict)

tup=(2,3)
mydict={tup:10}
print(mydict)'''

'''myset=set()

myset.add(1)
myset.add(2)
myset.add(3)
for i in myset:
  print(myset)'''

'''even={0,2,4,6,8,}
odd={1,3,5,7,9}
prime={2,3,5,7}
u=odd.union(even)
print(u)
i=prime.intersection(even)
print(i)'''
'''sa={1,2,3,4,5,6}
sb={1,2,5}

print(sa.issuperset(sb))'''
'''diff=sb.difference(sa)
print(diff)'''




#strings

'''st1='hello world'
print(st1.replace("r","universe"))'''




'''st='how,are,you,doing'
list=st.split(",")
new_string=' '.join(list)
print(new_string)
lst=["a"]*8
print(lst)

k=""
for i in lst:
    k+=i
    print(k)

k=" ".join(lst)
print(k)   ''' 
'''
var=8.225453
avr="priti"
my_str=f"the vaariable is {var*2} and {avr}"
print(my_str)'''



#collection Counter,nametuple,orderdict,defaultdict,deque


'''from collections import Counter
a="aaaaabbbbcccccc"
my_counter=Counter(a)
print(my_counter)
print(list(my_counter.elements()))'''


'''
from collections import namedtuple
point=namedtuple('point','x,y')
pt=point(1,-4)
print(pt.x)'''

'''
from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['2']=2
od['3']=3 
print(od)'''

'''from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=2
print(d['a'])'''

'''from collections import deque
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.extendleft([4,5,6,8])
print(d)
d.rotate(-1)
print(d)
'''


#iteratools product,permutations, combinations,groupby,infinate itrators
'''
from itertools import product
a=[1,2]
b=[3]
p=product(a,b, repeat=2)
print(list(p))'''

''''
from itertools import permutations
a=[1,2,3]
pr=permutations(a, 2)
print(list(pr))'''
'''
from itertools import combinations,combinations_with_replacement
a=[1,2,3,4]
c=combinations(a,2)
print(list(c))
cr=combinations_with_replacement(a,2)
print(list(cr))'''


'''from itertools import accumulate
import operator
a=[1,2,3,4]
acc=accumulate(a,func=max)
print(a)
print(list(acc))'''

''''from itertools import groupby

def small(x):
    return x<3
a=[1,2,3,4]
grp=groupby(a, key=small)
for key,value in grp:

    print(key,list(value))
'''


# lambda function
'''a=lambda x: x+10
print(a(5))

nul=lambda x,y:x+y
print(nul(2,7))

p=[(1,2),(13,4),(45,-2),(5,-1)]
ps=sorted(p,key=lambda x:x[0]+ x[1])
print(p)
print(ps)'''


#map(fun,seq)
'''q=[1,2,3,4,5]
b=map(lambda x: x*2, q)
print(list(b))

c=[x*2 for x in q]
print(c)'''

#filter
'''q=[1,2,3,4,5,6]
b=filter(lambda x: x%2==0, q)
print(list(b))

#reduce
from functools import reduce
a=[1,2,3,4,5,6]
produvta=reduce(lambda x,y:x*y,a)
print(produvta)'''


#exception
#rasie
#x=-5
#if x<0:
 #   raise Exception('x should be positive')
#assert (x==0)
'''
try:
    a=5/0
    b=a+1
except Exception as e:
    print(e) 
else:
    print('its fine')     
finally:    
    print('cleaning up')  
'''

'''class ValueToHigh(Exception):
    pass

def test_vlaue(x):
    if x>100:
        raise ValueToHigh('value jyada hai')
    
#test_vlaue(3000)    
try:
    test_vlaue(200)
except ValueToHigh as e:
    print(e)    '''


#logging

'''
import logging
logger=logging.getLogger(__name__)
logger.info('heloo from helper')'''






#json




'''
import json

person={"name":"jhon","age":23,"city":"goa","haschilder":False,"titles":["engineer","programmer"]}
personJSON=json.dumps(person,indent=4,sort_keys=True)
print(personJSON)

#serialization
with open('person.json','w') as file:
    json.dump(person,file,indent=4)

#deserialization
person=json.loads(personJSON)
print(person)    '''
'''

import json
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User('max',22)

def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('objext of type is not json')

from json import JSONEncoder
class Userencoder(JSONEncoder):
    def default(self, o):
          if isinstance(o,User):
            return {'name':o.name,'age':o.age,o.__class__.__name__:True}
          return JSONEncoder.default(self,o)
      


#userJSON=json.dumps(user,default=encode_user)
userJSON=Userencoder().encode(user)   
print(userJSON)'''







#random



#import random
'''a=random.normalvariate(0,1)
print(a)

ml=list("wrwygwdhw")
b=random.shuffle(ml)
print(b)
'''

'''random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(1)
print(random.random())
print(random.randint(1,10))'''

'''
import secrets
a=secrets.randbits(4)
print(a)'''


import numpy as np

a=np.random.rand(3)
print(a)
