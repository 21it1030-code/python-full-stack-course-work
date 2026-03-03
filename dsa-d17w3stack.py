#stack data structure
'''
stack functions:
    insertion-push()
    delete-pop()
    peek()[-1]
    isempty()
    isfull()   '''

#write a code to demonstrate stack operation
'''
print(1)
stack=[]
stack.append(11)
stack.append(22)
stack.append(33)
stack.append(44)
stack.append(55)
stack.append(11)
print("stack:",stack)
delete=stack.pop()
print("stack:",stack)
print("peek:",stack[-5])
print("size of stack:",len(stack))


stack: [11, 22, 33, 44, 55, 11]
stack: [11, 22, 33, 44, 55]
peek: 55
size of stack: 5
'''

#write a code to consider user input for stack
'''
print(2)
stack=[]
size=int(input("enter:"))
for i in range(size):
    value=int(input("enter values:"))
    stack.append(value)
print("stack:",stack)
print("popped element:",stack.pop())
print("stack:",stack)
print(len(stack))


2
enter:5
enter values:2
enter values:66
enter values:89
enter values:-1
enter values:67
stack: [2, 66, 89, -1, 67]
popped element: 67
stack: [2, 66, 89, -1]
'''

#stack using class
'''
print(3)
class stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if len(self.stack)==0:
            return "empty"
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "empty"
        return self.stack[-1]
    def display(self):
        if len(self.stack)==0:
            return "empty"
        return self.stack
s=stack()
s.push(5)
s.push(55)
s.push(555)
s.push(5555)
s.push(55555)
print("stack",s.display())
print("pop",s.pop())
print("peek",s.peek())
print("stack",s.display())
print("pop",s.pop())
print("peek",s.peek())
print("stack",s.display())
print("pop",s.pop())
print("peek",s.peek())
print("stack",s.display())
print("pop",s.pop())
print("peek",s.peek())
print("pop",s.pop())
print("peek",s.peek())



3
stack [5, 55, 555, 5555, 55555]
pop 55555
peek 5555
stack [5, 55, 555, 5555]
pop 5555
peek 555
stack [5, 55, 555]
pop 555
peek 55
stack [5, 55]
pop 55
peek 5
pop 5
peek empty

'''
#code to illustrate stack over-flow
'''
print(4)
class stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
    def is_empty(self):
        return len(self.stack)==0 
    def is_full(self):
        return len(self.stack)==self.size
    def push(self,value):
        if self.is_full():
            print("stack is full")
        else :
            self.stack.append(value)
            print(value,"pushed")
    def pop(self):
        if len(self.stack)==0:
            return "empty"
        return self.stack.pop()        
            
s=stack(4)
s.push(5)
s.push(55)
s.push(555)
s.push(5555)
print(s.is_full())
print("popped:",s.pop())
print(s.is_full())



4
5 pushed
55 pushed
555 pushed
5555 pushed
True
popped: 5555
False

'''

#write a code to reverse a string
'''
print(5)
text=input("enter string:")
stack=[]
for ch in text:
    stack.append(ch)
rev=" "
while stack:
    rev+=stack.pop()
print("reversed string:",rev)



5
enter string:kjdfiodsuhbjv
reversed string:  vjbhusdoifdjk

5
enter stringkdjvks
reversed string:  skvjdk

'''
    


















































