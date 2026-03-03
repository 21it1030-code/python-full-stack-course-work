#PREFIX-SUM
#precomputing cumulatiive sums of sn array / data structure to answer range
'''
find sum frim index 1 to R
prefix[i]=arr[0]+arr[1]+arr[2]+........+arr[n]
arr=[2,4,6,8,10]
index  arr  prefix
  0     2     2
  1     4     6
  2     6     12
  3     8     20
  4     10    30    '''
#   arr=[[0] for i in range len(arr)-1]
#write a code to implementaa prefix sum on an list f eliments and compute the range
'''
summation
arr=[2,4,6,8,10]
prefix=[2,6,12,20,30]
range 1=1
range R=3
sum of prefix ranhe:18   '''
#
'''
print(1)
n=int(input("emter elements:"))
arr=list(map(int,input("elements:").split()))
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
print("prefix array:",prefix)
l=int(input("enter l index:"))
r=int(input("enter r index:"))
if l==0:
      print("sum=",prefix(r))
else:
    print("sum:",prefix[r]-prefix[l-1])  '''

#multiple query range summation
'''    
arr=[5,2,8,1,3,7]
prefix_sum=[5,7,15,16,19,26]   '''
print(2)
n=int(input("emter elements:"))
arr=list(map(int,input("elements:").split()))
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
q=int(input("enter num of queries:"))
for _ in range(q):
    l,r=map(int,input("enter l and r:").split())
    if l==0:
        print("sum=",prefix[r])
    else:
        print("sum:",prefix[r]-prefix[l-1])

      
