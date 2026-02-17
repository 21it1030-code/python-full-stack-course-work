'''#patterns 1
n=8
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()    '''    

'''
#pattern 2
n=11
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
            print("*",end='')
        else:
            print(" ",end='')
    print()        
'''
'''
#pattern 3
n=11
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()'''

'''
#pattern 4
n=11
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or (i+j)==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print() '''   

'''
#pattern 5
n=11
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
print("butterfly")
'''
'''
#pattern 6
n=11                 #input=odd/even
for i in range(n):
    for j in range(n):
        if i==j or (i+j)==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()#print X
'''

'''
#pattern 7
n=11                # input=odd/even
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end='')
        else:
            print(' ',end='')
    print()     #print  +
'''
'''
#pattern 8
n=9                # input=odd     #amazon
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or (i+j)==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()
'''
'''
#pattern 9
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if j==0 or i==j or i==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()

#pattern 10
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i+j)==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()

#pattern 11
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if (i+j)==n-1 or j==n-1 or i==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()'''

'''
#pattern 12
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if j==0 or (i+j)==n-1 or i==0:
            print("*",end='')
        else:
            print(' ',end='')
    print()
'''
'''
#pattern 13
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (i+j)==n-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()    #print Z
'''
'''
#pattern 14
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1//2:
            print("*",end='')
        else:
            print(' ',end='')
    print()    #print F
'''

'''
#pattern 15
n=9                # input=odd     
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (i==n//2 and j<4) or (j==4 and i<n//2 and i!=0):
            print("*",end='')
        else:
            print(' ',end='')
    print()
'''
'''
#lksfjnopeqifnpqkcnopifw'odkcn;ou'[ohvbvklmc[ubc    day - 08 
# right angled triangle patter of stars
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

'''
for i in range(0,5):
    for j in range(i):
        print(chr(65+j),end=" ")
    print("*")
for i in range(5,-1,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print("*")'''


'''
n=int(input())             #print capital letters
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end='')   #right angle triangle
    print()
for i in range(n-1,-1,-1):
    for j in range(i):
        print(chr(65+j),end='')
    print()'''

'''
n=int(input())                #print lower letters
for i in range(1,n+1):
    for j in range(i):
        print(chr(97+j),end='')
    print()
for i in range(n-1,-1,-1):
    for j in range(i):
        print(chr(97+j),end='')
    print()'''

'''
n=int(input())                #print mirror of right angle triangle lower 
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end='')
    print()

n=int(input())                #print mirror of right angle triangle capital
for i in range(n,0,-1):
    for j in range(i):
        print(chr(97+j),end='')
    print()

n=int(input())                #print mirror of right angle triangle i
for i in range(n,0,-1):
    for j in range(i):
        print(i,end='')
    print()

n=int(input())                #print mirror of right angle triangle j
for i in range(n,0,-1):
    for j in range(i):
        print(j,end='')
    print()

n=int(input())                #print mirror of right angle triangle "*"
for i in range(n,0,-1):
    for j in range(i):
        print("*",end='')
    print()

n=int(input())                #print mirror of right angle triangle
for i in range(n,0,-1):
    for j in range(i):
        print(chr(97+j),end='')
    print()'''


'''
# right alligned right angled triangle
n=int(input()) 
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")   # j
    for j in range(i):
        print(j,end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")   # i
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")    #capital
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")        #lower
    for j in range(i):
        print(chr(97+j),end=" ")
    print()'''
'''
n=int(input())
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")        #lower
    for j in range(i):
        print(chr(97+j),end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print(chr(97+j),end=' ')
    print()'''

# jkbci9douwlwncou lkiuikmqhdkmdqdul    ,   ,mdowud,    qmd kjqjhdoh sou day 13






































    
