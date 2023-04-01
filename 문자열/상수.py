a,b=map(str,input().split())
if(int(''.join(reversed(a)))>int(''.join(reversed(b)))):
    print(''.join(reversed(a)))
else:
    print(''.join(reversed(b)))