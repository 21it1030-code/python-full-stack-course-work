n=int(input())                #print lower letters
for i in range(1,n+1):
    for j in range(i):
        print(chr(97+j),end='')
    print()
for i in range(n-1,-1,-1):
    for j in range(i):
        print(chr(97+j),end='')
    print()


'''
26
a
ab
abc
abcd
abcde
abcdef
abcdefg
abcdefgh
abcdefghi
abcdefghij
abcdefghijk
abcdefghijkl
abcdefghijklm
abcdefghijklmn
abcdefghijklmno
abcdefghijklmnop
abcdefghijklmnopq
abcdefghijklmnopqr
abcdefghijklmnopqrs
abcdefghijklmnopqrst
abcdefghijklmnopqrstu
abcdefghijklmnopqrstuv
abcdefghijklmnopqrstuvw
abcdefghijklmnopqrstuvwx
abcdefghijklmnopqrstuvwxy
abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxy
abcdefghijklmnopqrstuvwx
abcdefghijklmnopqrstuvw
abcdefghijklmnopqrstuv
abcdefghijklmnopqrstu
abcdefghijklmnopqrst
abcdefghijklmnopqrs
abcdefghijklmnopqr
abcdefghijklmnopq
abcdefghijklmnop
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
