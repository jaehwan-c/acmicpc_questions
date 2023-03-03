import sys

n = int(sys.stdin.readline())

for i in range(n):
    input_str = list(input())
    test_val = 0
    
    for j in input_str:
        if j == '(':
            test_val += 1
        else:
            test_val -= 1
        if test_val < 0:
            print('NO')
            break
        
    
    if test_val == 0:
        print('YES')
    elif test_val > 0:
        print('NO')