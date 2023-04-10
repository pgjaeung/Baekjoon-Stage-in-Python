import sys
sys.setrecursionlimit(10 ** 6)
tree=[]
#****************************
def postorder(first,end):
    if first > end:
        return
    mid = end + 1

    for i in range(first+1, end+1):
        if tree[first] < tree[i]:
            mid = i
            break
    postorder(first+1, mid-1)
    postorder(mid,end)
    print(tree[first])
#****************************
# 리스트에 입력
while True:
    try:
        a = int(input())
        tree.append(a)
    except:
        break

postorder(0,len(tree)-1)