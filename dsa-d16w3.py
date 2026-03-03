#     LINKED LIST
'''
liked list is a linear data sturucture where all the nodes were headed through pionters
each linked list is subjected with a node, where node carries the data as well as memory location
types:
1.single linked list
2.doubly linked list
3.circular linked list

node implementation:
class node:
    def __init__(self,data):
         self.data = data

operations:
1.insert from end
2.insert from begin
3.delete from end
4.delete from begin
5.insert from pos
7.insert from pos
8.searching  '''
#write a code to implement insertion in a single linked list INSERT END
'''
print(1,'INSERT END')

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_end(head,value):
    new_node=node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end='->')
        temp=temp.next
    print("Tail")    
head=None
n=int(input("enter nodes:"))
for i in range(n):
    val = int(input("enter value:"))
    head= insert_end(head,val)
print("single linked list:",print_list(head))    '''

#   DELETE END
'''
print(2,'DELETE END')
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_end(head,value):
    new_node=node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head
def delete_end(head):
    if head is None:#if empty
        print("empty")
        return None
    if head.next is None:
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head
def print_list(head):
    temp=head
    while temp:
        print(temp.data,end='->')
        temp=temp.next
    print("Tail")    
head=None
n=int(input("enter nodes:"))
for i in range(n):
    val = int(input("enter value:"))
    head= insert_end(head,val)
print("single linked list before delete:",print_list(head))
head=delete_end(head)
print("single linked list after delete:",print_list(head))    '''

# SEARCHING

print(3,"SEARCHING")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begin(self,value):
        new_node = node(value)   # Create new node
        new_node.next = head  # Point new node to current head
        return new_node
        
def insert_end(head,value):
    new_node=node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    return head

def delete_end(head):
    if head is None:#if empty
        print("empty")
        return None
    if head.next is None:
        return None
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
    return head

def print_list(head):
    temp=head
    while temp:
        print(temp.data,end='->')
        temp=temp.next
    print("Tail")
    
def search(head,key):
    pos=1
    temp=head
    while temp:
        if temp.data==key:
            return pos
        temp=temp.next
        pos+=1
    return -1
head=None
n=int(input("enter nodes:"))
for i in range(n):
    val = int(input("enter value:"))
    head= insert_begin(head,val)
    
key=int(input('enter element tio search:'))
p=search(head,key)

if p!=-1:
    print("element fount at position:",p)
else:
    print("not found")
print("single linked list before delete:",print_list(head))
head=delete_end(head)
print("single linked list after delete:",print_list(head))

'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_begin(head, value):
    new_node = node(value)      # Create new node
    new_node.next = head        # Point new node to current head
    return new_node             # New node becomes new head

def insert_end(head, value):
    new_node = node(value)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

def search(head, key):
    pos = 1
    temp = head
    while temp:
        if temp.data == key:
            return pos
        temp = temp.next
        pos += 1
    return -1

head = None
n = int(input("Enter number of nodes: "))

for i in range(n):
    val = int(input("Enter value: "))
    head = insert_begin(head, val)

key = int(input("Enter element to search: "))
p = search(head, key)

if p != -1:
    print("Element found at position:", p)
else:
    print("Not found")    '''





