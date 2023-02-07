import sys

n = int(input())
lst = list()
len_lst = list()


for i in range(n):
    a = str(input())
    if a not in lst:
        lst.append(a)
        len_lst.append(len(a))

dict_to_print = dict(zip(lst, len_lst))

x = list(dict(sorted(dict_to_print.items(), key=lambda x:[x[1], x[0]])).keys())

for i in range(len(x)):
    print(x[i])