n=int(input())                #print mirror of right angle triangle j
for i in range(n+1,0,-1):
    for j in range(i):
        print(j,end='')
    print()


'''
9
0123456789
012345678
01234567
0123456
012345
01234
0123
012
01
0  '''
