import sys

max_val = 1000000

dp = [1] * (max_val + 1)
prime_num = list()
dp_dic = {}

for i in range(2, 1001):
    if dp[i]:
        for j in range(i + i, max_val + 1, i):
            dp[j] = 0
            
for i in range(3, max_val + 1):
    if dp[i] == 1:
        prime_num.append(i)
        dp_dic[i] = 1

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    else:
        for i in range(len(prime_num)):
            if (n - prime_num[i] in dp_dic):
                print("%d = %d + %d" %(n, prime_num[i], n-prime_num[i]))
                break