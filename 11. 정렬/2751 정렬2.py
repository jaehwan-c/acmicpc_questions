import sys

n = int(input())
lst = list()

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst)

for i in lst:
    print(i)