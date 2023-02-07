n = int(input())
sum_num = 0

for i in range(1, n+1):
    sum_num += (n // i) * i

print(sum_num)