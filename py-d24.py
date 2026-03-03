# LAMBDA
'''
x=["python","java","code","gnan"]
print(list(map(lambda x:x[0].upper(),x)))
print(list(map(lambda x:x[0].upper()+x[1:len(x)-1] + x[-1].upper(),x)))
print(list(map(lambda x: len(x),x)))
print(list(map(lambda x:x if len(x)>4 else "False",x)))
print(list(map(lambda x:x if "a" in x else "False",x)))
print(list(map(lambda x:x if "a" not in x else "False",x)))
'''


# FILTER
'''
x=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,x)))
print(list(filter(lambda x:x%2!=0,x)))
print(list(filter(lambda x:x>4,x)))
'''

'''
a="apple8172345", "banana01827", "avocado", "cherry", "apricot32859072","akhil","prakashlam1324@gmail.com","abc123"
print(list(filter(lambda a:a.startswith("a"),a)))
print(list(filter(lambda a:a.endswith("@gmail.com"),a)))
b="sdfjhg12084714"
print("".join(list(filter(lambda b: b.isalpha(),b))))
'''


# REDUCE() function

a=[1,2,3,4,5]
from functools import reduce
print(reduce(lambda a,b:a+b,a))
print(reduce(lambda a,b:a-b,a))
print(reduce(lambda a,b:a*b,a))
print(reduce(lambda a,b:a/b,a))

print(all(n%2==0 for n in a))
print(any(n%2==0 for n in a))
print(any(n>2 for n in a))
