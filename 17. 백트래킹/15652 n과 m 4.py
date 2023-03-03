n, m = map(int, input().split())

lst = list()

def n_m_2():
    if m == len(lst):
        print(*lst)
    
    elif len(lst) == 0:
        for i in range(1, n+1):
            lst.append(i)
            n_m_2()
            lst.pop()
    
    else:
        for i in range(1, n+1):
            if i >= max(lst):
                lst.append(i)
                n_m_2()
                lst.pop()

n_m_2()