n=int(input())
sum = 0
result = 0

n_list=list(map(int,input().split()))

for i in range(len(n_list)):
    sum = sum+ n_list[i]
result = sum/n/max(n_list)*100
print(result)