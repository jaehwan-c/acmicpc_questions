n = int(input())

input_lst = list()

for i in range(n):
    input_lst.append(list(map(int, input().split())))

for i in range(1, n):
    input_lst[i][0] = min(input_lst[i-1][1], input_lst[i-1][2]) + input_lst[i][0]
    input_lst[i][1] = min(input_lst[i-1][0], input_lst[i-1][2]) + input_lst[i][1]
    input_lst[i][2] = min(input_lst[i-1][0], input_lst[i-1][1]) + input_lst[i][2]
    
print(min(input_lst[n-1]))