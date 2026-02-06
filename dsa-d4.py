'''
name='prakash'
num='123'
char='@#'
print(name)
print(num)
print(char)
#access
print(name[3])
print(name[-5])
#slicing
print(name[1:4])
print(name[2:])
s = 'mississipi'
print(s[4:8])
print(len(s))
'''
'''
#vowels and consents in user defined strimg
word=input()
v=0
c=0
for i in word:
    if i.isalpha():
        if i.lower() in 'aeiou':
            v+=1
        else:
            c+=1
print(v)
print(c)
'''

'''
#reverse the string using traversal method
w=input()
rw=""
for i in w:
    rw=i+rw
print(rw)
'''
'''
#proove 2 strings are tomriddle anagram each other
s1=input().replace(" "," ")         
s2=input().replace(" "," ")
s1=s1.lower()
s2=s2.lower()
if sorted(s1)==sorted(s2):
    print(s1,"is anagram with",s2)
else:
    print(s1,"is not naagram with",s2)
'''
'''
# ascii values
for i in range(256):
    #print(f"ASCII value of {i} is {chr(i)}")
    print(chr(i),end=" ")
'''
'''
# print patterns
s='codegnan'
for i in range(1,len(s)+1):
    print(" ".join(s[ :i]))
for i in range(len(s) -1,0,-1):
    print(" ".join(s[ :i]))
'''

























    
