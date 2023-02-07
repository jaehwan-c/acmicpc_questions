import sys
from collections import Counter

n = int(input())
lst = list()

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
    
print(round(sum(lst)/n))
print(lst[(n-1)//2])
if n != 1:
    if Counter(lst).most_common()[0][1] == Counter(lst).most_common()[1][1]:
        print(Counter(lst).most_common()[1][0])
    else:
        print(Counter(lst).most_common()[0][0])
else:
    print(Counter(lst).most_common()[0][0])
print(lst[-1] - lst[0])