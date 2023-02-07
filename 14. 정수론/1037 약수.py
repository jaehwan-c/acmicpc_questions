n = int(input())
num_lst = list(map(int, input().split()))
num_lst = sorted(num_lst)

print(num_lst[0]*num_lst[-1])