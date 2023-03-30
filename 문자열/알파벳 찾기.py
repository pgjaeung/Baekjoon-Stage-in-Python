a=[chr(i) for i in range(97,123)]
b=list(input())
for i in range(len(a)):
    if a[i] in b :
        print(b.index(a[i]),end=" ")
    else:
        print("-1",end=" ")
