import sys

n = int(sys.stdin.readline())
num_lst = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
search_lst = list(map(int, sys.stdin.readline().split()))

def bin_search(lst, num, low, high):
    if low > high:
        return 0

    mid = (low + high) // 2
    
    if lst[mid] == num:
        return 1
    elif lst[mid] > num:
        return bin_search(lst, num, low, mid-1)
    elif lst[mid] < num:
        return bin_search(lst, num, mid+1, high)
    else:
        return 0
    
for i in search_lst:
    print(bin_search(num_lst, i, 0, len(num_lst)-1))