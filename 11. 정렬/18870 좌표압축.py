import sys

n = int(input())

lst = list(map(int, sys.stdin.readline().split()))
sorted_lst = sorted(list(set(lst)))

dict_lst = {sorted_lst[i]: i for i in range(len(sorted_lst))}

for i in lst:
    print(dict_lst[i], end = " ")