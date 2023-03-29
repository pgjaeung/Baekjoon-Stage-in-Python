
n = int(input())
count = 2 ** n -1
print(count)
m=[]
#**********************
def hanoi(n,a,b,c):
    if n ==1:
        m.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        m.append([a,c])
        hanoi(n-1,b,a,c)
hanoi(n,1,2,3)
#**********************

for i in range(len(m)):
    print(" ".join(map(str, m[i])))