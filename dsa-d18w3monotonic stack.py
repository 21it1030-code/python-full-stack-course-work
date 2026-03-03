#stacks monotonic
'''
monotonic stack:
    increasing monotonic
    decreasing monotonic
    stock markets
    temperature
    data visualisation
    image processing


ex:
    [4,5,2,10]   true-> pop()   false->push()
    4
    stack=[]
    push[4]
    stack=[4]
    5❤
    push=5
    4>5 ? F push
    stack=[4,5]
    2
    5>2 T pop()
    stack=[4]
    4>2 T pop()
    stack=[]
    push=2
    stack=[2]
    2>10 F -> push(10)
    stack=[2,10]  '''


'''
#write a code to perform monotonic increasing stack and print the range  with-in
print(1)
stack=[]
arr=list(map(int,input("enter  a number:").split()))
for n in arr:
    while stack and stack[-1]>n:
        stack.pop()
    stack.append(n)
print("monitring increasing stocks:",stack)'''

'''
#write a code to perform monotonic decreasing stack and print the range  with-in
print(2)
stack=[]
arr=list(map(int,input("enter  a number:").split()))
for n in arr:
    while stack and stack[-1]<n:
        stack.pop()
    stack.append(n)
print("monitring increasing stocks:",stack)'''

#write a code toprint the next most high=est value in the stack for all the elements in the stack with adjuccent witr each other?(right)
stack=[]
arr=list(map(int,input("enter  a number:").split()))
size=len(arr)
result=[-1]*size
for i in range (size-1,-1,-1):
    while stack and stack[-1]<=arr[i]:
        stack.pop()
    if stack:
        result[i]=stack[-1]
    stack.append(arr[i])
print(result)
