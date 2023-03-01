import sys

n, m = map(int, sys.stdin.readline().split())

num_lst = list(map(int, sys.stdin.readline().split()))

sum_lst = [0] * (n+1)

for _ in range(1, n+1):
    sum_lst[_] += sum_lst[_-1] + num_lst[_-1]

for i in range(m):
    min_val, max_val = map(int, sys.stdin.readline().split())
    
    print(sum_lst[max_val] - sum_lst[min_val-1])