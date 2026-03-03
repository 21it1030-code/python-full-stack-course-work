#   random
'''
import random
a=""
for i in range(4):
    a+=str(random.randint(1,9))
print(a)


a=["a","b","c","d","e","f"]
otp=""
for i in range(4):
    otp+=random.choice(a)
print(otp)   '''



#anonymous functions
#lambda

#print((lambda a,b,c,d:a+b+c+d) (10,20,30,40))

'''
a=5
add=lambda a:a*2
print(add(a))  '''

print((lambda a:"even" if a>50 and a<100 else "not") (101))

print((lambda a,b,c:"a" if a>b and a>c else "b" if b>c and b>a else "c")(12,1,71))

#x=list(map(int,input().split()))

a=[2,3,45,6,5,66,78]
print(list(map(lambda a:a if a%2==0 else False,(a))))
print(list(filter(lambda a:a%2==0 ,(a))))
