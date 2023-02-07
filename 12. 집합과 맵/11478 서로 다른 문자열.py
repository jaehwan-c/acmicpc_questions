import sys

n = sys.stdin.readline().strip()
lst = list()

for i in range(len(n)):
    for j in range(i, len(n)):
        to_append = n[i:j+1]
        lst.append(to_append)
        
print(len(set(lst)))