#    SETS
'''
x={0}
print(type(x))
x=set()
print(type(x))

s={1,2,3,4,5}
print(s)
s.add(5)
s.add(9)

#upadte
s.update([6,7,8])
s.update(("a","b","c"))
print(s)
s.update(("xyz"))
print(s)
s.remove("x")
s.discard("k")

n=s.copy()
print(n)
s.clear()

print(s)'''

#arithmatic operations
'''
prabhas={"sndhya","yunus","kowshik","sampatgh","akhil","arvind","prakash"}
kajal={"balaji","vennela","diya","akhil","arvind","prakash"}
print(prabhas|kajal)
print(prabhas.union(kajal))
print()
print(prabhas.intersection(kajal))
print(prabhas&kajal)
print()
print(prabhas.difference(kajal))
print(prabhas-kajal)
print()
print(kajal-prabhas)
print()
print(prabhas.symmetric_difference(kajal))
print(kajal^prabhas)
print()
print(prabhas.issubset(kajal))
print(kajal.issubset(prabhas))
print(prabhas<=kajal)
print()
print(prabhas.issuperset(kajal))
print(kajal.issuperset(prabhas))
print(prabhas>=kajal)
print()
print(prabhas.isdisjoint(kajal))

count = 0
for element in kajal:
    count += 1
print(count) '''

#
x={1,2,3}
y={3,4,5,6,1,2}
print(x.isdisjoint(y))
print(x>=y)
print(y>=x)
print(x<=y)
print(y<=x)

