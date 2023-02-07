n = int(input())
cnt = 0

for i in range(1, n+1):
    while i >= 5:
        if i % 5 == 0:
            i = i // 5
            cnt += 1
        else:
            break
        
print(cnt)