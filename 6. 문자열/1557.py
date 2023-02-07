a = str(input())
lst = [i for i in a]
lst_to_comp = [0 for i in range(27)]
value_to_comp = 0
value_to_print = 0

for i in range(len(lst)):
    if 97 <= ord(lst[i]) <= 122:
        to_add = ord(lst[i])-97
        lst_to_comp[to_add] += 1
    else:
        to_add = ord(lst[i])-65
        lst_to_comp[to_add] += 1

for i in range(len(lst_to_comp)):
    if value_to_comp < lst_to_comp[i]:
        value_to_comp = lst_to_comp[i]
        value_to_print = chr(i+65)
    elif value_to_comp == lst_to_comp[i]:
        value_to_print = "?"

print(value_to_print)
