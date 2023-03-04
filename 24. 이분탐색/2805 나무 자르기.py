import sys

n, m = map(int, sys.stdin.readline().split())

lst = sorted(list(map(int, sys.stdin.readline().split())))

def obtained_calc(mid):
    cnt = 0
    for i in lst:
        if i > mid:
            cnt += i-mid
    return cnt
        
def bin_search(m, low, high):
    if low > high:
        return high
    
    mid = (low + high) // 2
    obtained = obtained_calc(mid)
    
    if obtained >= m:
        return bin_search(m, mid+1, high)
    else:
        return bin_search(m, low, mid-1)
    
print(bin_search(m, 0, lst[-1]-1))