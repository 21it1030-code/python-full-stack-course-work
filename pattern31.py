n=int(input()) 
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")   # i
    for j in range(i):
        print(i,end=" ")
    print()


'''
9
                1 
              2 2 
            3 3 3 
          4 4 4 4 
        5 5 5 5 5 
      6 6 6 6 6 6 
    7 7 7 7 7 7 7 
  8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9
'''
