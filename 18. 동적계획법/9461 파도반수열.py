n = int(input())

def padovan(n):
    lst = [0 for _ in range(n+3)]
    lst[1], lst[2], lst[3] = 1, 1, 1
    for i in range(4, n+1):
        lst[i] = lst[i-3] + lst[i-2]
    print(lst[n])

for i in range(n):
    padovan(int(input()))