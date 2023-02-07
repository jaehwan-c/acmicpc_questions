n = int(input())

time_lst = list()

for i in range(n):
    time_lst.append(list(map(int, input().split())))
    
time_lst.sort(key = lambda x: (x[1], x[0]))

min_time = 0
cnt = 0

for i in range(n):
    if min_time == 0:
        min_time = time_lst[i][1]
        cnt += 1
    else:
        if min_time <= time_lst[i][0]:
            min_time = time_lst[i][1]
            cnt += 1

print(cnt)