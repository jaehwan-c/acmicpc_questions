lst = input().split('-')
int_lst = list()

for i in lst:
    tmp_num = list(map(int, i.split('+')))
    int_lst.append(sum(tmp_num))

if len(int_lst) == 1:
    print(int_lst[0])
else:
    print(int_lst[0] - sum(int_lst[1:]))