#   DC- DIVIDE AND CONQUER

# write a code to print a d-2 matrix in a spiral pattern clock wise direction using divide and conquer approach
'''
print(1)
n=int(input("enter size:"))
matrix=[[0]*n for _ in range(n)]
#print(matrix)
num=1
top=0
bottom=n-1
left=0
right=n-1
while top<=bottom and left<=right:
    for i in range(left, right+1):
        matrix[top][i]=num
        num+=1
    top+=1
    for i in range(top, bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1
    for i in range(right, left-1, -1):
        matrix[bottom][i]=num
        num+=1
    bottom-=1
    for i in range(bottom, top-1, -1):
        matrix[i][left]=num
        num+=1
    left+=1
for row in matrix:
    print(*row)
    
o/p:

1
enter size:5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

'''

# write a code to print a 2-d matrix into spiral linear
print(2)
r=int(input("enter row size:"))
c=int(input("enter col size:"))
matrix=[]
print("enter elements:")
for i in range(r):
    row=list(map(int,input().split()))
    matrix.append(row)
top=0
bottom=r-1
left=0
right=c-1
while top<=bottom and left<=right:
    for i in range(left, right+1):
        print(matrix[top][i],end=" ")
    top+=1
    for i in range(top, bottom+1):
        print(matrix[i][right],end=" ")
    right-=1
    for i in range(right, left-1, -1):
        print(matrix[bottom][i],end=" ")
    bottom-=1
    for i in range(bottom, top-1, -1):
        print(matrix[i][left],end=" ")
    left+=1
'''
o/p:
    
2
enter row size:3
enter col size:3
enter elements:
1 2 3
4 5 6
7 8 9
1 2 3 6 9 8 7 4 5

2
enter row size:4
enter col size:4
enter elements:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

'''  
#practice diagonal
