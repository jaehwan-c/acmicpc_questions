import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque([i+1 for i in range(n)])

print('<', end='')
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')