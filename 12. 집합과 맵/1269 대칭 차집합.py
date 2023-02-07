import sys

n, m = map(int, sys.stdin.readline().split())

lst_n = set(map(int, sys.stdin.readline().split()))
    
lst_m = set(map(int, sys.stdin.readline().split()))

print(len(lst_n ^ lst_m))