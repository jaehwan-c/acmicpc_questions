string = str(input())
lst = [str(i) for i in string]

lst_to_comp = list()
for i in range(0,26):
    lst_to_comp.append(chr(i+97))

for i in range(len(lst)):
    for a in range(0,26):
        if lst_to_comp[a] == lst[i]:
            lst_to_comp[a] = i

for i in range(len(lst_to_comp)):
    if isinstance(lst_to_comp[i], int):
        continue
    else:
        lst_to_comp[i] = -1

print(*lst_to_comp)

