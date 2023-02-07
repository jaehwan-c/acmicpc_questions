n, m = map(int, input().split())

lst = list()

def n_m_1():
    if len(lst) == m:
        print(*lst)
    
    else:
        for i in range(1, n+1):
            if i in lst:
                continue
            else:
                lst.append(i)
                n_m_1()
                lst.pop()

n_m_1()                