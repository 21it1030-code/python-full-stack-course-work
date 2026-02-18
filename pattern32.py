n=int(input())
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")    #capital
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

for i in range(0,n+1):
    for s in range(n-i):
        print(" ",end=" ")    #capital
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

'''
9
                A 
              A B 
            A B C 
          A B C D 
        A B C D E 
      A B C D E F 
    A B C D E F G 
  A B C D E F G H 
A B C D E F G H I 
                  
                A 
              B B 
            C C C 
          D D D D 
        E E E E E 
      F F F F F F 
    G G G G G G G 
  H H H H H H H H 
I I I I I I I I I
'''
