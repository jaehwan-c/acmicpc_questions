from collections import Counter

x = list()
y = list()

for i in range(3):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)

cnt_x = Counter(x)
cnt_y = Counter(y)

print(*[k for k, v in cnt_x.items() if v == 1], *[i for i, l in cnt_y.items() if l == 1])