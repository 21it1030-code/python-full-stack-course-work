# LIST/ARRAY METHODS
'''a=[1,2,3,4]
print(a)
#append
a.append(5)
print(a)
#a.append([5,6,7])
#print(a)
a.extend([8,9,10])
print(a)
a.extend({20,30})
print(a)
a.insert(2,[200,300])
print(a)
a.pop()
print(a)
print(a.pop(2))
print(a)
a.remove(1)
print(a)
b=a.copy()
print(b)
print(id(a))
print(id(b))
a.clear()
print(a)
print(b)
'''


#sort
'''
a=[1,2,3,4,5,6]
a.sort()
print(a)
print(id(a))
b=sorted(a,reverse=True)
print(b)
print(id(b)) '''

#  bulit in methods
'''
a=[1,2,3,4,5,6,2]
print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(a.count(2))'''


# nested list
'''
a=[2,[4,[3, 4 ,5],6],4,["lpk"]]
print(a.index(["lpk"]))
print(a)
print(a[1])
print(a[1][1])
print(a[1][1][1])  '''


#              TUPLE
'''
t=(1,2,True,1,1,1)
print(t)
print(t[-4])
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(t.count(1))'''

#
'''l=[]
for i in range(2,101):
    if i%2==0:
        l.append(i)
print(l)        
#print("enen numbers:",[i for i in range(1,100) if i%2==0])
a=["lpk",":sam","sai","ram"]
for i in range(len(a),0,-1):
    print()'''

'''
a=["a","b","c","d"]
for i in range(len(a)):
    if i%2==0:
        a[i]=a[i].upper()
    else:
        a[i]=a[i].lower()
print("".join(a))  '''  

#print("enen numbers:",[i for i in range(1,100) if i%2==0])
'''
l=[]
for i in range(101):
    prime=True
    if i<=1:
        continue
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        l.append(i)
print(l)        '''

a = ["prakash", "apple", "sdkjfghdsi", "ksjdfheiw"]

for word in a:
    result = word[0].upper() + word[1:-1] + word[-1].upper()
    print(result)


