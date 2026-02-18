#CLASS
'''
syntax:
   class class_name:   or    class class_name
       statement1
       statement2
       statement3'''
#a code to access class variebes using class objects
'''
class stu:
    name="kjshdvu"
    branch='it'
    roll= 2
    per=70.0
obj=stu()
print("name:",obj.name)
print("branch:",obj.branch)
print("roll:",obj.roll)
print("per:",obj.per) '''

# CONSTRUCTURE
'''  syntax:
class -----:
    def __init__ -----(attribute,var): '''
'''
class icici():
    def __init__(self,money):
        self.money=money
        print("money added:",money)
cash=int(input('enter:'))
cash=icici(cash)   '''

#write a code 
'''
class number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            num.evens.append(num)
        else:
            num.odds.append(num)
n1=number(11)    
n2=number(122)    
n3=number(33)    
n4=number(44)    
n5=number(55)    
print('even ',number.evens)
print('odd ',number.odds)'''

#list comprehensions samples
'''
square=[]
for x in range(10):
    square.append(x**2)
print(square)
print([x**2 for x in range(10)])
print([x**2 for x in range(10) if x%2==0]) '''

#write a code for string hashing including size
class hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
    def hash_fun(self,key):
        return sum(ord(c) for c in key) % self.size
    def insert(self,key):
        index=self.hash_fun(key)
        self.table[index].append(key)
    def display(self):
        for i in range(self.size):
            print(f"index {i} -> {self.table}")
size=int(input('enter size:'))
ht=hashtable(size)
n=int(input('enter itemes:'))
for _ in range(n):
    s=input('enter string:')
    ht.insert(s)
ht.display()    
