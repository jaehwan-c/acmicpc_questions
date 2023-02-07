n = int(input())
for i in range(n):
    a, b = map(str,input().split(" "))
    a = int(a)
    c = str()
    for i in b:
        c += a*i
    print(c)
