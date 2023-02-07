n = int(input())
start_num = 666
cnt = 0

while True:
    if '666' in str(start_num):
        cnt += 1
        if cnt == n:
            print(start_num)
            break
        else:
            start_num += 1
    else:
        start_num += 1
    