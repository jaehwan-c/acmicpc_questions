max_val = 1000000
dp = [0] * (max_val+1)
sum_lst = [0] * (max_val+1)

for i in range(1, max_val+1):
    j = 1
    while i * j <= max_val:
        dp[i*j] += i
        j += 1
        
for i in range(1, max_val+1):
    sum_lst[i] = sum_lst[i-1] + dp[i]
  
t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    ans.append(sum_lst[n])

print('\n'.join(map(str,ans))+'\n')