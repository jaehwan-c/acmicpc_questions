n = int(input())
numlst = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if numlst[i] > numlst[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))