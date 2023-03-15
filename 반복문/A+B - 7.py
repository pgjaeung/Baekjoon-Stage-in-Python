import sys

inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #".strip(),i+1,": ".lstrip(), a+b,sep="")