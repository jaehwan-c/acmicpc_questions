n = int(input())

lst = [0 for _ in range(n+2)]

lst[1], lst[2] = 1, 2

for i in range(3, n+1):
    lst[i] = (lst[i-2] + lst[i-1]) % 15746
    
print(lst[n])