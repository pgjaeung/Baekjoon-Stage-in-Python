a = list(input())
b=[]
sum=0
for i in range(len(a)):
    if(a[i]==' '):
        b.apppend(1)
    elif(a[i] in 'ABC'):
        b.append(2)
    elif(a[i] in 'DEF'):
        b.append(3)
    elif(a[i] in 'GHI'):
        b.append(4)
    elif(a[i] in 'JKL'):
        b.append(5)
    elif(a[i] in 'MNO'):
        b.append(6)
    elif(a[i] in 'PQRS'):
        b.append(7)
    elif(a[i] in 'TUV'):
        b.append(8)
    elif(a[i] in 'WXYZ'):
        b.append(9)
    else:
        b.append(0)

for i in range(len(b)):
    sum=sum+b[i]+1
print(sum)