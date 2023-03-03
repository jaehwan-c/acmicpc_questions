from collections import deque

queue = deque([i+1 for i in range(int(input()))])

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
else:
    print(queue[0])