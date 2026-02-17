#  WHILE LOOP USING TABLE
'''
print(1)
n=int(input("enter number:"))
i=1
while(i<=10):
    if(i!=5):
        print(n,"*",i,"=",i*n)
        i+=1
    else:
        break   '''

#patterns using while loop
'''
print(2)
i=1
while(i<=3):
    j=1
    while(j<=i):
        print("*",end=' ')
        j+=1
    print()    
    i+=1    '''

#    INDEXING
'''
print(3)
x="prakash"
print(x[2])  #we have out of range erros
print(x[-2])
print(x[5])
print(x[-5])'''   

#SLICING
x="prakash"
print(x[0:7:1])
print(x[-1:])
print(x[5:6])      #wedo not have out of range errors
print(x[-5:-1])
