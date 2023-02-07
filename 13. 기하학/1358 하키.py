import math

w, h, x, y, p = map(int, input().split())

c1 = [x, y+h/2]
c2 = [x+w, y+h/2]

cnt = 0

for i in range(p):
    x1, y1 = list(map(int, input().split()))
    if c1[0] <= x1 <= c2[0] and y <= y1 <= y+h:
        cnt += 1
    elif c1[0]-h/2 <= x1 <= c1[0]:
        if math.sqrt((x1-c1[0])**2 + (y1-c1[1])**2) <= h/2:
            cnt += 1
    elif c2[0] <= x1 <= c2[0] + h/2:
        if math.sqrt((x1-c2[0])**2 + (y1-c2[1])**2) <= h/2:
            cnt += 1

print(cnt)