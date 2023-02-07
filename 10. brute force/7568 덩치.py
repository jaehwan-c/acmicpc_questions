trl = int(input())
lst = list()

for i in range(trl):
    lst.append(input().split())

for i in range(trl):
    lvl = 1
    for j in range(trl):
        if int(lst[i][0]) < int(lst[j][0]) and int(lst[i][1]) < int(lst[j][1]):
            lvl += 1
    print(lvl,end=" ")