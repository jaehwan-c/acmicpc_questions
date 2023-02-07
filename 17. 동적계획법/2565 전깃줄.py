n = int(input())

lst = list()
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key = lambda x:x[0])

dp = [0] * n
for i in range(n):
    for j in range(i):
        if lst[i][1] > lst[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))