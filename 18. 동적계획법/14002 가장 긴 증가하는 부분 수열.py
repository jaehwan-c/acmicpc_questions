n = int(input())
lst = list(map(int, input().split()))

# longest increaseing sequence
dp = [0] * (n + 1)

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j]:
            dp[i] = dp[j] 
    dp[i] += 1

print(max(dp))

target = max(dp)

# printing actual sequence
to_print = list()

for j in range(n-1, -1, -1):
    if dp[j] == target:
        to_print.append(lst[j])
        target -= 1

to_print.reverse()
print(*to_print)