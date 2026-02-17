#write a code to find  factorial of a number using recursion
'''
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input())
for i in range(n):
    print(fact(i))
print(fact(n))'''

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

#BACK TRACKING
'''
BACK TRACKING IS recursion + undo
a->b
a->c'''

#write a code to back track all the permutations of a string
'''
1.choose a character
2.recur for remaining chars
3.undo choice(back track)'''
def comb(s,result=" "):
    if len(s)==0:
        print(result)
        return
    for i in range(len(s)):
        ch=s[i]
        remain=s[:i]+s[i+1:]
        comb(remain,result+ch)
s=input("string:")
comb(s)
