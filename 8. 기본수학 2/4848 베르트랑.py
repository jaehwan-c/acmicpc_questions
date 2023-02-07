def pr_detector(i):
    if i == 1: 
        return False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0: 
            return False
    return True

or_lst = list(range(2,246912))
pr_lst = []

for i in or_lst:
    if pr_detector(i):
        pr_lst.append(i)

while(1):
    to_print = 0
    n = int(input())
    if n == 0:
        break
    for i in pr_lst:
        if n < i <= n*2:
            to_print += 1

    print(to_print)