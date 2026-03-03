#print greastest of three by only use 2 if statements
'''
print(1)
a=1
b=24
c=3
great=a
if b>a:
    great=b
if c>b:
    great=c
print(great)    '''

#print vowels and consonents in a word
'''
print(2)
x="python"
c=""
v=""
for i in x:
    if i in "aeiou":
        v+=i
    else:
        c+=i
print(v)
print(c)   '''

#prnint
'''
print(3)
x="python"
c=""
v=""
for i in x:
    if i not in "aeiou":
        c+=i
    print(c)  '''


#
'''
print(4)
x="java"
for i in range(len(x)):
    print(x[i])  '''

'''
print(5)
x="java"
#print(x[::-1])
rev=' '
for i in x:
    rev=i+rev
print(rev)  '''


#list comprehenssion
'''
xal=['kagj','kshgwi','hgwi']
aa=[name.title() for name in xal]
print(aa)'''

#
'''
x=['kagj','kshgwi','hgwi']
res=''
for i in x:
    res+=i[0].upper()+i[1:]+","
print(res) '''
    
#capital of every first letter
'''
arr=["kagj","kshgwi","hgwi"]
for i in range(len(arr)):
    arr[i]=arr[i][0].upper()+arr[i][1:]
print(arr)

#concatinate every word in list with capital of every first letter

arr=["kagj","kshgwi","hgwi"]
for i in range(len(arr)):
    arr[i]+=arr[i][0].upper()+arr[i][1:]
print(arr)



['Kagj', 'Kshgwi', 'Hgwi']
['kagjKagj', 'kshgwiKshgwi', 'hgwiHgwi']
'''


#
x="jai balayya"
print(x.replace("a","@"))
print(x.replace(" ",""))

print(x[0],x[-1])
print(x[-1])
