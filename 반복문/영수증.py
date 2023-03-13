a = int(input())
b = int(input())
sum=0
for i in range(b):
    tmpa, tmpb=map(int, input().split())
    sum=sum+tmpa*tmpb
print("Yes" if sum== a else "No")