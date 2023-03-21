n, m = map(int, (input().split()))
result = []
for e in range(n):
    result.append(e + 1)
for q in range(m):
    i, j = map(int, input().split())
    tmp = result[i - 1]
    result[i - 1] = result[j - 1]
    result[j - 1] = tmp

# 출력
for i in range(n):
    print(result[i], end=" ")
