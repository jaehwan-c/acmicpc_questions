import math

n = int(input())
int_lst = list()
temp_lst = list()
lst_to_print = list()

for i in range(n):
    int_lst.append(int(input()))

int_lst.sort()

for i in range(n-1):
    temp_lst.append(int_lst[i+1] - int_lst[i])

temp_lst = list(set(temp_lst))
temp_lst.sort()

gcd = temp_lst[0]

for i in range(1, len(temp_lst)):
    gcd = math.gcd(gcd, temp_lst[i])

for i in range(2, int(gcd**0.5 + 1)):
    if gcd % i == 0:
        lst_to_print.append(i)
        lst_to_print.append(gcd // i)
    else:
        continue

lst_to_print.append(gcd)
lst_to_print = sorted(list(set(lst_to_print)))

print(*lst_to_print)