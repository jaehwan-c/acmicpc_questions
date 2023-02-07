n = int(input())
    
def fibo_2(n):
    global cnt_2
    cnt_lst = [1 for _ in range(n+1)]
    for i in range(3, n+1):
        cnt_2 += 1
        cnt_lst[i] = cnt_lst[i-2] + cnt_lst[i-1]
            
    return cnt_lst[n]

cnt_2 = 0
cnt_1 = fibo_2(n)

print(cnt_1, cnt_2)