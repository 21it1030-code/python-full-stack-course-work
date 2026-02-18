n=int(input())                #print mirror of right angle triangle capital
for i in range(n,0,-1):
    for j in range(i):
        print(chr(97+j),end='')
    print()


'''
15
abcdefghijklmno
abcdefghijklmn
abcdefghijklm
abcdefghijkl
abcdefghijk
abcdefghij
abcdefghi
abcdefgh
abcdefg
abcdef
abcde
abcd
abc
ab
a   '''
