import sys

n, m = map(int, sys.stdin.readline().split())
len_lst = [int(sys.stdin.readline()) for i in range(n)]
len_lst.sort()

def bin_search(m, low, high):
    if low > high:
        return high

    mid = (low + high) // 2
    len = sum([x // mid for x in len_lst])
    
    if len >= m:
        return bin_search(m, mid+1, high)
    else:
        return bin_search(m, low, mid-1)
    
print(bin_search(m, 1, len_lst[-1]))