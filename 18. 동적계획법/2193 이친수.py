lst = [0] * 91

n = int(input())

lst[1] = 1

for i in range(2, n + 1):
    lst[i] = lst[i - 2] + lst[i - 1]

print(lst[n])