n = input()
lst = list()

for i in range(len(n)):
    lst.append(int(n[i]))

print(''.join(list(map(str, sorted(lst, reverse=True)))))