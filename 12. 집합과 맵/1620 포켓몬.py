import sys

n, m = map(int, sys.stdin.readline().split())
poke_lst = dict()
int_lst = dict()

for i in range(1, n+1):
    pokemon = sys.stdin.readline().strip()
    poke_lst[i] = pokemon
    int_lst[pokemon] = i
    
for j in range(m):
    test = sys.stdin.readline().strip()
    if test.isdigit():
        print(poke_lst[int(test)])
    else:
        print(int_lst[test])