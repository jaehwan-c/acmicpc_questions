max_val = 1000000

dp = [1] * (max_val + 1)

for i in range(3, 1001):
    for j in range(i + i, max_val + 1, i):
        dp[j] = 0

while True:
    n = int(input())
    
    if n == 0:
        break
    
    else:
        for i in range(3, len(dp), 2):
            if dp[i] and dp[n-i]:
                print("%d = %d + %d" %(n, i, n-i))
                break