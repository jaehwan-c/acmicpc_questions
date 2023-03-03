n = int(input())

dp_lst = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    dp_lst[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(len(dp_lst[i])):
        if j == 0:
            dp_lst[i][j] = dp_lst[i][j] + dp_lst[i-1][j]
        elif j == len(dp_lst[i]) - 1:
            dp_lst[i][j] = dp_lst[i][j] + dp_lst[i-1][j-1]
        else:
            dp_lst[i][j] = max(dp_lst[i-1][j-1], dp_lst[i-1][j]) + dp_lst[i][j]
        
print(max(dp_lst[-1]))