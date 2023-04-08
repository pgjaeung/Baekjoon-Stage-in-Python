ch = [1, 1, 2, 2, 2, 8]
p= list(map(int, input().split()))
res = []
for i in range(len(ch)):
    res.append(ch[i]-p[i])

for i in range(len(res)):
    print(res[i],end=" ")
