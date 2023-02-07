import math

n = int(input())

for i in range(n):
    cnt = 0
    
    x1, y1, x2, y2 = map(int, input().split())
    
    circles = int(input())

    for i in range(circles):
        c1, c2, r = map(int, input().split())
        if math.sqrt((x1-c1)**2 + (y1-c2)**2) < r and math.sqrt((x2 - c1)**2 + (y2 - c2)**2) > r:
            cnt += 1
        elif math.sqrt((x2 - c1)**2 + (y2 - c2)**2) < r and math.sqrt((x1-c1)**2 + (y1-c2)**2) > r:
            cnt += 1
            
    print(cnt)