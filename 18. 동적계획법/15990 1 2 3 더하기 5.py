lst = [[0, 0, 0] for _ in range(100001)]

lst[1] = [1, 0, 0]
lst[2] = [0, 1, 0]
lst[3] = [1, 1, 1]

for i in range(4, 100001):
    lst[i][0] = (lst[i-1][1] + lst[i-1][2]) % 1000000009
    lst[i][1] = (lst[i-2][0] + lst[i-2][2]) % 1000000009
    lst[i][2] = (lst[i-3][0] + lst[i-3][1]) % 1000000009

n = int(input())
for j in range(n):
    num = int(input())
    print(sum(lst[num]) % 1000000009)