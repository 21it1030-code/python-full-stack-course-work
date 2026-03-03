#comparator thinking
'''
list=[1,2,3,4,5]
even=2,4
odd=1,3,5

funcs:
    sorting
    searching
    evaluationary


lambda
l c-> list comprehensions   '''
'''
# write a code using lambda function
print("program no:1")
add= lambda a,b : a+b
print(add(2,3))

#square
add= lambda a : a**2
print(add(5))

#check even or odd
check= lambda x : "even" if x%2==0 else "odd"
print(check(2))
print(check(3))

#
from functools import reduce
nums=[2,3,4,5,6,7,8,9,10]
res=list(map(lambda x:x**2,nums))
print(res)
res=list(map(lambda x:x**3,nums))
print(res)
print(list(filter(lambda x:x%2==0,nums)))
print(reduce(lambda a,b:a+b,nums))
'''

#write a code to segregate a l;ist of numberd to even and odd with in a list without disturbing the pattern of list
'''
input=[1,2,3,4,5]
output=[2,4,1,3,5]
arr=list(map(int,input("enter:").split()))
arr.sort(key=lambda x:(x%2,x))
print(arr)  '''


#LIST COMPREHENSIONS
'''
SYNTAX:
    [ expressions for item in iterable if conditions]  '''

#write a code using list comprehension
'''
nums=[1,2,3,4,5,6]
print([i**2 for i in nums])
print("enen numbers:",[i for i in range(1,11) if i%2==0])
print("enen numbers:",[i for i in range(1,11) if i%2!=0])
print(["even" if i%2==0 else "odd" for i in range(1,11)])  '''

#NESTED LIST COMPREHENSIONS
'''
input=[[1,2,3],
       [4,5,6],
       [7,8,9]]

output=[1,2,3,4,5,6,7,8,9]
'''
#write a code to convert multi diemensional data into single diemensional data
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print("flat:",[num for row in matrix for num in row])

for row in matrix:
    for num in row:
        print([num],end=" ")
