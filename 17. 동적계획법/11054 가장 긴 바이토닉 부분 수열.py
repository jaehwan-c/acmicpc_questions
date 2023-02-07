n = int(input())
numlst = list(map(int, input().split()))
dp = [0] * n
reverse_dp = [0] * n

for i in range(n):
    for j in range(i):
        if numlst[i] > numlst[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if numlst[i] > numlst[j] and reverse_dp[i] < reverse_dp[j]:
            reverse_dp[i] = reverse_dp[j]
    reverse_dp[i] += 1

print(max(list(dp[i] + reverse_dp[i] for i in range(n)))-1)