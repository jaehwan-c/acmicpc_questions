import sys
from collections import Counter

n = int(input())
checklst = sorted(list(map(int, sys.stdin.readline().split())))
        
m = int(input())
datalst = list(map(int, sys.stdin.readline().split()))

cnt = Counter(checklst)

for i in datalst:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0, end=" ")