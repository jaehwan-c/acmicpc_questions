n, m = map(int, input().split())
test_set = list()
input_set = list()
cnt = 0

for i in range(n):
    test_set.append(input())

test_set = list(set(test_set))

for i in range(m):
    test_str = input()
    if test_str in test_set:
        cnt += 1
    
print(cnt)