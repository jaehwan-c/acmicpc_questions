a = int(input())
lst = [a]
i = 0

while(True):
    b = lst[i] // 10
    c = lst[i] % 10
    d = c*10+(b+c)%10
    lst.append(d)
    i+=1
    if (lst[i] == a):
        print(i)
        break
        
