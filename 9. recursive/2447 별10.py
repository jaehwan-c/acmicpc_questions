n = int(input())

def star(n):
    if n == 3:
        return ['***','* *','***']
    pre_arr = star(n//3)
    to_prt = []
    for i in pre_arr:
        to_prt.append(i*3)
    for i in pre_arr:
        to_prt.append(i+' '*(n//3)+i)
    for i in pre_arr:
        to_prt.append(i*3)
    return to_prt

print("\n".join(star(n)))