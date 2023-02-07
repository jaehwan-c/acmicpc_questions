len = int(input())
lst = list(map(int, input().split()))
a = 0
maxn = 0

for i in range(len):
    if lst[i] > maxn:
        maxn = lst[i]
    a += lst[i]

print((a/len)/(maxn)*100)

