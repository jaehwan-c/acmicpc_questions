import math

n = int(input())
rad_lst = list(map(int, input().split()))
txt = "{num}/{den}"

for i in range(1, len(rad_lst)):
    gcd = math.gcd(rad_lst[0], rad_lst[i])
    print(txt.format(num = rad_lst[0] // gcd, den = rad_lst[i] // gcd))