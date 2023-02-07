def pr_detector(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i**0.5 + 1)):
            if i % j == 0:
                return False
        return True
    
min, max = map(int, input().split())

for i in range(min, max+1):
    if pr_detector(i):
        print(i)
        
# 에라토스테네스의 체 사용