n, m = map(int, input().split(' '))

money_lst = list()

for i in range(n):
    money_lst.append(int(input()))

money_lst.sort(reverse=True)

remaining = m
cnt = 0

for i in money_lst:
    if remaining >= i:
        cnt += remaining // i
        remaining = remaining % i
        if remaining == 0:
            break
        
print(cnt)