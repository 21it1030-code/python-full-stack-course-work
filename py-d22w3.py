#dictionary
'''x=[1,2,3]
d={}
for i in range(len(x)):#range gives index
    d[i]=x[i]
print(d)'''

#frequency
x=["java","bava","oracle","miracle","kjxciosuc"]
d={}
count=0
for i in x:   # x it gives word
    word=len(i)
    if word not in d:
        d[word]=[i]
    else:
        d[word]+=[i]
print(d)        
