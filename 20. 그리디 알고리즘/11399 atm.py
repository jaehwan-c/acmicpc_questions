n = int(input())
queue_lst = list(map(int, input().split()))

queue_lst.sort()
waiting_min = 0

for i in range(n):
    waiting_min += queue_lst[i]*(n-i)
    
print(waiting_min)