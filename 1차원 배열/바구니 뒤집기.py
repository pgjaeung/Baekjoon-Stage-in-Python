n,m = map(int,input().split())
a = [i+1 for i in range(n)]

for _ in range(m):
    i,j = map(int, input().split())
    a = a[:i-1] + a[i-1:j][::-1] + a[j:]
for i in a:
    print(i, end=' ')