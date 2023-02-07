n = int(input())
stair_lst = [0] * 10001
step_lst = [0] * 10001
    
for i in range(n):
    stair_lst[i] = int(input())
    
step_lst[0] = stair_lst[0]
step_lst[1] = stair_lst[1] + stair_lst[0]
step_lst[2] = max(step_lst[1], stair_lst[1] + stair_lst[2], stair_lst[0] + stair_lst[2])

for i in range(3, n):
    step_lst[i] = max(step_lst[i-1], step_lst[i-3] + stair_lst[i-1] + stair_lst[i], step_lst[i-2] + stair_lst[i])
  
print(step_lst[n-1])