from collections import Counter

for i in range(int(input())):
    gear_lst = list()
    for j in range(int(input())):
        a, b = input().split()
        gear_lst.append(b)
    
    cnt = Counter(gear_lst)
    cnt_num = 1
    for k in cnt:
        cnt_num *= cnt[k] + 1
    print(cnt_num-1)