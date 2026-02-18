n=int(input())    
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")        #lower
    for j in range(i):
        print(chr(97+j),end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")        #lower
    for j in range(i):
        print(chr(96+i),end=" ")
    print()

'''
9
                a 
              a b 
            a b c 
          a b c d 
        a b c d e 
      a b c d e f 
    a b c d e f g 
  a b c d e f g h 
a b c d e f g h i 
                a 
              b b 
            c c c 
          d d d d 
        e e e e e 
      f f f f f f 
    g g g g g g g 
  h h h h h h h h 
i i i i i i i i i
'''
