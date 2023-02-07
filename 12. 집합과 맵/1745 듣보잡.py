import sys

n, m = map(int, sys.stdin.readline().split())
lst_n = list()
lst_m = list()

for i in range(n):
    lst_n.append(sys.stdin.readline().strip())
    
for i in range(m):
    lst_m.append(sys.stdin.readline().strip())

lst = sorted(list(set(set(lst_n) & set(lst_m))))

print(len(lst))
for i in lst:
    print(i)