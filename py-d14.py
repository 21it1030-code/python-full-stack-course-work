'''
print(1)
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()    
'''
'''
print(2)        
for i in range(5,0,-1):
    for j in range(1,6,1):
        print("*",end=" ")
    print() 
'''
'''
print(3)        
for i in range(0,4):
    for j in range(i):
        print("*",end=" ")
    print("*")
for i in range(0,4):
    for j in range(i):
        print("*",end=" ")
    print("*")    
for i in range(4,-1,-1):
    for j in range(i):
        print("*",end=" ")
    print("*")
'''

'''
#print(4)

n=int(input())                #print mirror of right angle triangle
for i in range(n,0,-1):
    for j in range(i):
        print("*",end='')
    print(" ")
'''

print(5)
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
