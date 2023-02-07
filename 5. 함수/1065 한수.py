def fnc(a):
    if a <= 99:
        to_count = a
    else:
        to_count = 99
        for i in range(100,a+1):
            res = list(map(int, str(i)))
            if res[0] - res[1] == res[1] - res[2]:
                to_count += 1
    return to_count
    
a = int(input())
print(fnc(a))
