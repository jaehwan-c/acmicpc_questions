n, m = map(int, input().split())

def cnt_2(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt

def cnt_5(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt

print(min(cnt_2(n) - cnt_2(n - m) - cnt_2(m), cnt_5(n) - cnt_5(n - m) - cnt_5(m)))