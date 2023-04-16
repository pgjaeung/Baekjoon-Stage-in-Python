import sys
sys.setrecursionlimit(10**6)

def star(n):
    if n == 1:
        return '*'
    stars=star(n//3)
    l=[]


    for i in stars:
       l.append(i*3)
    for i in stars:
        l.append(i+' '*(n//3)+i)
    for i in stars:
        l.append(i*3)

a = int(input())
print('\n'.join(star(a)))