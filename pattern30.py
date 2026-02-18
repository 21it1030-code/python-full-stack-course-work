n=int(input()) 
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")   # j
    for j in range(i):
        print(j,end=" ")
    print()


'''
10
                  0 
                0 1 
              0 1 2 
            0 1 2 3 
          0 1 2 3 4 
        0 1 2 3 4 5 
      0 1 2 3 4 5 6 
    0 1 2 3 4 5 6 7 
  0 1 2 3 4 5 6 7 8 
0 1 2 3 4 5 6 7 8 9
'''
