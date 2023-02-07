import sys

n = int(input())
checklst = sorted(list(map(int, sys.stdin.readline().split())))

def binary_search(data, target, low, high):
    if low > high:
        return 0
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return 1
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)
        
m = int(input())
datalst = list(map(int, sys.stdin.readline().split()))
lst_to_print = list()

for i in range(m):
    lst_to_print.append(binary_search(checklst, datalst[i], 0, n-1))
    
print(*lst_to_print)