import sys

n = int(input())
lst = list()

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))
    
lst.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
    print(lst[i][0], lst[i][1])