import sys

n = int(input())
lst = list()

for i in range(n):
    lst.append(tuple(map(str, sys.stdin.readline().split())))

lst = sorted(lst, key=lambda x: int(x[0]))

for i in range(n):
    print(lst[i][0], lst[i][1])