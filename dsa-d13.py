#recurtions
'''# write a code  for even or odd with indirect recursion
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
n=int(input())
print("even:", is_even(n))'''

#natural numbers using head recursion
'''def head(n):
    if n==0:
        return 0
    head(n-1)
    print(n)
n=int(input())
head(n)'''

# sum of numbers using linear recursion
'''
def linear(n):
    if n==0:
        return 0
    return n+linear(n-1)
n=int(input())
print("sum:",linear(n))'''

# fibonacci series number using tree recursion
'''
def tree(n):
    if n<=1:
        return n
    return tree(n-1)+tree(n-2)
n=int(input())
for i in range(n):
    print(tree(i))
#print(tree(n)) '''# for particular index of a fibonacci series of number

#write a code to convert a number to zero by using a nested recursion
def convert(n):
    if n<=0:
        return 0
    return convert(convert(n-1))
n=int(input())
print(convert(n))
