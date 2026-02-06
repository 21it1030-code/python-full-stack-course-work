#advance ds arrays
'''
1. brute force
2. naive math approach
3.one-pass approach
4.hashing approach / dictionary approach
5.space approach / auxillary array approach
6.in-place modification approach
'''
'''
#remove repeated elements in an array without its original place value    -> brute force approach
arr=list(map(int,input().split()))
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)
'''
'''
#missing number in a series of an array -> naive math
arr=list(map(int,input().split()))
n=len(arr)+1
e_sum=n*(n+1)//2
arr_sum=sum(arr)
print(e_sum-arr_sum)
'''
'''
#dictionary / hashing apporach
person={
    "name":"lpk",
    "no":31,
    "city":"vja"
}
print(person)
'''
'''
#repeated values in an array
arr=list(map(int,input().split()))
fre={}
for num in arr:
    fre[num]=fre.get(num,0)+1
for k,v,in fre.items():
    print(k,"->",v)
'''
