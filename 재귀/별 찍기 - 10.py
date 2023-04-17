import sys
sys.setrecursionlimit(10 ** 6)

def star(len):
    if len == 1:
        return '*'
    stars = star(len//3)
    l = []

    for first in stars:
        l.append(first*3)
    for second in stars:
        l.append(second+' '*(len//3)+second)
    for third in stars:
        l.append(third*3)
    return l

n = int(input())

print('\n'.join(star(n)))